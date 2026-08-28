%undefine __brp_mangle_shebangs

Name:           t3code
%electronmeta -D
Version:        0.0.35
Release:        1%{?dist}
Summary:        Minimal web GUI for coding agents
License:        MIT AND %{electron_license}
URL:            https://github.com/pingdotgg/t3code
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  ImageMagick
BuildRequires:  pnpm

Requires:       git-core
Suggests:       azure-cli
Suggests:       gh
Suggests:       glab

Conflicts:      t3code-nightly

Packager:       Addison LeClair <me@addi.lol>

%description
T3 Code is a minimal web GUI for coding agents such as Codex, Claude Code,
Cursor, and OpenCode.

%prep
%autosetup -n %{name}-%{version}
for manifest in apps/server/package.json apps/desktop/package.json apps/web/package.json packages/contracts/package.json; do
  node -e 'const fs = require("fs"); const [file, version] = process.argv.slice(1); const pkg = JSON.parse(fs.readFileSync(file, "utf8")); pkg.version = version; fs.writeFileSync(file, JSON.stringify(pkg, null, 2) + "\n");' "$manifest" %{version}
done

%build
export T3CODE_DESKTOP_VERSION=%{version}
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

install -dm755 %{buildroot}%{_libdir}/%{name}
cp -pr dist/. %{buildroot}%{_libdir}/%{name}/
chmod 4755 %{buildroot}%{_libdir}/%{name}/chrome-sandbox

install -dm755 %{buildroot}%{_bindir}
ln -sf %{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

install -Dm644 assets/prod/black-universal-1024.png %{buildroot}%{_hicolordir}/1024x1024/apps/%{name}.png

cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=T3 Code (Alpha)
Comment=%{summary}
Exec=%{name} --ozone-platform-hint=auto %U
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;
StartupWMClass=%{name}
MimeType=x-scheme-handler/t3code;x-scheme-handler/t3code-dev;
EOF

%desktop_file_install %{name}.desktop

%check
%desktop_file_validate %{buildroot}%{_appsdir}/*.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_appsdir}/%{name}.desktop
%{_hicolordir}/*/apps/%{name}.png

%changelog
* Thu Jul 30 2026 Addison LeClair <me@addi.lol> - 0.0.31-1
- Fix T3 Connect by adding missing auth variables
- Fix .desktop title to match upstream
- Use correct icon

* Sun Jul 12 2026 Addison LeClair <me@addi.lol> - 0.0.28-1
- Initial package
