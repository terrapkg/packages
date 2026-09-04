%define debug_package %nil
%global ver 2.005R

Name:           adobe-source-han-sans-fonts
Version:        %(echo %ver | sed -E 's/R$//')
Release:        2%?dist
Summary:        Source Han Sans | 思源黑体 | 思源黑體 | 思源黑體 香港 | 源ノ角ゴシック | 본고딕
License:        OFL-1.1
URL:            https://github.com/adobe-fonts/source-han-sans
Source0:        %url/releases/download/%ver/03_SourceHanSansOTC.zip
Source1:        %url/releases/download/%ver/02_SourceHanSans-VF.zip
Packager:       madonuko <mado@fyralabs.com>
BuildArch:      noarch
BuildRequires:  unzip

%description
Source Han Sans is a set of OpenType Pan-CJK fonts.

This package ships the Static OTC versions.

%files
%license LICENSE.txt
%_datadir/fonts/%name/SourceHanSans-Bold.ttc
%_datadir/fonts/%name/SourceHanSans-ExtraLight.ttc
%_datadir/fonts/%name/SourceHanSans-Heavy.ttc
%_datadir/fonts/%name/SourceHanSans-Light.ttc
%_datadir/fonts/%name/SourceHanSans-Medium.ttc
%_datadir/fonts/%name/SourceHanSans-Normal.ttc
%_datadir/fonts/%name/SourceHanSans-Regular.ttc


%dnl DO NOT CHANGE THIS TO `%global`, I REPEAT, DO NOT USE `%global`, OTHERWISE MACROS LIKE `%{-h}` DO NOT EXPAND.
%dnl Parameterized macros cannot be defined using `%global`. Guess I'm today years old. — mado
%dnl ╭── %define fpkg(vhs)
%define fpkg(vhs)                                                                                   \
%package -n adobe-source-han-sans-%{-h:hw-}%{-v:vf-}%{-s:subset-}%1-fonts                           \
Summary: %name: %{-h:half-width }%{-v:variable }%{-s:subset }%{upper:%1} font files                 \
                                                                                                    \
%description -n adobe-source-han-sans-%{-h:hw-}%{-v:vf-}%{-s:subset-}%1-fonts                       \
This package provides a specific font type of %name.                                                \
%{-v:VF: variable font: Variable font weights are supported.                                        \
}%{-h:HW: half-width: some proportional punctuations are turned into half-width.                    \
The list can be seen here, at page 19~20, section "Proportional & Half-Width CJK Punctuation":      \
https://github.com/adobe-fonts/source-han-sans/blob/release/SourceHanSansReadMe.pdf                 \
}%{-s:Subset: The fonts are split into regional-specific subset fonts.                              \
}                                                                                                   \
                                                                                                    \
%files -n adobe-source-han-sans-%{-h:hw-}%{-v:vf-}%{-s:subset-}%1-fonts                             \
%license LICENSE.txt
%dnl ╰── %define fpkg(vhs)

%fpkg -v otc
%_datadir/fonts/%name/SourceHanSans-VF.*.ttc

%fpkg -vh otc
%_datadir/fonts/%name/SourceHanSansHW-VF.*.ttc

%fpkg -v otf
%_datadir/fonts/%name/SourceHanSans-VF.otf
%_datadir/fonts/%name/SourceHanSansHC-VF.otf
%_datadir/fonts/%name/SourceHanSansK-VF.otf
%_datadir/fonts/%name/SourceHanSansSC-VF.otf
%_datadir/fonts/%name/SourceHanSansTC-VF.otf

%fpkg -vh otf
%_datadir/fonts/%name/SourceHanSansHW-VF.otf
%_datadir/fonts/%name/SourceHanSansHWHC-VF.otf
%_datadir/fonts/%name/SourceHanSansHWK-VF.otf
%_datadir/fonts/%name/SourceHanSansHWSC-VF.otf
%_datadir/fonts/%name/SourceHanSansHWTC-VF.otf

%fpkg -vs otf
%_datadir/fonts/%name/SourceHanSansCN-VF.otf
%_datadir/fonts/%name/SourceHanSansHK-VF.otf
%_datadir/fonts/%name/SourceHanSansJP-VF.otf
%_datadir/fonts/%name/SourceHanSansKR-VF.otf
%_datadir/fonts/%name/SourceHanSansTW-VF.otf

%fpkg -v ttf
%_datadir/fonts/%name/SourceHanSans-VF.ttf
%_datadir/fonts/%name/SourceHanSansHC-VF.ttf
%_datadir/fonts/%name/SourceHanSansK-VF.ttf
%_datadir/fonts/%name/SourceHanSansSC-VF.ttf
%_datadir/fonts/%name/SourceHanSansTC-VF.ttf

%fpkg -vh ttf
%_datadir/fonts/%name/SourceHanSansHW-VF.ttf
%_datadir/fonts/%name/SourceHanSansHWHC-VF.ttf
%_datadir/fonts/%name/SourceHanSansHWK-VF.ttf
%_datadir/fonts/%name/SourceHanSansHWSC-VF.ttf
%_datadir/fonts/%name/SourceHanSansHWTC-VF.ttf

%fpkg -vs ttf
%_datadir/fonts/%name/SourceHanSansCN-VF.ttf
%_datadir/fonts/%name/SourceHanSansHK-VF.ttf
%_datadir/fonts/%name/SourceHanSansJP-VF.ttf
%_datadir/fonts/%name/SourceHanSansKR-VF.ttf
%_datadir/fonts/%name/SourceHanSansTW-VF.ttf

%fpkg -v otf-woff2
%_datadir/fonts/%name/SourceHanSans-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansHC-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansK-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansSC-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansTC-VF.otf.woff2

%fpkg -vh otf-woff2
%_datadir/fonts/%name/SourceHanSansHW-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansHWHC-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansHWK-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansHWSC-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansHWTC-VF.otf.woff2

%fpkg -vs otf-woff2
%_datadir/fonts/%name/SourceHanSansCN-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansHK-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansJP-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansKR-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSansTW-VF.otf.woff2

%fpkg -v ttf-woff2
%_datadir/fonts/%name/SourceHanSans-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansHC-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansK-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansSC-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansTC-VF.ttf.woff2

%fpkg -vh ttf-woff2
%_datadir/fonts/%name/SourceHanSansHW-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansHWHC-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansHWK-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansHWSC-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansHWTC-VF.ttf.woff2

%fpkg -vs ttf-woff2
%_datadir/fonts/%name/SourceHanSansCN-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansHK-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansJP-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansKR-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSansTW-VF.ttf.woff2


%prep
unzip %{S:0}
yes | unzip %{S:1}

%build

%install
install -Dpm644 OTC/SourceHanSans-*.ttc -t %buildroot%_datadir/fonts/%name
install -Dpm644 Variable/OTC/*.* -t %buildroot%_datadir/fonts/%name
install -Dpm644 Variable/{,WOFF2/}{OTF,TTF}/{,HW/,Subset/}*.* -t %buildroot%_datadir/fonts/%name
%changelog
* Sat Jun 20 2026 madonuko <mado@fyralabs.com> - 2.005-1
- Initial package.
