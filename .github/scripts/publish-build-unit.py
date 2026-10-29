#!/usr/bin/env python3
"""Publish RPM artifacts for one successful build unit."""

import base64
import json
import os
import subprocess
import sys
from pathlib import Path


def artifact_name(package: dict[str, object], unit_id: str, version: str) -> str:
    labels = package.get("labels", {})
    group = labels.get("group", "") if isinstance(labels, dict) else ""
    if unit_id:
        prefix = unit_id
    elif group:
        prefix = "group-" + base64.urlsafe_b64encode(str(group).encode()).decode().rstrip("=")
    else:
        prefix = "package-" + base64.urlsafe_b64encode(str(package["pkg"]).encode()).decode().rstrip("=")
    return f"{prefix}-{package['pkg']}-{package['arch']}-{version}".replace("/", "@")


def destination(package: dict[str, object], version: str, *, source: bool = False) -> str:
    labels = package.get("labels", {})
    subrepo = labels.get("subrepo") if isinstance(labels, dict) else None
    target = f"terra{version}"
    if subrepo:
        target += f"-{subrepo}"
    return target + ("-source" if source else "")


def main() -> int:
    packages = json.loads(os.environ["PACKAGES_JSON"])
    if not packages:
        print("No packages to publish.")
        return 0

    unit_id = os.environ.get("UNIT_ID", "")
    version = os.environ["BUILD_VERSION"]
    token = os.environ["SUBATOMIC_TOKEN"]
    rpm_uploads = []
    source_uploads = []
    uploaded_sources = set()

    # Validate the entire unit before uploading any of its artifacts.
    for package in packages:
        artifact_dir = Path("artifacts") / artifact_name(package, unit_id, version)
        rpms = sorted(path for path in (artifact_dir / "rpms").glob("*") if path.is_file())
        if not rpms:
            raise SystemExit(
                f"No RPM artifact found for {package['pkg']} ({package['arch']}); publishing aborted."
            )
        rpm_uploads.append((destination(package, version), rpms))

        pkg = package["pkg"]
        labels = package.get("labels", {})
        if pkg in uploaded_sources or labels.get("no_upload_srpms") == "1":
            continue
        srpms = sorted(path for path in (artifact_dir / "srpm").glob("*") if path.is_file())
        if not srpms:
            raise SystemExit(
                f"No source RPM artifact found for {pkg} ({package['arch']}); publishing aborted."
            )
        source_uploads.append((destination(package, version, source=True), srpms))
        uploaded_sources.add(pkg)

    for target, files in rpm_uploads + source_uploads:
        command = [
            "subatomic-cli",
            "upload",
            "--prune",
            "--server",
            "https://subatomic.fyralabs.com",
            "--token",
            token,
            target,
            *(str(path) for path in files),
        ]
        result = subprocess.run(command, check=False)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
