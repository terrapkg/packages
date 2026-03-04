%global orgprefix fyralabs
%global fontcontact security@fyralabs.com
%global fontorg co.tauos
%global foundry           Fyra Labs
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.md
%global fontdocs          README.md

Version:        1.0.0
Release:        1%{?dist}
%global fontfamily        Natrium
%global fontsummary       Natrium - The tauOS UI font
%global fonts             Natrium/otf/*.otf
%global fontdescription   %fontsummary

URL:            https://github.com/tau-OS/natrium
Provides:       natrium-fonts = %{version}-%{release}
Source0:        %url/releases/download/v%{version}/natrium-fonts.zip

BuildRequires:	fontforge
BuildRequires:  rpm_macro(fontpkg)


%global fonts2             NatriumMono/otf/*.otf
%global fontfamily2        Natrium Mono
%global fontsummary2       Natrium Mono - The tauOS monospace font
%global fontdescription2   %fontsummary2

%fontpkg -a
%fontmetapkg


%prep
%autosetup -c

%build
%fontbuild

%install
%fontinstall -a



%check
%fontcheck -a

%fontfiles -a
