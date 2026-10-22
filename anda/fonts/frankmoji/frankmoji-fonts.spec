%global fontcontact talk@selwyn.cc
%global fontorg com.frankmoji
%global fonttag Beta0012

Version:        0.012
Release:        1%{?dist}
URL:            https://frankmoji.com/
Packager:       Selwyn <talk@selwyn.cc>

%global fontlicense       CC-BY-NC-ND-4.0
%global fontlicenses      LICENSE.txt
%global fontfamily        FrankMoji
%global fontsummary       Hand-drawn color emoji font by Frank Rausch
%global fonts             *.ttf
%global fontdescription   %fontsummary

Source0:        https://frankmoji.com/download/FrankMoji%{fonttag}-Font.zip

BuildRequires:  unzip
BuildRequires:  rpm_macro(fontpkg)

%fontpkg

%prep
%autosetup -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Wed Oct 21 2026 Selwyn <talk@selwyn.cc> - 0.012-1
- Initial package
