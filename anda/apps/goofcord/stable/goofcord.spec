%global git_name GoofCord
%global appid io.github.milkshiift.GoofCord

Name:          goofcord
Version:       2.1.0
Release:       3%?dist
License:       OSL-3.0
Summary:       A privacy-minded Legcord fork.
Group:         Applications/Internet
URL:           https://github.com/Milkshiift/%{git_name}
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
Patch0:        %{url}/commit/5be00d22d09f118fa5a2ac40deb12c54f66f03b8.patch
BuildRequires: anda-srpm-macros >= 0.3.0
BuildRequires: bun-bin
Packager:      Gilver E. <roachy@fyralabs.com>

%electronmeta -D

%description
A highly configurable and privacy minded Discord client.

%prep
%autosetup -p1 -n %{git_name}-%{version}
%ifarch %{arm64} armv7hl armv7l
sed -i '/\"x64\",/d' electron-builder.ts
%endif

%build
%bun_build

%install
%electron_install -D -O -U %U -E UseOzonePlatform,WaylandWindowDecorations -I

install -Dm644 assetsDev/%{appid}.metainfo.xml -t %{buildroot}%{_metainfodir}

%check
%desktop_file_validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}/
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/16x16/apps/%{name}.png
%{_hicolordir}/32x32/apps/%{name}.png
%{_hicolordir}/48x48/apps/%{name}.png
%{_hicolordir}/64x64/apps/%{name}.png
%{_hicolordir}/128x128/apps/%{name}.png
%{_hicolordir}/256x256/apps/%{name}.png
%{_hicolordir}/512x512/apps/%{name}.png
%{_hicolordir}/1024x1024/apps/%{name}.png

%changelog
* Sat Jun 28 2025 Gilver E. <rockgrub@disroot.org> - 1.10.1-1
- Initial package
