%global real_name nvidia-xconfig

Name:           %{real_name}-580xx
Version:        580.159.03
Release:        1%{?dist}
Summary:        NVIDIA X configuration file editor
Epoch:          3
License:        GPL-2.0-or-later
URL:            http://www.nvidia.com/object/unix.html
Source0:        https://download.nvidia.com/XFree86/%{real_name}/%{real_name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  libpciaccess-devel
BuildRequires:  m4
Requires:       libnvidia-cfg-580xx%{?_isa} >= %{?epoch:%{epoch}:}%{version}
Requires:       xorg-x11-nvidia-580xx%{?_isa} >= %{?epoch:%{epoch}:}%{version}
Provides:       %{real_name}-580 = %{evr}
ExclusiveArch:  x86_64 aarch64
Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
%{real_name} is a command line tool intended to provide basic control over
configuration options available in the NVIDIA X driver.

%prep
%autosetup -p1 -n %{real_name}-%{version}
# Remove additional CFLAGS added when enabling DEBUG
sed -i '/+= -O0 -g/d' utils.mk

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags} \
    DEBUG=1 \
    MANPAGE_GZIP=0 \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

%install
%make_install \
    MANPAGE_GZIP=0 \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

%files
%license COPYING
%{_bindir}/%{real_name}
%{_mandir}/man1/%{real_name}.1*

%changelog
* Mon Apr 13 2026 Gilver E. <roachy@fyralabs.com> - 3:580.142-3
- Update spec for Terra packaging team
