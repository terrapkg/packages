%global fontlicense       Microsoft EULA
%global fontlicenses      License.txt

%global fontfamily1       MS Core Tahoma
%global fontsummary1      Tahoma TTF font
%global fontpkgheader1    %{expand:
Obsoletes: %{name}-common < 1.0-5
}

%global fonts1            tahoma.ttf
%global fontconfs1        %{SOURCE1}
%global fontdescription1  %{expand:
%{common_description}
TTF Tahoma fonts that were made available to the public in the Word Reader
package.
}

### Different name because of font package and setup macro weirdness
Name:           mscore-tahoma-fonts
Version:        1.0
Release:        2%{?dist}
Summary:        Microsoft core Tahoma fonts for better Windows compatibility
License:        LicenseRef-MS-Core-Fonts
URL:            https://mscorefonts2.sourceforge.net
Group:          User Interface/X
Source0:        https://downloads.sourceforge.net/corefonts/the%%20fonts/final/wd97vwr32.exe
Source1:        61-ms-core-tahoma.conf
BuildRequires:  cabextract
BuildRequires:  fontpackages-devel
Requires:       xorg-x11-font-utils
Requires:       fontconfig
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%fontpkg -a

%description
TTF Tahoma fonts that were made available to the public in the Word Reader package.

Improves the look of Windows documents.


%prep
%setup -cT
cabextract %{SOURCE0}
cabextract Viewer1.cab
%forgesetup -a

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a
%fontfiles -a

%post
/usr/bin/fc-cache

%files

%changelog
* Mon Feb 24 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
