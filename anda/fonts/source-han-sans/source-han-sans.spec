%define debug_package %nil
%global ver 2.005R

Name:           source-han-sans
Version:        %(echo %ver | sed -E 's/R$//')
Release:        1%?dist
Summary:        Source Han Sans | 思源黑体 | 思源黑體 | 思源黑體 香港 | 源ノ角ゴシック | 본고딕
License:        OFL-1.1
URL:            https://github.com/adobe-fonts/source-han-sans
Source0:        %url/releases/download/%version/03_SourceHanSansOTC.zip
BuildArch:      noarch
BuildRequires:  unzip

%description
Source Han Sans is a set of OpenType Pan-CJK fonts.

This package ships the Static OTC versions.

%prep
unzip %{S:0}

%build

%install
install -Dpm644 SourceHanSans-*.ttc -t %buildroot%_datadir/fonts/%name

%files
%license LICENSE.txt
%_datadir/fonts/%name/

%changelog
* Sat Jun 20 2026 madonuko <mado@fyralabs.com> - 2.005-1
- Initial package.
