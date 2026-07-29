%undefine __brp_mangle_shebangs

Name:           t3code
%electronmeta -D
Version:        0.0.31
Release:        1%{?dist}
Summary:        Minimal web GUI for coding agents
License:        MIT AND %{electron_license}
URL:            https://github.com/pingdotgg/t3code
Source0:        https://github.com/pingdotgg/t3code/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  anda-srpm-macros
BuildRequires:  ImageMagick
BuildRequires:  pnpm

Requires:       git-core
Suggests:       azure-cli
Suggests:       gh
Suggests:       glab

Packager:       Addison LeClair <me@addi.lol>

%description
T3 Code is a minimal web GUI for coding agents such as Codex, Claude Code,
Cursor, and OpenCode.

%prep
%autosetup -n %{name}-%{version}

%build
export T3CODE_DESKTOP_VERSION=%{version}
export T3CODE_DESKTOP_PLATFORM=linux
export T3CODE_DESKTOP_TARGET=tar.xz
export T3CODE_DESKTOP_ARCH=%{_electron_cpu}
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

install -Dm644 apps/desktop/resources/icon.png %{buildroot}%{_hicolordir}/512x512/apps/%{name}.png

cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=T3 Code
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

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_appsdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%changelog
* Sun Jul 12 2026 Addison LeClair <me@addi.lol> - 0.0.28-1
- Initial package
