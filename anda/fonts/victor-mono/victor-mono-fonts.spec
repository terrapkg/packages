%global fontcontact victor.mono.font@gmail.com
%global fontorg io.github.rubjo

Version:        1.5.6
Release:        1%{?dist}
URL:            https://rubjo.github.io/victor-mono/
Packager:       ammix <maxim@ammix.dev>

%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.txt
%global fontdocs          README.md
%global fontfamily        Victor Mono
%global fontsummary       Free programming font with cursive italics and ligatures
%global fonts             TTF/*.ttf
%global fontdescription   %{expand:
Victor Mono is a free programming font with semi-connected cursive italics and
symbol ligatures.}

Source0:        https://github.com/rubjo/victor-mono/raw/v%{version}/public/VictorMonoAll.zip
Source1:        https://raw.githubusercontent.com/rubjo/victor-mono/v%{version}/README.md

BuildRequires:  unzip
BuildRequires:  rpm_macro(fontpkg)

%fontpkg

%prep
%autosetup -c
cp -p %{SOURCE1} README.md

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Fri Aug 28 2026 ammix <maxim@ammix.dev> - 1.5.6-1
- Initial package
