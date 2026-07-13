%undefine __brp_mangle_shebangs

Name:           t3code
%electronmeta -D
Version:        0.0.28
Release:        1%{?dist}
Summary:        Minimal web GUI for coding agents
License:        MIT AND %{electron_license}
URL:            https://github.com/pingdotgg/t3code

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
%pnpm_build -F -r dist:desktop:artifact

%install
appimage="$(find release -maxdepth 1 -name '*.AppImage' -print -quit)"
chmod +x "$appimage"
dd if=/dev/zero of="$appimage" bs=1 count=3 seek=8 conv=notrunc
"$appimage" --appimage-extract

install -dm755 %{buildroot}%{_libdir}/%{name}
cp -pr squashfs-root/. %{buildroot}%{_libdir}/%{name}/
find %{buildroot}%{_libdir}/%{name} -path '*musl*' -delete
chmod -R a+rX %{buildroot}%{_libdir}/%{name}
rm -rf %{buildroot}%{_libdir}/%{name}/AppRun \
       %{buildroot}%{_libdir}/%{name}/usr \
       %{buildroot}%{_libdir}/%{name}/.DirIcon \
       %{buildroot}%{_libdir}/%{name}/*.desktop

install -dm755 %{buildroot}%{_datadir}
cp -pr squashfs-root/usr/share/icons %{buildroot}%{_datadir}/

sed -i '/AppImage/d' squashfs-root/*.desktop
desktop-file-install \
    --set-key=Exec --set-value="%{name} --ozone-platform-hint=auto %U" \
    --set-key=Icon --set-value=%{name} \
    --dir=%{buildroot}%{_appsdir} \
    squashfs-root/*.desktop

install -dm755 %{buildroot}%{_bindir}
ln -sf %{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

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
