%global flist 3270 Agave AnonymousPro Arimo AurulentSansMono BigBlueTerminal BitstreamVeraSansMono CascadiaCode CodeNewRoman Cousine DaddyTimeMono DejaVuSansMono DroidSansMono FantasqueSansMono FiraCode FiraMono Go-Mono Gohu Hack Hasklig HeavyData Hermit IBMPlexMono Inconsolata InconsolataGo InconsolataLGC Iosevka JetBrainsMono Lekton LiberationMono Lilex MPlus Meslo Monofur Monoid Mononoki NerdFontsSymbolsOnly Noto OpenDyslexic Overpass ProFont ProggyClean RobotoMono ShareTechMono SourceCodePro SpaceMono Terminus Tinos Ubuntu UbuntuMono VictorMono iA-Writer
%global desc Nerd Fonts is a project that patches developer targeted fonts with a high number of glyphs (icons).

Name:		nerd-fonts
Version:	2.2.2
Release:	%autorelease
URL:		https://nerdfonts.com/
Source0:	https://github.com/ryanoasis/nerd-fonts/archive/refs/tags/v%{version}.tar.gz
License:	OFLv1.1
Summary:	All packaged Nerd fonts
Requires:	%{lua:
local x = ""
local ver = rpm.expand("%{version}")
for font in (rpm.expand("%{flist}")):gmatch("[^ ]+") do
	x = x .. font:lower().."="..ver.." "
end
print(x)
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

%prep
%autosetup -n %{name}-%{version}

%build
find patched-fonts -name "* Windows Compatible.*" -delete
find patched-fonts -name "font-info.md" -delete
find patched-fonts -name "readme.md" -delete

search() {
	for folder in $1/*; do
		if [[ -d "$folder/complete" ]]; then
			mv $folder/complete/* $folder/
			rmdir $folder/complete
		else
			if [[ -d $folder ]]; then
				search $folder
			fi
		fi
	done
	return 0
}
search patched-fonts

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/nerd-fonts/ 
cp -r patched-fonts/* %{buildroot}/%{_datadir}/fonts/nerd-fonts/


%files
%doc readme.md
%license LICENSE

%{lua:
for font in (rpm.expand("%{flist}")):gmatch("[^ ]+") do
	print("%files -n "..font:lower().."-nerd-fonts\n")
	print("%doc readme.md\n")
	print("%license LICENSE\n")
	print("%/usr/share/fonts/nerd-fonts/"..font.."\n")
end
}


%changelog
* Wed Jan 4 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
