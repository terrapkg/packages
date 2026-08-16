%global debug_package     %{nil}
%global fontname          cleartype
%global fontlicense       Microsoft EULA
%global fontlicenses      EULA eula.txt

%global fontfamily1       ClearType Calibri
%global fontsummary1      ClearType Calibri TTF font
%global fontpkgheader1    %{expand:
Obsoletes: %{name}-common < 1.0-5
}

%global fonts1            CALIBR*.TTF
%global fontconfs1        %{SOURCE1}
%global fontdescription1  %{expand:
%{common_description}
Microsoft Calibri font, part of the ClearType collection made available
in the PowerPointViewer package, still available on the Microsoft website.
}

%global fontfamily2       ClearType Cambria
%global fontsummary2      ClearType Cambria TTF font
%global fontpkgheader2    %{expand:
Obsoletes: %{name}-common < 1.0-5
}

%global fonts2            CAMBRI*.TTF
%global fontconfs2        %{SOURCE2}
%global fontdescription2  %{expand:
%{common_description}
Microsoft Cambria font, part of the ClearType collection made available
in the PowerPointViewer package, still available on the Microsoft website.
}

%global fontfamily3       ClearType Candara
%global fontsummary3      ClearType Candara TTF font
%global fontpkgheader3    %{expand:
Obsoletes: %{name}-common < 1.0-5
}

%global fonts3            CANDAR*.TTF
%global fontconfs3        %{SOURCE3}
%global fontdescription3  %{expand:
%{common_description}
Microsoft Candara font, part of the ClearType collection made available
in the PowerPointViewer package, still available on the Microsoft website.
}

%global fontfamily4       ClearType Consolas
%global fontsummary4      ClearType Consolas TTF font
%global fontpkgheader4    %{expand:
Obsoletes: %{name}-common < 1.0-5
}

%global fonts4            CONSOL*.TTF
%global fontconfs4        %{SOURCE4}
%global fontdescription4  %{expand:
%{common_description}
Microsoft Consolas font, part of the ClearType collection made available
in the PowerPointViewer package, still available on the Microsoft website.
}

%global fontfamily5       ClearType Constantia
%global fontsummary5      ClearType Constantia TTF font
%global fontpkgheader5    %{expand:
Obsoletes: %{name}-common < 1.0-5
}

%global fonts5            CONSTAN*.TTF
%global fontconfs5        %{SOURCE5}
%global fontdescription5  %{expand:
%{common_description}
Microsoft Constantia font, part of the ClearType collection made available
in the PowerPointViewer package, still available on the Microsoft website.
}

%global fontfamily6       ClearType Corbel
%global fontsummary6      ClearType Corbel TTF font
%global fontpkgheader6    %{expand:
Obsoletes: %{name}-common < 1.0-5
}

%global fonts6            CORBEL*.TTF
%global fontconfs6        %{SOURCE6}
%global fontdescription6  %{expand:
%{common_description}
Microsoft Corbel font, part of the ClearType collection made available
in the PowerPointViewer package, still available on the Microsoft website.
}

Name:           %{fontname}-fonts
Version:        1.0
Release:        2%{?dist}
Summary:        Package containing ClearType fonts.
License:        LicenseRef-MS-Core-Fonts
URL:            https://mscorefonts2.sourceforge.net
Group:          User Interface/X
Source0:        https://sourceforge.net/projects/mscorefonts2/files/cabs/PowerPointViewer.exe
Source1:        61-%{fontname}-calibri.conf
Source2:        61-%{fontname}-cambria.conf
Source3:        61-%{fontname}-candara.conf
Source4:        61-%{fontname}-consolas.conf
Source5:        61-%{fontname}-constantia.conf
Source6:        61-%{fontname}-corbel.conf
BuildRequires:  cabextract
BuildRequires:  fontpackages-devel
Requires:       xorg-x11-font-utils
Requires:       fontconfig
Requires:       %{fontname}-calibri-fonts
Requires:       %{fontname}-cambria-fonts
Requires:       %{fontname}-candara-fonts
Requires:       %{fontname}-consolas-fonts
Requires:       %{fontname}-constantia-fonts
Requires:       %{fontname}-corbel-fonts
Requires(post): fontconfig
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%fontpkg -a

%description
ClearType fonts made available to the public in the PowerPoint Viewer package in 2006.

%prep
%setup -cT
cabextract %{SOURCE0}
cabextract ppviewer.cab
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
