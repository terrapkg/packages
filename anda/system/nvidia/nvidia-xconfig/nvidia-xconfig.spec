Name:           nvidia-xconfig
Version:        590.48.01
Release:        2%?dist
Summary:        NVIDIA X configuration file editor
Epoch:          3
License:        GPL-2.0-or-later
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  x86_64 aarch64

Source0:        https://download.nvidia.com/XFree86/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  libpciaccess-devel
BuildRequires:  m4
BuildRequires:  sed

Requires:       libnvidia-cfg%{?_isa} >= %{?epoch:%{epoch}:}%{version}
Requires:       xorg-x11-nvidia%{?_isa} >= %{?epoch:%{epoch}:}%{version}

%description
%{name} is a command line tool intended to provide basic control over
configuration options available in the NVIDIA X driver.

%prep
%autosetup -p1
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
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
