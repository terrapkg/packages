%global extension   tdp-control
%global uuid        %{extension}@opengamingcollective.org

Name:           gnome-shell-extension-%{extension}
Version:        0.1.0
Release:        1%{?dist}
Summary:        A GNOME shell extension for steamos-manager's performance profile, TDP limit and manual GPU clock
License:        GPL-3.0-or-later
URL:            https://github.com/OpenGamingCollective/gnome-shell-extension-tdp-control
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

Requires:       gnome-shell >= 48~
Requires:       steamos-manager
Recommends:     gnome-extensions-app

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C

%install
install -Dm644 metadata.json                                                %{buildroot}%{_gnomeextensionsdir}/metadata.json
install -Dm644 extension.js                                                 %{buildroot}%{_gnomeextensionsdir}/extension.js
install -Dm644 schemas/org.gnome.shell.extensions.tdp-control.gschema.xml   %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

%files
%license LICENSE
%doc README.md
%{_gnomeextensionsdir}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

%changelog
* Sun Sep 06 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
