Name:     budgie-indicator-applet
Version:  0.7.2
Release:  1%{?dist}

License:  GPL-3.0
Summary:  AppIndicator applet for Budgie
URL:      https://ubuntubudgie.org/

Source0:  https://github.com/UbuntuBudgie/budgie-indicator-applet/releases/download/v%{version}/budgie-indicator-applet-%{version}.tar.xz

BuildRequires: pkgconfig(budgie-1.0)
BuildRequires: pkgconfig(ayatana-indicator3-0.4)

%description
AppIndicator applet for Budgie

%prep
%autosetup

%build
autoreconf --force --install --symlink --warnings=all
%configure
%make_build

%install
%make_install

%files
%{_libdir}/budgie-desktop/plugins/appindicator-applet

