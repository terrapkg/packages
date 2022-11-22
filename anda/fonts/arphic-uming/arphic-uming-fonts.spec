Name:       arphic-uming-fonts
Version:    0.2.20080216.2
Release:    %autorelease
URL:        https://www.freedesktop.org/wiki/Software/CJKUnifonts
Source0:	https://deb.debian.org/debian/pool/main/f/fonts-arphic-uming/fonts-arphic-uming_%{version}.orig.tar.bz2
License:    custom
Summary:    CJK Unicode font Ming style
BuildArch: noarch

%description
%{summary}.


%prep
%setup -n ttf-arphic-uming-%{version}


%install
install -D -m644 uming.ttc %{buildroot}/%{_datadir}/fonts/arphic-uming/uming.ttc


%files
%doc README
%license license/english/ARPHICPL.TXT
%defattr(-,root,root,0755)
/%{_datadir}/fonts/arphic-uming/uming.ttc

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.004
- Initial package
