%global __make bmake
%global _make_output_sync %nil
%global fontcontact security@fyralabs.com
%global fontorg com.fyralabs.terra

Version:		2.2.0
Release:		1%?dist
URL:			https://www.cambus.net/spleen-monospaced-bitmap-fonts/

%global fontlicense       BSD-2-Clause
%global fontlicenses      LICENSE
%global fontdocs          FAQ ChangeLog AUTHORS README.md
%global fontfamily        Spleen
%global fontsummary       Monospaced bitmap fonts
%global fonts             *.otf
%global fontdescription   %fontsummary

Source0:		https://github.com/fcambus/spleen/archive/refs/tags/%version.zip

BuildRequires:	bmake fontforge
BuildRequires:	bdf2sfd
BuildRequires:  rpm_macro(fontpkg)

%fontpkg

%prep
%autosetup -n spleen-%version

%build
%make_build sfd
%make_build otf
%fontbuild

%install
install -Dm644 fonts.alias *.otf -t %buildroot%_fontbasedir/%name/
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a
%_fontbasedir/%name/fonts.alias
