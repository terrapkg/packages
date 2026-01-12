%global git_name GoofCord

%electronmeta

Name:          goofcord
Version:       2.0.0
Release:       1%?dist
License:       OSL-3.0
Summary:       A privacy-minded Legcord fork.
Group:         Applications/Internet
URL:           https://github.com/Milkshiift/%{git_name}
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires: anda-srpm-macros >= 0.2.26
BuildRequires: bun-bin
Packager:      Gilver E. <rockgrub@disroot.org>

%description
A highly configurable and privacy minded Discord client.

%prep
%autosetup -n %{git_name}-%{version}

%build
%ifarch %{arm64} armv7hl armv7l
sed -i '/\"x64\",/d' electron-builder.ts
%endif
%bun_build -r build -R

%install
%electron_install -D -O -U %U -E UseOzonePlatform,WaylandWindowDecorations

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}/
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%{_iconsdir}/hicolor/128x128/apps/%{name}.png
%{_iconsdir}/hicolor/256x256/apps/%{name}.png
%{_iconsdir}/hicolor/512x512/apps/%{name}.png
%{_iconsdir}/hicolor/1024x1024/apps/%{name}.png

%changelog
* Sat Jun 28 2025 Gilver E. <rockgrub@disroot.org> - 1.10.1-1
- Initial package
