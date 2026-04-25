%global metainfo_commit baf65ee3b0236d447e250294c5773f9411d85cfa

Name:			proton-vpn-gtk-app
Version:		4.15.3
Release:		1%{?dist}
Summary:		Official ProtonVPN Linux app
License:		GPL-3.0-only
URL:			https://protonvpn.com/download-linux
Source0:		https://github.com/ProtonVPN/proton-vpn-gtk-app/archive/refs/tags/v%version.tar.gz
# So cursed but makes our lives easier
Source1:        https://github.com/flathub/com.protonvpn.www/archive/%{metainfo_commit}/com.protonvpn.www-%{metainfo_commit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-wheel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-gobject
BuildRequires:  python3-dbus
BuildRequires:  python3-packaging
BuildRequires:  gtk3
BuildRequires:  libnotify
BuildRequires:  python3-proton-vpn-api-core
BuildRequires:  librsvg2

Requires:       gtk3
Requires:       libnotify
Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-packaging
Requires:       python3-proton-vpn-api-core
Requires:       python3-proton-core >= 0.7.0
Requires:       librsvg2

Provides:       protonvpn
Provides:       proton-vpn

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
The Proton VPN GTK app is intended for every Proton VPN service user,
it provides full access to all functionalities available to authenticated users,
with the user signup process handled on the website.

%prep
%autosetup -n %{name}-%{version}
tar -xvf %{SOURCE1}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files proton
install -Dm644 rpmbuild/SOURCES/proton-vpn-logo.svg %{buildroot}%{_scalableiconsdir}/proton-vpn-logo.svg
install -Dm644 com.protonvpn.www-%{metainfo_commit}/com.protonvpn.www.metainfo.xml %{buildroot}%{_metainfodir}/com.protonvpn.www.metainfo.xml
install -Dm644 rpmbuild/SOURCES/proton.vpn.app.gtk.desktop %{buildroot}%{_appsdir}/proton.vpn.app.gtk.desktop

# We pull in a metainfo file that often changes upstream, that calls the .desktop file what we are symlinking it to.
# If we install the .desktop file with the new name, the icon does not show properly on KDE Plasma.
%{__ln_s} -f %{_appsdir}/proton.vpn.app.gtk.desktop %{buildroot}%{_appsdir}/com.protonvpn.www.desktop

%files -f %{pyproject_files}
%doc README.md CONTRIBUTING.md CODEOWNERS
%license LICENSE COPYING.md
%{_bindir}/protonvpn-app
%{_appsdir}/proton.vpn.app.gtk.desktop
%{_appsdir}/com.protonvpn.www.desktop
%{_scalableiconsdir}/proton-vpn-logo.svg
%{_metainfodir}/com.protonvpn.www.metainfo.xml

%changelog
* Wed Mar 25 2026 Owen Zimmerman <owen@fyralabs.com>
- Fix metainfo and .desktop file

* Sat Jan 17 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
