%undefine __brp_mangle_shebangs

Name:           t3code
%electronmeta -D
Version:        0.0.28
Release:        1%{?dist}
Summary:        Minimal web GUI for coding agents
License:        MIT AND %{electron_license}
URL:            https://github.com/pingdotgg/t3code
Source0:        https://github.com/pingdotgg/t3code/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  anda-srpm-macros
BuildRequires:  ImageMagick
BuildRequires:  pnpm

Packager:       Addison LeClair <me@addi.lol>

%description
T3 Code is a minimal web GUI for coding agents such as Codex, Claude Code,
Cursor, and OpenCode.

%prep
%git_clone %url v%version

%build
export T3CODE_DESKTOP_VERSION=%{version}
export T3CODE_DESKTOP_PLATFORM=linux
export T3CODE_DESKTOP_TARGET=tar.xz
export T3CODE_DESKTOP_ARCH=%{_electron_cpu}
%pnpm_build -F -r dist:desktop:artifact

%install
archive="$(find release -maxdepth 1 -name '*.tar.xz' -print -quit)"
mkdir -p dist
tar -xJf "$archive" -C dist

# electron-builder tar targets can extract either flat or under one top-level
# directory. Normalize the archive to a flat app payload in dist/.
topdir="$(find dist -mindepth 1 -maxdepth 1 -type d -print -quit)"
if [ -n "$topdir" ] && [ "$(find dist -mindepth 1 -maxdepth 1 -print | wc -l)" -eq 1 ]; then
    mv "$topdir" dist.tmp
    rm -rf dist
    mv dist.tmp dist
fi

find dist -path '*musl*' -delete
chmod -R a+rX dist

install -dm755 %{buildroot}%{_libdir}/%{name}
cp -pr dist/. %{buildroot}%{_libdir}/%{name}/

install -dm755 %{buildroot}%{_bindir}
ln -sf %{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

install -Dm644 apps/desktop/resources/icon.png %{buildroot}%{_hicolordir}/512x512/apps/%{name}.png

echo '[Desktop Entry]' > %{name}.desktop
echo 'Name=T3 Code' >> %{name}.desktop
echo 'Comment=Minimal web GUI for coding agents' >> %{name}.desktop
echo 'Exec=%{name} --ozone-platform-hint=auto %U' >> %{name}.desktop
echo 'Icon=%{name}' >> %{name}.desktop
echo 'Terminal=false' >> %{name}.desktop
echo 'Type=Application' >> %{name}.desktop
echo 'Categories=Development;' >> %{name}.desktop
echo 'StartupWMClass=t3code' >> %{name}.desktop
echo 'MimeType=x-scheme-handler/t3code;x-scheme-handler/t3code-dev;' >> %{name}.desktop

%desktop_file_install %{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%attr(4755, root, root) %{_libdir}/%{name}/chrome-sandbox
%{_appsdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%changelog
* Sun Jul 12 2026 Addison LeClair <me@addi.lol> - 0.0.28-1
- Initial package
