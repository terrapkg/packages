%define debug_package %nil
%global ver 2.003R

Name:           adobe-source-han-serif-fonts
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


%dnl DO NOT CHANGE THIS TO `%global`, I REPEAT, DO NOT USE `%global`, OTHERWISE MACROS LIKE `%{-h}` DO NOT EXPAND.
%dnl Parameterized macros cannot be defined using `%global`. Guess I'm today years old. — mado
%dnl ╭── %define fpkg(vhs)
%define fpkg(vhs)                                                                                   \
%package -n adobe-source-han-serif-%{-h:hw-}%{-v:vf-}%{-s:subset-}%1-fonts                          \
Summary: %name: %{-h:half-width }%{-v:variable }%{-s:subset }%{upper:%1} font files                 \
                                                                                                    \
%description -n adobe-source-han-serif-%{-h:hw-}%{-v:vf-}%{-s:subset-}%1-fonts                      \
This package provides a specific font type of %name.                                                \
%{-v:VF: variable font: Variable font weights are supported.                                        \
}%{-h:HW: half-width: some proportional punctuations are turned into half-width.                    \
The list can be seen here, at page 19~20, section "Proportional & Half-Width CJK Punctuation":      \
https://github.com/adobe-fonts/source-han-sans/blob/release/SourceHanSansReadMe.pdf                 \
}%{-s:Subset: The fonts are split into regional-specific subset fonts.                              \
}                                                                                                   \
                                                                                                    \
%files -n adobe-source-han-serif-%{-h:hw-}%{-v:vf-}%{-s:subset-}%1-fonts                            \
%license LICENSE.txt
%dnl ╰── %define fpkg(vhs)

%fpkg -v otc
%_datadir/fonts/%name/SourceHanSerif-VF.*.ttc

%fpkg -v otf
%_datadir/fonts/%name/SourceHanSerif-VF.otf
%_datadir/fonts/%name/SourceHanSerifHC-VF.otf
%_datadir/fonts/%name/SourceHanSerifK-VF.otf
%_datadir/fonts/%name/SourceHanSerifSC-VF.otf
%_datadir/fonts/%name/SourceHanSerifTC-VF.otf

%fpkg -vs otf
%_datadir/fonts/%name/SourceHanSerifCN-VF.otf
%_datadir/fonts/%name/SourceHanSerifHK-VF.otf
%_datadir/fonts/%name/SourceHanSerifJP-VF.otf
%_datadir/fonts/%name/SourceHanSerifKR-VF.otf
%_datadir/fonts/%name/SourceHanSerifTW-VF.otf

%fpkg -v ttf
%_datadir/fonts/%name/SourceHanSerif-VF.ttf
%_datadir/fonts/%name/SourceHanSerifHC-VF.ttf
%_datadir/fonts/%name/SourceHanSerifK-VF.ttf
%_datadir/fonts/%name/SourceHanSerifSC-VF.ttf
%_datadir/fonts/%name/SourceHanSerifTC-VF.ttf

%fpkg -vs ttf
%_datadir/fonts/%name/SourceHanSerifCN-VF.ttf
%_datadir/fonts/%name/SourceHanSerifHK-VF.ttf
%_datadir/fonts/%name/SourceHanSerifJP-VF.ttf
%_datadir/fonts/%name/SourceHanSerifKR-VF.ttf
%_datadir/fonts/%name/SourceHanSerifTW-VF.ttf

%fpkg -v otf-woff2
%_datadir/fonts/%name/SourceHanSerif-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifHC-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifK-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifSC-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifTC-VF.otf.woff2

%fpkg -vs otf-woff2
%_datadir/fonts/%name/SourceHanSerifCN-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifHK-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifJP-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifKR-VF.otf.woff2
%_datadir/fonts/%name/SourceHanSerifTW-VF.otf.woff2

%fpkg -v ttf-woff2
%_datadir/fonts/%name/SourceHanSerif-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifHC-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifK-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifSC-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifTC-VF.ttf.woff2

%fpkg -vs ttf-woff2
%_datadir/fonts/%name/SourceHanSerifCN-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifHK-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifJP-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifKR-VF.ttf.woff2
%_datadir/fonts/%name/SourceHanSerifTW-VF.ttf.woff2


%prep
unzip %{S:0}
yes | unzip %{S:1}

%build

%install
install -Dpm644 OTC/SourceHanSerif-*.ttc -t %buildroot%_datadir/fonts/%name
install -Dpm644 Variable/OTC/*.* -t %buildroot%_datadir/fonts/%name
install -Dpm644 Variable/{,WOFF2/}{OTF,TTF}/{,Subset/}*.* -t %buildroot%_datadir/fonts/%name

%changelog
* Sat Jun 20 2026 madonuko <mado@fyralabs.com> - 2.005R-1
- Initial package.
