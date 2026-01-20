%global commit 73ece590b2efe9bc64fb472326e69d3d809c8b44
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260118
%global ver 2.0.1^
%global base_name goofcord
%global git_name GoofCord

%electronmeta

Name:          %{base_name}-nightly
Version:       %{ver}%{commit_date}.git.%{shortcommit}
Release:       2%{?dist}
License:       OSL-3.0
Summary:       A privacy-minded Legcord fork.
Group:         Applications/Internet
URL:           https://github.com/Milkshiift/%{git_name}
Source0:       %{url}/archive/%{commit}/%{git_name}-%{commit}.tar.gz
BuildRequires: anda-srpm-macros >= 0.2.26
BuildRequires: bun-bin
Packager:      Gilver E. <roachy@fyralabs.com>

%description
A highly configurable and privacy minded Discord client.

%prep
%autosetup -n %{git_name}-%{commit}

%build
%ifarch %{arm64} armv7hl armv7l
sed -i '/\"x64\",/d' electron-builder.ts
%endif
%bun_build -r build -R

%install
%electron_install -d %{base_name} -s %{base_name} -i %{base_name} -D -O -U %U -E UseOzonePlatform,WaylandWindowDecorations

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{base_name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{base_name}
%{_datadir}/applications/%{base_name}.desktop
%{_libdir}/%{base_name}/
%{_iconsdir}/hicolor/16x16/apps/%{base_name}.png
%{_iconsdir}/hicolor/32x32/apps/%{base_name}.png
%{_iconsdir}/hicolor/48x48/apps/%{base_name}.png
%{_iconsdir}/hicolor/64x64/apps/%{base_name}.png
%{_iconsdir}/hicolor/128x128/apps/%{base_name}.png
%{_iconsdir}/hicolor/256x256/apps/%{base_name}.png
%{_iconsdir}/hicolor/512x512/apps/%{base_name}.png
%{_iconsdir}/hicolor/1024x1024/apps/%{base_name}.png

%changelog
* Sat Jun 28 2025 Gilver E. <rockgrub@disroot.org> - 1.10.1^20250615.git.3f5eda1
- Initial package
