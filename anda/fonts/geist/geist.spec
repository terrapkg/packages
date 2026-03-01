%global ver geist@1.7.0

Name:		    geist-font
Version:	    %(echo %ver | sed 's/^geist@//')
Release:	    1%?dist
URL:		    https://vercel.com/font
Source0:	    https://github.com/vercel/geist-font/archive/refs/tags/%ver.tar.gz
License:	    OFL-1.1
Summary:	    Geist is a new font family for Vercel, created by Vercel in collaboration with Basement Studio
BuildRequires:  make python3 python3.10 python3.10-devel meson cairo cairo-devel gcc
BuildArch:	    noarch
Provides:       geist = %evr
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Geist is a new font family for Vercel, created by Vercel in collaboration with Basement Studio.

Geist Sans is a sans-serif typeface designed for legibility and simplicity. It is a modern, geometric typeface
that is based on the principles of classic Swiss typography. It is designed to be used in
headlines, logos, posters, and other large display sizes.

%package        mono
Requires:       %{name} = %{evr}
Summary:        Geist Mono is a monospaced typeface that has been crafted to be the perfect partner to Geist Sans
Provides:       geist-mono = %evr
Provides:       geist-mono-fonts = %evr

%description    mono
Geist Mono is a monospaced typeface that has been crafted to be the perfect partner to Geist Sans.
It is designed to be used in code editors, diagrams, terminals, and other textbased interfaces where code is represented.

%prep
%autosetup -n %name-geist-%version

%build
%make_build

%install
mkdir -p %{buildroot}/usr/share/fonts/Geist/
mkdir -p %{buildroot}/usr/share/fonts/GeistMono/
install -Dm644 fonts/Geist/ttf/*.ttf %{buildroot}%{_datadir}/fonts/Geist/
install -Dm644 fonts/GeistMono/ttf/*.ttf %{buildroot}%{_datadir}/fonts/GeistMono/

%files
%doc readme.md AUTHORS.txt CONTRIBUTORS.txt requirements-test.txt requirements.txt OFL.txt
%license LICENSE.txt
%{_datadir}/fonts/Geist/*

%files mono
%{_datadir}/fonts/GeistMono/*

%changelog
* Wed Jun 04 2025 Owen Zimmerman <owen@fyralabs.com>
- Package Geist fonts
