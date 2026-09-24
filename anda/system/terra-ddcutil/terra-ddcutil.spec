%bcond_without build_lib

%global packagename ddcutil

Name:       terra-ddcutil
Version:    3.0.2
Release:    1%{?dist}
Summary:    Query and update monitor settings
Packager:   Kyle Gospodnetich <me@kylegospodneti.ch>

License:    GPL-2.0-or-later
URL:        http://www.ddcutil.com
Source0:    https://github.com/rockowitz/%{packagename}/archive/v%{version}/%{packagename}-%{version}.tar.gz

# Excluding arch s390/s390x due to i2c-tools does so
ExcludeArch:    s390 s390x

Provides:       %{packagename} = %{evr}
Conflicts:      %{packagename}

BuildRequires:      automake
BuildRequires:      autoconf
BuildRequires:      libtool
BuildRequires:      gcc
BuildRequires:      make
BuildRequires:      pkgconfig(glib-2.0)   >= 2.40
BuildRequires:      pkgconfig(libusb-1.0) >= 1.0.15
BuildRequires:      pkgconfig(systemd)
BuildRequires:      pkgconfig(libudev)
BuildRequires:      pkgconfig(x11)
BuildRequires:      pkgconfig(xrandr)
BuildRequires:      pkgconfig(xext)
BuildRequires:      pkgconfig(libdrm) >= 2.4.67
BuildRequires:      pkgconfig(libkmod)
BuildRequires:      pkgconfig(jansson) >= 2.0
BuildRequires:      pkgconfig(libacl)
BuildRequires:      pkgconfig(dbus-1)
%if %{with build_lib}
BuildRequires:      pkgconfig(zlib)
%endif

Requires:   hwdata
Requires:   i2c-tools

# file that may be used at runtime
Recommends: /usr/bin/lsusb
Recommends: /usr/bin/modprobe
Recommends: pkg-config
Recommends: /usr/bin/lscpu
Recommends: /usr/bin/lsb_release
Recommends: xrandr

%description
Query and change monitor settings

ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.  In general, anything that can be controlled using a monitor's
on-screen display can be controlled by this program.  Examples include
changing a monitor's input source and adjusting its brightness.

# libddcutil can be installed separately
%if %{with build_lib}
%package -n libddcutil
Summary:        Shared library to query and update monitor settings
Provides:       libddcutil = %{evr}
Conflicts:      libddcutil

%description -n libddcutil
Shared library version of ddcutil, exposing a C API.

%package -n libddcutil-devel
Summary:        Development files for libddcutil
# FindDDCUtils.cmake has BSD-3-Clause license header
License:        GPL-2.0-or-later AND BSD-3-Clause
Provides:       libddcutil-devel = %{evr}
Conflicts:      libddcutil-devel
Requires:       libddcutil%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem%{?_isa}

%description -n libddcutil-devel
Development files for libddcutil
%endif

%prep
%setup -q -n %{packagename}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
%if %{with build_lib}
    --enable-lib=yes
%else
    --enable-lib=no
%endif
%make_build

%install
%make_install

%files
%doc AUTHORS NEWS.md README.md CHANGELOG.md
%license COPYING
%{_bindir}/%{packagename}
%{_datadir}/%{packagename}
%{_mandir}/man1/%{packagename}.1.*
%{_udevrulesdir}/60-ddcutil-i2c.rules
%{_modulesloaddir}/ddcutil.conf

%if %{with build_lib}
%files -n libddcutil
%doc AUTHORS NEWS.md README.md CHANGELOG.md
%license COPYING
%{_libdir}/lib%{packagename}.so.5*

%files -n libddcutil-devel
%{_libdir}/lib%{packagename}.so
%{_includedir}/%{packagename}*.h
%{_libdir}/cmake/%{packagename}
%{_libdir}/pkgconfig/%{packagename}.pc
%endif

%changelog
* Thu Sep 24 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 3.0.2-1
- Initial release of terra-ddcutil
