Name:      juliamono-fonts
Version:   0.062
Release:   1%?dist
URL:       https://juliamono.netlify.app/
Source0:   https://github.com/cormullion/juliamono/archive/refs/tags/v%{version}.tar.gz
License:   OFL-1.1
Summary:   A monospaced font with reasonable unicode support
Requires:  xorg-x11-font-utils
BuildArch: noarch
Provides:  JuliaMono-fonts
Packager:  Its-J


%description
JuliaMono is a monospaced typeface designed for programming in text editing environments that require a wide range of specialist and technical unicode characters.

%prep
%autosetup -n juliamono-%{version}

%build

%install
mkdir -p %{buildroot}%{_fontbasedir}/juliamono/
install -Dm644 *.ttf %{buildroot}%{_fontbasedir}/juliamono/

%files
%doc README.md
%license LICENSE
%{_fontbasedir}/juliamono/*.ttf

%changelog
* Fri Nov 21 2025 Its-J
- Package JuliaMono