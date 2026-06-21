%define debug_package %nil
%global ver 2.003R

Name:           source-han-serif-fonts
Version:        %(echo %ver | sed -E 's/R$//')
Release:        1%?dist
Summary:        Source Han Serif | 思源宋体 | 思源宋體 | 思源宋體 香港 | 源ノ明朝 | 본명조
License:        OFL-1.1
URL:            https://github.com/adobe-fonts/source-han-serif
Source0:        %url/releases/download/%ver/03_SourceHanSerifOTC.zip
Source1:        %url/releases/download/%ver/02_SourceHanSerif-VF.zip
Packager:       madonuko <mado@fyralabs.com>
BuildArch:      noarch
BuildRequires:  unzip

%description
Source Han Serif is a set of OpenType Pan-CJK fonts.

This package ships the Static OTC versions.

%files
%license LICENSE.txt
%_datadir/fonts/%name/


%dnl ╭── %global fpkg(vhst:)
%global fpkg(vhst:) %{quote:
%package %{?-h:hw-}%{?-v:vf-}%{?-s:subset-}%{-t*}
Summary: %name: %{?-h:half-width }%{?-v:variable }%{?-s:subset }%{upper:%{-t*}} font files

%description %{?-h:hw-}%{?-v:vf-}%{?-s:subset-}%{-t*}
This package provides a specific font type of %name.
%{?-v:VF: variable font: Variable font weights are supported.
}%{?-h:HW: half-width: some proportional punctuations are turned into half-width.
The list can be seen here, at page 19~20, section "Proportional & Half-Width CJK Punctuation":
https://github.com/adobe-fonts/source-han-sans/blob/release/SourceHanSansReadMe.pdf
}%{?-s:Subset: The fonts are split into regional-specific subset fonts.
}

%files %{?-h:hw-}%{?-v:vf-}%{?-s:subset-}%{-t*}
%license LICENSE.txt}
%dnl ╰── %fpkg(vhst:)

%fpkg -vt otc
%_datadir/fonts/%name/SourceHanSerif-VF.*.ttc

%fpkg -vht otc
%_datadir/fonts/%name/SourceHanSerifHW-VF.*.ttc

%fpkg -vt otf
%_datadir/fonts/%name/SourceHanSerif-VF.otf
%_datadir/fonts/%name/SourceHanSerifHC-VF.otf
%_datadir/fonts/%name/SourceHanSerifK-VF.otf
%_datadir/fonts/%name/SourceHanSerifSC-VF.otf
%_datadir/fonts/%name/SourceHanSerifTC-VF.otf

%fpkg -vht otf
%_datadir/fonts/%name/SourceHanSerifHW-VF.otf
%_datadir/fonts/%name/SourceHanSerifHWHC-VF.otf
%_datadir/fonts/%name/SourceHanSerifHWK-VF.otf
%_datadir/fonts/%name/SourceHanSerifHWSC-VF.otf
%_datadir/fonts/%name/SourceHanSerifHWTC-VF.otf

%fpkg -vst otf
%_datadir/fonts/%name/SourceHanSerifCN-VF.otf
%_datadir/fonts/%name/SourceHanSerifHK-VF.otf
%_datadir/fonts/%name/SourceHanSerifJP-VF.otf
%_datadir/fonts/%name/SourceHanSerifKR-VF.otf
%_datadir/fonts/%name/SourceHanSerifTW-VF.otf

%fpkg -vt ttf
%_datadir/fonts/%name/SourceHanSerif-VF.ttf
%_datadir/fonts/%name/SourceHanSerifHC-VF.ttf
%_datadir/fonts/%name/SourceHanSerifK-VF.ttf
%_datadir/fonts/%name/SourceHanSerifSC-VF.ttf
%_datadir/fonts/%name/SourceHanSerifTC-VF.ttf

%fpkg -vht ttf
%_datadir/fonts/%name/SourceHanSerifHW-VF.ttf
%_datadir/fonts/%name/SourceHanSerifHWHC-VF.ttf
%_datadir/fonts/%name/SourceHanSerifHWK-VF.ttf
%_datadir/fonts/%name/SourceHanSerifHWSC-VF.ttf
%_datadir/fonts/%name/SourceHanSerifHWTC-VF.ttf

%fpkg -vst ttf
%_datadir/fonts/%name/SourceHanSerifCN-VF.ttf
%_datadir/fonts/%name/SourceHanSerifHK-VF.ttf
%_datadir/fonts/%name/SourceHanSerifJP-VF.ttf
%_datadir/fonts/%name/SourceHanSerifKR-VF.ttf
%_datadir/fonts/%name/SourceHanSerifTW-VF.ttf

%fpkg -vt otf-woff2
%_datadir/fonts/%name/SourceHanSerif-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifHC-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifK-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifSC-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifTC-VF.otf.woff2

%fpkg -vht otf-woff2
%_datadir/fonts/%name/SourceHanSerifHW-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifHWHC-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifHWK-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifHWSC-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifHWTC-VF.otf.woff2

%fpkg -vst otf-woff2
%_datadir/fonts/%name/SourceHanSerifCN-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifHK-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifJP-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifKR-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifTW-VF.otf.woff2

%fpkg -vt ttf-woff2
%_datadir/fonts/%name/SourceHanSerif-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifHC-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifK-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifSC-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifTC-VF.ttf.woff2

%fpkg -vht ttf-woff2
%_datadir/fonts/%name/SourceHanSerifHW-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifHWHC-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifHWK-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifHWSC-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifHWTC-VF.ttf.woff2

%fpkg -vst ttf-woff2
%_datadir/fonts/%name/SourceHanSerifCN-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifHK-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifJP-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifKR-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifTW-VF.ttf.woff2


%prep
unzip %{S:0}
unzip %{S:1}

%build

%install
install -Dpm644 OTC/SourceHanSerif-*.ttc -t %buildroot%_datadir/fonts/%name
install -Dpm644 Variable/OTC/*.* -t %buildroot%_datadir/fonts/%name
install -Dpm644 Variable/{,WOFF2/}{OTF,TTF}/{,HW/,Subset/}*.* -t %buildroot%_datadir/fonts/%name

%changelog
* Sat Jun 20 2026 madonuko <mado@fyralabs.com> - 2.005R-1
- Initial package.
