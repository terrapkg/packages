%global commit dbe10e789ae55aa0f1ab8828b0341ac1104849e0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20251204
%global ver 1.11.2
%global base_name goofcord
%global git_name GoofCord

%electronmeta

Name:          %{base_name}-nightly
Version:       %{ver}^%{commit_date}.git.%{shortcommit}
Release:       1%?dist
License:       OSL-3.0
Summary:       A privacy-minded Legcord fork.
Group:         Applications/Internet
URL:           https://github.com/Milkshiift/%{git_name}
Source0:       %{url}/archive/%{commit}/%{git_name}-%{commit}.tar.gz
BuildRequires: bun-bin
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: make
BuildRequires: nodejs
BuildRequires: nodejs-npm
BuildRequires: python3
%ifarch aarch64
BuildRequires: zlib-ng-compat-devel
%endif
Packager:      Gilver E. <rockgrub@disroot.org>

%description
A highly configurable and privacy minded Discord client.

%prep
%autosetup -n %{git_name}-%{commit}

%build
%ifarch aarch64 armv7hl armv7l
sed -i '/\"x64\",/d' electron-builder.ts
%endif
%bun_build -r build -R

%install
%electron_install -D -O -U %U -E UseOzonePlatform,WaylandWindowDecorations

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{git_name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{git_name}
%{_datadir}/applications/%{git_name}.desktop
%{_datadir}/%{git_name}/
%{_iconsdir}/hicolor/16x16/apps/%{git_name}.png
%{_iconsdir}/hicolor/32x32/apps/%{git_name}.png
%{_iconsdir}/hicolor/48x48/apps/%{git_name}.png
%{_iconsdir}/hicolor/64x64/apps/%{git_name}.png
%{_iconsdir}/hicolor/128x128/apps/%{git_name}.png
%{_iconsdir}/hicolor/256x256/apps/%{git_name}.png
%{_iconsdir}/hicolor/512x512/apps/%{git_name}.png
%{_iconsdir}/hicolor/1024x1024/apps/%{git_name}.png

%changelog
* Sat Jun 28 2025 Gilver E. <rockgrub@disroot.org> - 1.10.1^20250615.git.3f5eda1
- Initial package
