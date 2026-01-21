%dnl %define debug_package %{nil}

%global goipath github.com/nwg-piotr/nwg-look
Version:        1.0.6

%gometa -f

Name:           nwg-look
Release:        1%?dist
Summary:        GTK3 settings editor adapted to work in the wlroots environment

License:        MIT
URL:            https://github.com/nwg-piotr/nwg-look
Source0:        https://github.com/nwg-piotr/nwg-look/archive/refs/tags/v%version.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
Requires:       glibc

%description
%{summary}.

%gopkg

%prep
%autosetup -n %{name}-%{version}

%build
%make_build
%make_build build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_appsdir}/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.svg

%changelog
* Fri Dec 05 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
