Name:           libssc
Version:        0.4.4
Release:        1%{?dist}
Summary:        Library to access sensors managed by the Qualcomm Sensor Core

License:        GPL-3.0-or-later
URL:            https://codeberg.org/DylanVanAssche/libssc
Source0:        %{url}/archive/v%{version}.tar.gz

Patch1:         0001-meson-drop-the-mocking-and-tests-subdirs.patch

BuildRequires:  gcc
BuildRequires:  meson >= 1.4.0
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(qmi-glib) >= 1.33.4
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  protobuf-compiler
BuildRequires:  /usr/bin/protoc-gen-c

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Qualcomm SoCs offload sensors to a dedicated Sensor Low Power Island (SLPI)
DSP; direct access is blocked by the hypervisor, so the only way to reach
these sensors is by talking QMI to the DSP over QRTR. libssc does that and
exposes proximity, light, accelerometer, magnetometer, gyroscope, and
rotation-vector sensors as a GLib-based library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{evr}

%description    devel
Headers and pkgconfig file for developing applications against %{name}.

%prep
%autosetup -n %{name} -p1

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/ssccli
%{_libdir}/libssc.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libssc.so
%{_libdir}/pkgconfig/libssc.pc

%changelog
* Tue Sep 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
