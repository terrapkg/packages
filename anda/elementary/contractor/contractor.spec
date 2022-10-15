Name:           contractor
Version:        0.3.5
Release:        %autorelease
Summary:        Desktop-wide extension service

License:        GPL-3.0-or-later
URL:            https://github.com/elementary/contractor
Source0:        %{url}/archive/%{version}/contractor-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  meson

# data/meson.build
BuildRequires:  pkgconfig(dbus-1)
# src/meson.build
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)

# For %%{_datadir}/dbus-1/services/ directory:
Requires:       dbus-common

%description
An extension service that allows apps to use the exposed functionality
of registered apps. This way, apps don't have to have the functions hard
coded into them.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

# Create the the directory where other programs put their contracts
mkdir -p %{buildroot}/%{_datadir}/contractor


%files
%doc README.md
%license COPYING

%{_bindir}/contractor

%dir %{_datadir}/contractor
%{_datadir}/dbus-1/services/org.elementary.contractor.service


%changelog
%autochangelog
