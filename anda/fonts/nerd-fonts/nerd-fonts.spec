%global desc %{expand:
Nerd Fonts is a project that patches developer targeted fonts with a high
number of glyphs (icons).}

Name:		nerd-fonts
Version:	3.5.1

%global flist %(curl -fsSL https://api.github.com/repos/ryanoasis/nerd-fonts/releases/tags/v%version |\
	jq -r '[.assets.[].name | select(type == "string" and contains(".tar.xz")) | gsub(".tar.xz"; "")] | join(" ")')

Release:	3%{?dist}
URL:		https://nerdfonts.com/
Source0:	https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v%version/readme.md
Source1:	https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v%version/LICENSE
License:	OFL-1.1
Summary:	All packaged Nerd fonts
BuildArch:	noarch
Recommends:	%{lua:
local x = ""
local ver = rpm.expand("%version-%release")
for font in (rpm.expand("%flist")):gmatch("[^ ]+") do
	x = x .. font:lower().."-nerd-fonts = "..ver.." "
end
print(x)
}
BuildRequires:	tar xz
%{lua:
local url = rpm.expand(": https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/");
local n = 2;
for font in (rpm.expand("%flist")):gmatch("[^ ]+") do
	print("Source"..n..url..font..".tar.xz\n")
	n = n + 1
end
}

%description
%{desc} Specifically to add a high number of extra glyphs from popular
'iconic fonts' such as Font Awesome, Devicons, Octicons, and others.

%{lua:
local desc = rpm.expand("%desc")
for font in (rpm.expand("%flist")):gmatch("[^ ]+") do
	print("%package -n "..font:lower().."-nerd-fonts\n")
	print("Summary:\tPatched Nerd fonts: "..font)
	print("\n%description -n "..font:lower().."-nerd-fonts\n")
	print(desc..". The package contains the patched version of "..font..".\n")
end
}

%global debug_package %nil

%prep
cp %SOURCE0 .
cp %SOURCE1 .

%build

%install
mkdir -p %buildroot/usr/share/fonts/nerd-fonts/
%{lua:
local dest = rpm.expand("%buildroot/usr/share/fonts/nerd-fonts/");
local fontconfig = rpm.expand("%buildroot/usr/share/fontconfig/conf.avail/");
local etc = rpm.expand("%buildroot/etc/fonts/conf.d/");
local file = "10-nerd-font-symbols.conf"
local n = 2;
for font in (rpm.expand("%flist")):gmatch("[^ ]+") do
	local src = rpm.expand("%SOURCE"..n)
	if font:find("NerdFontsSymbolsOnly", 1, true) then
		print("mkdir -p "..dest..font.." && tar -xJf "..src.." -C "..dest..font.."\n")
		print("mkdir -p "..fontconfig.." "..etc.."\n")
		print("mv "..dest..font.."/"..file.." "..fontconfig..file.."\n")
		print("ln -s /usr/share/fontconfig/conf.avail/"..file.." "..etc..file.."\n")
	else
		print("mkdir -p "..dest..font.." && tar -xJf "..src.." -C "..dest..font.." &\n")
	end
	n = n + 1
end
}
wait

find %buildroot/usr/share/fonts/nerd-fonts/ -name "* Windows Compatible.*" -delete &
find %buildroot/usr/share/fonts/nerd-fonts/ -name "*.txt" -delete &
find %buildroot/usr/share/fonts/nerd-fonts/ -name "readme.md" -delete &
wait

%files
%doc readme.md
%license LICENSE

%{lua:
for font in (rpm.expand("%flist")):gmatch("[^ ]+") do
	print("%files -n "..font:lower().."-nerd-fonts\n")
	print("%doc readme.md\n")
	print("%license LICENSE\n")
	print("/usr/share/fonts/nerd-fonts/"..font.."\n")
	if font:find("NerdFontsSymbolsOnly", 1, true) then
		print("/usr/share/fontconfig/conf.avail/10-nerd-font-symbols.conf\n")
		print("/etc/fonts/conf.d/10-nerd-font-symbols.conf\n")
	end
end
}


%changelog
* Sun Nov 15 2026 Mizuki Nguyen <acertaindrizzle@proton.me> - 3.5.1-2
- Automate fetching list of fonts
- Enable NerdFontsSymbolsOnly fontconfig fallback
- Use smaller .tar.xz archive

* Wed Jan 4 2023 madonuko <mado@fyralabs.com> - 2.2.2-1
- Initial package
