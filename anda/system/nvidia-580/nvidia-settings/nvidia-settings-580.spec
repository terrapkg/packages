%global real_name nvidia-settings

Name:           %{real_name}-580
Version:        580.126.09
Release:        1%?dist
Summary:        Configure the NVIDIA graphics driver
Epoch:          3
License:        GPLv2+
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  x86_64 aarch64

Source0:        https://download.nvidia.com/XFree86/%{real_name}/%{real_name}-%{version}.tar.bz2
Source1:        %{real_name}-load.desktop
Source2:        %{real_name}.appdata.xml
Patch0:         %{real_name}-desktop.patch
Patch1:         %{real_name}-lib-permissions.patch
Patch2:         %{real_name}-link-order.patch
Patch3:         %{real_name}-libXNVCtrl.patch
Patch4:         %{real_name}-ld-dep-remove.patch

BuildRequires:  desktop-file-utils
BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  jansson-devel
BuildRequires:  libappstream-glib
BuildRequires:  libvdpau-devel >= 1.0
BuildRequires:  libXxf86vm-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXv-devel
BuildRequires:  m4
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  vulkan-headers

Requires:       nvidia-libXNVCtrl-580%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       nvidia-driver-580%{?_isa} = %{?epoch}:%{version}
# Loaded at runtime
Requires:       libvdpau%{?_isa} >= 0.9

%description
The %{real_name} utility is a tool for configuring the NVIDIA graphics
driver. It operates by communicating with the NVIDIA X driver, querying and
updating state as appropriate.

This communication is done with the NV-CONTROL X extension.

%package -n nvidia-libXNVCtrl-580
Summary:        Library providing the NV-CONTROL API
Obsoletes:      libXNVCtrl < %{?epoch}:%{version}-%{release}
Provides:       libXNVCtrl-580 = %{?epoch}:%{version}-%{release}

%description -n nvidia-libXNVCtrl-580
This library provides the NV-CONTROL API for communicating with the proprietary
NVidia xorg driver. It is required for proper operation of the %{real_name} utility.

%package -n nvidia-libXNVCtrl-580-devel
Summary:        Development files for libXNVCtrl
Requires:       nvidia-libXNVCtrl-580 = %{?epoch}:%{version}-%{release}
Requires:       libX11-devel

%description -n nvidia-libXNVCtrl-580-devel
This devel package contains libraries and header files for
developing applications that use the NV-CONTROL API.

%prep
%autosetup -p1 -n %{real_name}-%{version}

# Remove bundled jansson
rm -fr src/jansson

# Remove additional CFLAGS added when enabling DEBUG
sed -i '/+= -O0 -g/d' utils.mk src/libXNVCtrl/utils.mk

# Change all occurrences of destinations in each utils.mk.
sed -i -e 's|$(PREFIX)/lib|$(PREFIX)/%{_lib}|g' utils.mk src/libXNVCtrl/utils.mk

%build
export CFLAGS="%{optflags} -fPIC"
export LDFLAGS="%{?__global_ldflags}"
make \
    DEBUG=1 \
    NV_USE_BUNDLED_LIBJANSSON=0 \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    XNVCTRL_LDFLAGS="-L%{_libdir}"

%install
# Install libXNVCtrl headers
mkdir -p %{buildroot}%{_includedir}/NVCtrl
cp -af src/libXNVCtrl/*.h %{buildroot}%{_includedir}/NVCtrl/

# Install main program
%make_install \
    DEBUG=1 \
    NV_USE_BUNDLED_LIBJANSSON=0 \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix}

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
desktop-file-install --dir %{buildroot}%{_datadir}/applications/ doc/%{real_name}.desktop
cp doc/%{real_name}.png %{buildroot}%{_datadir}/pixmaps/

# Install autostart file to load settings at login
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/%{real_name}-load.desktop

# install AppData and add modalias provides
mkdir -p %{buildroot}%{_metainfodir}/
install -p -m 0644 %{SOURCE2} %{buildroot}%{_metainfodir}/

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{real_name}.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{real_name}-load.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{real_name}.appdata.xml

%files
%{_bindir}/%{real_name}
%{_metainfodir}/%{real_name}.appdata.xml
%{_datadir}/applications/%{real_name}.desktop
%{_datadir}/pixmaps/%{real_name}.png
%{_libdir}/libnvidia-gtk3.so.%{version}
%{_libdir}/libnvidia-wayland-client.so.%{version}
%{_mandir}/man1/%{real_name}.*
%{_sysconfdir}/xdg/autostart/%{real_name}-load.desktop

%files -n nvidia-libXNVCtrl-580
%license COPYING
%{_libdir}/libXNVCtrl.so.*

%files -n nvidia-libXNVCtrl-580-devel
%doc doc/NV-CONTROL-API.txt doc/FRAMELOCK.txt
%{_includedir}/NVCtrl
%{_libdir}/libXNVCtrl.so

%changelog
%autochangelog
