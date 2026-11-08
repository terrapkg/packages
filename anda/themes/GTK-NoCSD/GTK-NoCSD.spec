Name:           GTK-NoCSD
Version:        4.8
Release:        1%{?dist}
Summary:        An LD_PRELOAD library to disable CSD in GTK3/4, LibHandy, and LibAdwaita apps
License:        GPL-3.0-or-later
URL:            https://codeberg.org/MorsMortium/GTK-NoCSD
Source0:        %{url}/archive/%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package devel
%pkg_devel_files

%prep
%autosetup -C

%build
%make_build

%install
%make_install \
    PREFIX=%{_prefix} \
    NODOC=1 \
    NOOPT=1 \

%files
%doc README.md
%license LICENSE
%license %{_defaultlicensedir}/gtk-nocsd/LICENSE
%{_libdir}/libgtk-nocsd.so.0

%changelog
* Sun Nov 08 2026 Owen Zimmerman <owen@fyralabs.com> - 4.8-1
- Initial commit
