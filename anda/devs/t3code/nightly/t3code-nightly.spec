%undefine __brp_mangle_shebangs

%global appid gg.ping.T3Code-nightly

%global ver 0.0.46
%global commit 0fcd5f90611451cca842689faea53b5450c022da
%global date 20261008
%global run 2849
%global tag 0.0.46-nightly.20261008.2849
%global electron_version %{ver}-nightly.%{date}.%{run}

Name:           t3code-nightly
%electronmeta -D
Version:        %{ver}^%{date}^%{run}
Release:        1%{?dist}
Summary:        Minimal web GUI for coding agents
License:        MIT AND %{electron_license}
URL:            https://github.com/pingdotgg/t3code
Source0:        %{url}/archive/refs/tags/v%{tag}.tar.gz
Source1:        %{name}.desktop
Source2:        %{appid}.metainfo.xml

BuildRequires:  cargo
BuildRequires:  ImageMagick
BuildRequires:  pnpm
BuildRequires:  nodejs24
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  desktop-file-utils

Requires:       git-core
Suggests:       azure-cli
Suggests:       gh
Suggests:       glab

Conflicts:      t3code

Packager:       Addison LeClair <me@addi.lol>, Owen Zimmerman <owen@fyralabs.com>

%description
T3 Code is a minimal web GUI for coding agents such as Codex, Claude Code,
Cursor, and OpenCode.

%prep
%autosetup -n t3code-%{tag}
for manifest in apps/server/package.json apps/desktop/package.json apps/web/package.json packages/contracts/package.json; do
  node -e 'const fs = require("fs"); const [file, version] = process.argv.slice(1); const pkg = JSON.parse(fs.readFileSync(file, "utf8")); pkg.version = version; fs.writeFileSync(file, JSON.stringify(pkg, null, 2) + "\n");' "$manifest" %{electron_version}
done

%build
export T3CODE_DESKTOP_VERSION=%{electron_version}
export T3CODE_DESKTOP_PLATFORM=linux
export T3CODE_DESKTOP_TARGET=tar.xz
export T3CODE_DESKTOP_ARCH=%{_electron_cpu}
# needed for t3 connect (pulled from action runs)
export T3CODE_CLERK_PUBLISHABLE_KEY=pk_live_Y2xlcmsudDMuY29kZXMk
export T3CODE_CLERK_JWT_TEMPLATE=t3-relay
export T3CODE_CLERK_CLI_OAUTH_CLIENT_ID=hzxSgY2cH10sDU2r
export T3CODE_RELAY_URL=https://relay.t3.codes
%pnpm_build -F -r dist:desktop:artifact

%install
archive="$(find release -maxdepth 1 -name '*.tar.xz' -print -quit)"
mkdir -p dist
tar -xJf "$archive" -C dist --strip-components=1

find dist -path '*musl*' -delete
%ifarch x86_64
rm -rf dist/resources/app.asar.unpacked/node_modules/node-pty/prebuilds/linux-arm64
%elifarch aarch64
rm -rf dist/resources/app.asar.unpacked/node_modules/node-pty/prebuilds/linux-x64
%endif

install -dm755 %{buildroot}%{_libdir}/%{name}
cp -pr dist/. %{buildroot}%{_libdir}/%{name}/
chmod 4755 %{buildroot}%{_libdir}/%{name}/chrome-sandbox

install -dm755 %{buildroot}%{_bindir}
ln -sf %{_libdir}/%{name}/t3code %{buildroot}%{_bindir}/%{name}

install -dm755 %{buildroot}%{_hicolordir}/512x512/apps
magick assets/prod/black-universal-1024.png -resize 512x512 %{buildroot}%{_hicolordir}/512x512/apps/%{name}.png
chmod 644 %{buildroot}%{_hicolordir}/512x512/apps/%{name}.png

%desktop_file_install %{SOURCE1} %{buildroot}%{_appsdir}/%{name}.desktop

%terra_appstream -o %{SOURCE2}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_appsdir}/%{name}.desktop
%{_hicolordir}/*/apps/%{name}.png
%{_metainfodir}/%appid.metainfo.xml

%changelog
* Fri Oct 02 2026 Cypress Reed <cypress@fyralabs.com>
- Switch to using upstream nightly tags, fix desktop files for policy, add appstream metainfo

* Thu Oct 01 2026 Owen Zimmerman <owen@fyralabs.com>
- Remove conflicting arch bundled node modules

* Fri Sep 04 2026 Addison LeClair <me@addi.lol>
- Add new libsecret dependency

* Thu Jul 30 2026 Addison LeClair <me@addi.lol>
- Fix T3 Connect by adding missing auth variables
- Fix .desktop title to match upstream
- Fix version string to enable in-app nightly display.

* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Make nightly package

* Sun Jul 12 2026 Addison LeClair <me@addi.lol> - 0.0.28-1
- Initial package
