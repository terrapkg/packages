%global flist 3270 Agave AnonymousPro Arimo AurulentSansMono BigBlueTerminal BitstreamVeraSansMono CascadiaCode CodeNewRoman Cousine DaddyTimeMono DejaVuSansMono DroidSansMono FantasqueSansMono FiraCode FiraMono Go-Mono Gohu Hack Hasklig HeavyData Hermit IBMPlexMono Inconsolata InconsolataGo InconsolataLGC Iosevka JetBrainsMono Lekton LiberationMono Lilex MPlus Meslo Monofur Monoid Mononoki NerdFontsSymbolsOnly Noto OpenDyslexic Overpass ProFont ProggyClean RobotoMono ShareTechMono SourceCodePro SpaceMono Terminus Tinos Ubuntu UbuntuMono VictorMono iA-Writer
%global desc Nerd Fonts is a project that patches developer targeted fonts with a high number of glyphs (icons).

Name:		nerd-fonts
Version:	2.3.1
Release:	%autorelease
URL:		https://nerdfonts.com/
Source0:	https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v%{version}/readme.md
Source1:	https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v%{version}/LICENSE
License:	OFLv1.1
Summary:	All packaged Nerd fonts
BuildArch:	noarch
Requires:	%{lua:
local x = ""
local ver = rpm.expand("%{version}")
for font in (rpm.expand("%{flist}")):gmatch("[^ ]+") do
	x = x .. font:lower().."="..ver.." "
end
print(x)
}
BuildRequires:	unzip
%{lua:
local url = rpm.expand(": https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/");
local n = 2;
for font in (rpm.expand("%{flist}")):gmatch("[^ ]+") do
	print("Source"..n..url..font..".zip\n")
	n = n + 1
end
}

%description
%{desc} Specifically to add a high number of extra glyphs from popular
'iconic fonts' such as Font Awesome, Devicons, Octicons, and others.

%{lua:
for font in (rpm.expand("%{flist}")):gmatch("[^ ]+") do
	print("%package -n "..font:lower().."-nerd-fonts\n")
	print("Summary:\tPatched Nerd fonts: "..font)
	print("\n%description -n "..font:lower().."-nerd-fonts\n")
	print("%{desc}. The package contains the patched version of "..font..".\n")
end
}

%global debug_package %{nil}

%prep
mkdir fonts
%{lua:
local n = 2;
for font in (rpm.expand("%{flist}")):gmatch("[^ ]+") do
	local src = rpm.expand("%{SOURCE"..n.."}")
	print("unzip "..src.." -d fonts\n")
	n = n + 1
end
}

%build
echo "==========================================="
ls fonts
echo "==========================================="
find fonts -name "* Windows Compatible.*" -delete
find fonts -name "*.txt" -delete
find fonts -name "readme.md" -delete

%install
%{lua:
local dir = rpm.expand("%{buildroot}/%{_datadir}/fonts/nerd-fonts/");
for font in (rpm.expand("%{flist}")):gmatch("[^ ]+") do
	print("mv "..font.." "..dir)
end
}
install -Dm644 %{SOURCE0} "%{buildroot}/%{_datadir}/doc/%{name}/README.md"
install -Dm644 %{SOURCE1} "%{buildroot}/%{_datadir}/licenses/%{name}/LICENSE"


%files
%doc readme.md
%license LICENSE

%{lua:
for font in (rpm.expand("%{flist}")):gmatch("[^ ]+") do
	print("%files -n "..font:lower().."-nerd-fonts\n")
	print("%doc readme.md\n")
	print("%license LICENSE\n")
	print("/usr/share/fonts/nerd-fonts/"..font.."\n")
end
}


%changelog
* Wed Jan 4 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
