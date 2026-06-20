%define debug_package %nil
%global ver 2.003R

Name:           source-han-serif
Version:        %(echo %ver | sed -E 's/R$//')
Release:        1%?dist
Summary:        Source Han Serif | 思源宋体 | 思源宋體 | 思源宋體 香港 | 源ノ明朝 | 본명조
License:        OFL-1.1
URL:            https://github.com/adobe-fonts/source-han-serif
Source0:        %url/releases/download/%version/03_SourceHanSerifOTC.zip
Packager:       madonuko <mado@fyralabs.com>
BuildArch:      noarch
BuildRequires:  unzip

%description
Source Han Serif is a set of OpenType Pan-CJK fonts.

This package ships the Static OTC versions.

%prep
unzip %{S:0}

%build

%install
install -Dpm644 SourceHanSerif-*.ttc -t %buildroot%_datadir/fonts/%name

%files
%license LICENSE.txt
%_datadir/fonts/%name/

%changelog
* Sat Jun 20 2026 madonuko <mado@fyralabs.com> - 2.005R-1
- Initial package.
