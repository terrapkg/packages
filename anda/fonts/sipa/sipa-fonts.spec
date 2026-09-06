%global fontcontact depathailand@depa.or.th
# note: SIPA is actually dead, superceded by depa
# This namespace is still kept for historical reasons,
# kinda like how packages from Meta still use the `com.facebook`
# namespace
%global fontorg th.or.sipa
Version:		20200217
Release:		8%{?dist}
URL:			https://www.nstda.or.th/home/news_post/thai-font/
%global fontlicense       LicenseRef-DIP-SIPA AND OFL-1.1-RFN
%global fontlicenses      LICENSE

%global common_description %{expand:
Thai National Fonts collection, freely-licensed computer fonts for the Thai
script sponsored by the Thai government.
}
# hoo boy, this is gonna be a long one

Name:			sipa-fonts
Provides:       %{name} = %{version}-%{release}
Obsoletes:      sipa-fonts < 20200217-5
Packager:       Cappy Ishihara <cappy@fyralabs.com>
Summary:		Thai National Fonts collection
Source0:		https://waa.inter.nstda.or.th/stks/pub/%(x=%version;echo ${x:0:4})/%version-13Fonts.zip
Requires:       tlwg-laksaman-fonts

# The packages were renamed
Obsoletes:      th-baijam-fonts
Obsoletes:      th-chakra-fonts
Obsoletes:      th-charm-fonts
Obsoletes:      th-charmonman-fonts
Obsoletes:      th-fahkwang-fonts
Obsoletes:      th-k2d-july8-fonts
Obsoletes:      th-kodchasal-fonts
Obsoletes:      th-koho-fonts
Obsoletes:      th-krub-fonts
Obsoletes:      th-mali-grade6-fonts
Obsoletes:      th-niramit-as-fonts
Obsoletes:      th-sarabun-fonts
Obsoletes:      th-sarabunnew-fonts
Obsoletes:      th-srisakdi-fonts

# migration path for old versions
Requires:       %{name}-all
# The SIPA license is a custom localized variant of the OFL,
# which means it's open source. It's a one-off license just for
# this package so this is necessary,
# and these fonts are an open-source, state-sponsored package
# required for official Thai documentation
License:		LicenseRef-DIP-SIPA
Source2:        SIPA-LICENSE
BuildRequires:  rpm_macro(fontpkg)
Supplements:    (default-fonts-th)
Supplements:    langpacks-th-fonts
BuildArch:		noarch

%description
%{common_description}

%global fontfamily1        TH Sarabun PSK
%global foundry1           Suppakit Chalermlarp
%global fonts1             'TH Sarabun'.ttf 'TH Sarabun Italic.ttf' 'TH Sarabun Bold.ttf' 'TH Sarabun BoldItalic.ttf'
%global fontsummary1       %{fontfamily1} font family
%global fontdescription1   %{common_description}

%global fontfamily2        TH Sarabun New
%global foundry2           %foundry1
%global fontlicense2       OFL-1.1-RFN
%global fonts2             'TH Sarabun New'*.ttf
%global fontsummary2       Revision of the %{fontfamily1} font family
%global fontdescription2   %{common_description}

%global fontfamily3        TH Charmonman
%global foundry3           Ekkalak Phianphanawet
%global fonts3             'TH Charmonman'*.ttf
%global fontsummary3       %{fontfamily3} font family
%global fontdescription3   %{common_description}

%global fontfamily4        TH Krub
%global foundry4           Ekkalak Phianphanawet
%global fonts4             'TH Krub'*.ttf
%global fontsummary4       %{fontfamily4} font family
%global fontdescription4   %{common_description}

%global fontfamily5        TH Srisakdi
%global foundry5           Aksaramethi
%global fonts5             'TH Srisakdi'*.ttf
%global fontsummary5       %{fontfamily5} font family
%global fontdescription5   %{common_description}

%global fontfamily6        TH Niramit AS
%global foundry6           Aksaramethi
%global fonts6             'TH Niramit AS'*.ttf
%global fontsummary6       %{fontfamily6} font family
%global fontdescription6   %{common_description}

%global fontfamily7        TH Charm of AU
%global foundry7           Kanlayanamit Noraratphutthi
%global fonts7             'TH Charm of AU'*.ttf
%global fontsummary7       %{fontfamily7} font family
%global fontdescription7   %{common_description}

%global fontfamily8        TH Kodchasal
%global foundry8           Kansuda Piamprachakphong
%global fonts8             'TH Kodchasal'*.ttf
%global fontsummary8       %{fontfamily8} font family
%global fontdescription8   %{common_description}

%global fontfamily9        TH K2D July8
%global foundry9           Kan Rotsawat
%global fonts9             'TH K2D July8'*.ttf
%global fontsummary9       %{fontfamily9} font family
%global fontdescription9   %{common_description}

%global fontfamily10       TH Mali Grade 6
%global foundry10          Sudarat Leotsithong
%global fonts10            'TH Mali Grade6'*.ttf
%global fontsummary10      %{fontfamily10} font family
%global fontdescription10  %{common_description}

%global fontfamily11       TH Chakra Petch
%global foundry11          Thirawat Photwibunsiri
%global fonts11            'TH Chakra Petch'*.ttf
%global fontsummary11      %{fontfamily11} font family
%global fontdescription11  %{common_description}

%global fontfamily12       TH Bai Jamjuree CP
%global foundry12          PITA
%global fonts12            'TH Baijam'*.ttf
%global fontsummary12      %{fontfamily12} font family
%global fontdescription12  %{common_description}

%global fontfamily13       TH KoHo
%global foundry13          KoHo
%global fonts13            'TH KoHo'*.ttf
%global fontsummary13      %{fontfamily13} font family
%global fontdescription13  %{common_description}

%global fontfamily14       TH Fah Kwang
%global foundry14          Team 11
%global fonts14            'TH Fahkwang'*.ttf
%global fontsummary14      %{fontfamily14} font family
%global fontdescription14  %{common_description}


%fontpkg -a
%fontmetapkg
# pull in tlwg-laksaman-fonts
# since this actually provides a fix for TH Sarabun
# (#6929) (#2482)


%prep
%autosetup -n Fonts
cp -v %{SOURCE2} LICENSE

%build
touch METAPKG
mv "THSarabun Bold Italic.ttf"		"TH Sarabun Bold Italic.ttf"
mv "THSarabun Bold.ttf"				"TH Sarabun Bold.ttf"
mv "THSarabun BoldItalic.ttf"		"TH Sarabun BoldItalic.ttf"
mv "THSarabun Italic.ttf"			"TH Sarabun Italic.ttf"
mv "THSarabun.ttf"					"TH Sarabun.ttf"
mv "THSarabunNew Bold.ttf"			"TH Sarabun New Bold.ttf"
mv "THSarabunNew BoldItalic.ttf"	"TH Sarabun New BoldItalic.ttf"
mv "THSarabunNew Italic.ttf"		"TH Sarabun New Italic.ttf"
mv "THSarabunNew.ttf"				"TH Sarabun New.ttf"
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%files
%license LICENSE

%fontfiles -a


%changelog
* Mon Sep 29 2025 Cappy Ishihara <cappy@fyralabs.com> - 20200217-5
- Use Fedora macros to build and install fonts
- Auto-generate AppStream metadata for fonts

* Sun Jun 11 2023 madonuko <mado@fyralabs.com> - 20200217-1
- Initial package
