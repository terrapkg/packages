Name:           nvidia-persistenced
Version:        590.48.01
Release:        2%?dist
Summary:        A daemon to maintain persistent software state in the NVIDIA driver
Epoch:          3
License:        GPL-2.0-or-later
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  x86_64 aarch64

Source0:        https://download.nvidia.com/XFree86/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.service
Source2:        %{name}-sysusers.conf

BuildRequires:    gcc
BuildRequires:    libtirpc-devel
BuildRequires:    m4
BuildRequires:    sed
BuildRequires:    systemd-rpm-macros

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Requires:         libnvidia-cfg%{?_isa} >= %{?epoch:%{epoch}:}%{version}

%description
The %{name} utility is used to enable persistent software state in the NVIDIA
driver. When persistence mode is enabled, the daemon prevents the driver from
releasing device state when the device is not in use. This can improve the
startup time of new clients in this scenario.

%prep
%autosetup
# Remove additional CFLAGS added when enabling DEBUG
sed -i -e '/+= -O0 -g/d' utils.mk

%build
export CFLAGS="%{optflags} -I%{_includedir}/tirpc"
make %{?_smp_mflags} \
    DEBUG=1 \
    LIBS="-ldl -ltirpc" \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

%install
%make_install \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

# Systemd unit files
install -Dpm644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# Systemd user
install -Dpm644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf

%changelog
%autochangelog
