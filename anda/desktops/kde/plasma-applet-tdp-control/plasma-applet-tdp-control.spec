%global commit cf553bcd2ee87e651d82dcdb3f77c4abda515967
%global appid org.opengamingcollective.tdpcontrol

Name:           plasma-applet-tdp-control
Version:        1.9.3
Release:        1%{?dist}
Summary:        A Plasma applet for steamos-manager's performance profile, TDP limit and manual GPU clock
License:        GPL-3.0-or-later
URL:            https://github.com/OpenGamingCollective/plasma-applet-tdp-control
Source0:        %url/archive/%commit/plasma-applet-tdp-control-%commit.tar.gz

BuildRequires:  make
Requires:       plasma-workspace
Requires:       plasma-desktop
Requires:       steamos-manager

BuildArch:      noarch

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C

%build
%make_build plasmoid

%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/org.opengamingcollective.tdpcontrol
cp -r package/* %{buildroot}%{_datadir}/plasma/plasmoids/org.opengamingcollective.tdpcontrol/

%files
%license LICENSE
%doc README.md
%{_datadir}/plasma/plasmoids/org.opengamingcollective.tdpcontrol/*

%changelog
* Sun Sep 06 2026 Owen Zimmerman <owen@fyralabs.com> - VERSION-RELEASE
- Initial commit
