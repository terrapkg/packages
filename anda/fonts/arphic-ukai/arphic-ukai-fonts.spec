Name:		arphic-ukai-fonts
Version:	0.2.20080216.2
Release:	2%?dist
URL:		https://www.freedesktop.org/wiki/Software/CJKUnifonts
Source0:	https://deb.debian.org/debian/pool/main/f/fonts-arphic-ukai/fonts-arphic-ukai_%{version}.orig.tar.bz2
License:	Arphic-1999
Summary:	CJK Unicode font Kaiti style
BuildArch:	noarch

%description
%{summary}.


%prep
%setup -q -n fonts-arphic-ukai-%{version}

%build

%install
install -D -m644 ukai.ttc %{buildroot}/%{_datadir}/fonts/arphic-ukai/ukai.ttc


%files
%doc README
%license license/english/ARPHICPL.TXT
/%{_datadir}/fonts/arphic-ukai/ukai.ttc

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 0.2.20080216.2-1
- Initial package
