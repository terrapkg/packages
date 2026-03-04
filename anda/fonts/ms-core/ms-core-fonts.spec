%global                   fontname ms-core
%global sf_url            https://downloads.sourceforge.net/corefonts/the%20fonts/final
%global fontlicense       Microsoft EULA
%global fontlicenses      Licen.TXT

%global fontfamily1       MS Core Andale
%global fontsummary1      Microsoft Andale Mono TTF font
%global fontpkgheader1    %{expand:
Obsoletes: %{name}-common <= 2.2-4
}

%global fonts1            AndaleMo.TTF
%global fontconfs1        %{SOURCE8}
%global fontdescription1  %{expand:
%{common_description}
Andale Mono font for the web that prior to 2002 was available from
http://www.microsoft.com/typography/fontpack.
}

%global fontfamily2       MS Core Arial
%global fontsummary2      Microsoft Arial TTF font
%global fontpkgheader2    %{expand:
Obsoletes: %{name}-common <= 2.2-4
}

%global fonts2            Arial*.ttf AriBlk.TTF
%global fontconfs2        %{SOURCE9}
%global fontdescription2  %{expand:
%{common_description}
Microsoft Arial font for the web that prior to 2002 was available from
http://www.microsoft.com/typography/fontpack/, updated in the European
Union Expansion Update circa May 2007, still available on the Microsoft
website.
}

%global fontfamily3       MS Core Comic
%global fontsummary3      Microsoft Comic Sans TTF font
%global fontpkgheader3    %{expand:
Obsoletes: %{name}-common <= 2.2-4
}

%global fonts3            Comic*.TTF
%global fontconfs3        %{SOURCE10}
%global fontdescription3  %{expand:
%{common_description}
Comic Sans bold and regular font for the web that prior to 2002 was available
from http://www.microsoft.com/typography/fontpack.
}

%global fontfamily4       MS Core Courier
%global fontsummary4      Microsoft Courier New TTF font
%global fontpkgheader4    %{expand:
Obsoletes: %{name}-common <= 2.2-4
}

%global fonts4            cour*ttf
%global fontconfs4        %{SOURCE11}
%global fontdescription4  %{expand:
%{common_description}
Courier New bold, bold italic, italic and regular font for the web that prior
to 2002 was available from http://www.microsoft.com/typography/fontpack.
}

%global fontfamily5       MS Core Georgia
%global fontsummary5      Microsoft Georgia TTF font
%global fontpkgheader5    %{expand:
Obsoletes: %{name}-common <= 2.2-4
}

%global fonts5            Georgi*TTF
%global fontconfs5        %{SOURCE12}
%global fontdescription5  %{expand:
%{common_description}
Georgia font for the web that prior to 2002 was available from
http://www.microsoft.com/typography/fontpack.
}

%global fontfamily6       MS Core Impact
%global fontsummary6      Microsoft Impact TTF font
%global fontpkgheader6    %{expand:
Obsoletes: %{name}-common <= 2.2-4
}

%global fonts6            Impact.TTF
%global fontconfs6        %{SOURCE13}
%global fontdescription6  %{expand:
%{common_description}
Impact font for the web that prior to 2002 was available from
http://www.microsoft.com/typography/fontpack.
}

%global fontfamily7       MS Core Times
%global fontsummary7      Microsoft Times New Roman TTF font
%global fontpkgheader7    %{expand:
Obsoletes: %{name}-common <= 2.2-4
}

%global fonts7            Times*.ttf
%global fontconfs7        %{SOURCE14}
%global fontdescription7  %{expand:
%{common_description}
Microsoft Times New Roman font for the web that prior to 2002 was available from
http://www.microsoft.com/typography/fontpack/, updated in the European
Union Expansion Update circa May 2007, still available on the Microsoft
website.
}

%global fontfamily8       MS Core Trebuchet
%global fontsummary8      Microsoft Trebuchet TTF font
%global fontpkgheader8    %{expand:
Obsoletes: %{name}-common <= 2.2-4
}

%global fonts8            trebuc*.ttf
%global fontconfs8        %{SOURCE15}
%global fontdescription8  %{expand:
%{common_description}
Microsoft Trebuchet font for the web that prior to 2002 was available
from http://www.microsoft.com/typography/fontpack, updated
in the European Union Expansion Update circa May 2007, still available
on the Microsoft website.
}

%global fontfamily9       MS Core Verdana
%global fontsummary9      Microsoft Verdana TTF font
%global fontpkgheader9    %{expand:
Obsoletes: %{name}-common <= 2.2-4
}

%global fonts9            Verdana*.ttf
%global fontconfs9        %{SOURCE16}
%global fontdescription9  %{expand:
%{common_description}
Microsoft Verdana font for the web that prior to 2002 was available from
http://www.microsoft.com/typography/fontpack/, updated in the European
Union Expansion Update circa May 2007, still available on the Microsoft
website.
}

%global fontfamily10      MS Core Webdings
%global fontsummary10     Microsoft Verdana TTF font
%global fontpkgheader10   %{expand:
Obsoletes: %{name}-common <= 2.2-4
}

%global fonts10           Webdings.TTF
%global fontconfs10       %{SOURCE17}
%global fontdescription10 %{expand:
%{common_description}
Webdings font for the web that prior to 2002 was available from
http://www.microsoft.com/typography/fontpack.
}

Name:            ms-core-fonts
Version:         2.2
Release:         2%{?dist}
Summary:         Microsoft core fonts
License:         LicenseRef-MS-Core-Fonts
URL:             https://mscorefonts2.sourceforge.net
Group:           User Interface/X
Source0:         https://sourceforge.net/projects/mscorefonts2/files/cabs/EUupdate.EXE
Source1:         %{sf_url}/andale32.exe
Source2:         %{sf_url}/arialb32.exe
Source3:         %{sf_url}/comic32.exe
Source4:         %{sf_url}/courie32.exe
Source5:         %{sf_url}/georgi32.exe
Source6:         %{sf_url}/impact32.exe
Source7:         %{sf_url}/webdin32.exe
Source8:         61-ms-core-andale.conf
Source9:         61-ms-core-arial.conf
Source10:        61-ms-core-comic.conf
Source11:        61-ms-core-courier.conf
Source12:        61-ms-core-georgia.conf
Source13:        61-ms-core-impact.conf
Source14:        61-ms-core-times.conf
Source15:        61-ms-core-trebuchet.conf
Source16:        61-ms-core-verdana.conf
Source17:        61-ms-core-webdings.conf
BuildRequires:   cabextract
BuildRequires:   fontpackages-devel
Requires:        fontconfig
Requires:        %{fontname}-andale-fonts
Requires:        %{fontname}-arial-fonts
Requires:        %{fontname}-comic-fonts
Requires:        %{fontname}-courier-fonts
Requires:        %{fontname}-georgia-fonts
Requires:        %{fontname}-impact-fonts
Requires:        %{fontname}-times-fonts
Requires:        %{fontname}-trebuchet-fonts
Requires:        %{fontname}-verdana-fonts
Requires:        %{fontname}-webdings-fonts
Requires:        xorg-x11-font-utils
Requires(post):  fontconfig
BuildArch:       noarch
Packager:        Gilver E. <roachy@fyralabs.com>

%fontpkg -a

%description
TrueType core fonts that prior to 2002 were available from http://www.microsoft.com/typography/fontpack/

Updated in the European Union Expansion Update circa May 2007.

Still available on the Microsoft website.

%prep
%setup -cT
cabextract %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} \
    %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}
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
