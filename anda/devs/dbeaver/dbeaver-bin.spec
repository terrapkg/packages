%define debug_package %nil
%global appid io.dbeaver.DBeaver

Name:           dbeaver-bin
Version:        26.1.5
Release:        1%?dist
Summary:        Free universal database tool and SQL client
License:        Apache-2.0
URL:            https://dbeaver.io
Source0:        https://github.com/dbeaver/dbeaver/releases/download/%version/dbeaver-ce-%version-linux-x86_64.tar.gz
Source1:        https://github.com/dbeaver/dbeaver/releases/download/%version/dbeaver-ce-%version-linux-aarch64.tar.gz
Packager:       madonuko <mado@fyralabs.com>
ExclusiveArch:  x86_64 aarch64
Provides:       dbeaver = %evr
Conflicts:      dbeaver

%description
Free multi-platform database tool for developers, SQL programmers, database administrators and analysts.

%prep
%ifarch x86_64
tar xf %{S:0}
%elifarch aarch64
tar xf %{S:1}
%endif

%global buildsubdir dbeaver

%build

%install
mkdir -p %buildroot{%_datadir,%_licensedir,%_bindir,%_hicolordir/256x256/apps,%_appsdir}
cp -r . %buildroot%_datadir/dbeaver-bin/
mv %buildroot%_datadir/%name/licenses %buildroot%_licensedir/%name
ln -s %_datadir/%name/dbeaver %buildroot%_bindir/dbeaver
ln -s %_datadir/%name/dbeaver.png %buildroot%_hicolordir/256x256/apps/dbeaver.png
mv %buildroot{%_datadir/%name,%_appsdir}/dbeaver-ce.desktop
mv %buildroot%_datadir/%name/readme.txt .

%terra_appstream

%files
%doc readme.txt
%_licensedir/%name
%_appsdir/dbeaver-ce.desktop
%_bindir/dbeaver
%_datadir/%name/
%_hicolordir/256x256/apps/dbeaver.png
%_metainfodir/%appid.metainfo.xml

%changelog
* Mon Aug 17 2026 madonuko <mado@fyralabs.com> - 26.1.5-1
- Initial package
