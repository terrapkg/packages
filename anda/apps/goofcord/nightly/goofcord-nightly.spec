%global commit 70738d6b1d4e4ac1992c52f49869c587d062b33b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260127
%global ver 2.0.1^
%global base_name goofcord
%global git_name GoofCord
%global appid io.github.milkshiift.GoofCord

Name:          %{base_name}-nightly
Version:       %{ver}%{commit_date}.git.%{shortcommit}
Release:       1%?dist
License:       OSL-3.0
Summary:       A privacy-minded Legcord fork.
Group:         Applications/Internet
URL:           https://github.com/Milkshiift/%{git_name}
Source0:       %{url}/archive/%{commit}/%{git_name}-%{commit}.tar.gz
BuildRequires: anda-srpm-macros >= 0.2.26
BuildRequires: bun-bin
Packager:      Gilver E. <roachy@fyralabs.com>

%electronmeta -D

%description
A highly configurable and privacy minded Discord client.

%prep
%autosetup -n %{git_name}-%{commit}
%ifarch %{arm64} armv7l armv7hl armv7hnl
sed -i '/\"x64\",/d' electron-builder.ts
%endif

%build
%bun_build

%install
%electron_install -d %{base_name} -s %{base_name} -b %{base_name} -i %{base_name} -D -O -U %U -E UseOzonePlatform,WaylandWindowDecorations -I
install -Dm644 assetsDev/%{appid}.metainfo.xml -t %{buildroot}%{_metainfodir}

%check
%desktop_file_validate %{buildroot}%{_datadir}/applications/%{base_name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{base_name}
%{_datadir}/applications/%{base_name}.desktop
%{_libdir}/%{base_name}/
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/16x16/apps/%{base_name}.png
%{_hicolordir}/32x32/apps/%{base_name}.png
%{_hicolordir}/48x48/apps/%{base_name}.png
%{_hicolordir}/64x64/apps/%{base_name}.png
%{_hicolordir}/128x128/apps/%{base_name}.png
%{_hicolordir}/256x256/apps/%{base_name}.png
%{_hicolordir}/512x512/apps/%{base_name}.png
%{_hicolordir}/1024x1024/apps/%{base_name}.png

%changelog
* Sat Jun 28 2025 Gilver E. <rockgrub@disroot.org> - 1.10.1^20250615.git.3f5eda1
- Initial package
