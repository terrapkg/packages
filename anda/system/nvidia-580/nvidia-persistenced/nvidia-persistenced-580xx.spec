%global real_name nvidia-persistenced

Name:             %{real_name}-580xx
Version:          580.173.02
Release:          1%{?dist}
Summary:          A daemon to maintain persistent software state in the NVIDIA driver
Epoch:            3
License:          GPL-2.0-or-later
URL:              http://www.nvidia.com/object/unix.html
ExclusiveArch:    x86_64 aarch64
Source0:          https://download.nvidia.com/XFree86/%{real_name}/%{real_name}-%{version}.tar.bz2
Source1:          %{real_name}.service
Source2:          %{real_name}-sysusers.conf
BuildRequires:    gcc
BuildRequires:    libtirpc-devel
BuildRequires:    m4
# For Fedora systemd-rpm-macros would be enough:
BuildRequires:    systemd-devel
Requires:         libnvidia-cfg-580xx%{?_isa} >= %{?epoch:%{epoch}:}%{version}
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Provides:         %{real_name}-580 = %{evr}
Packager:         Terra Packaging Team <terra@fyralabs.com>

%description
The %{real_name} utility is used to enable persistent software state in the NVIDIA
driver. When persistence mode is enabled, the daemon prevents the driver from
releasing device state when the device is not in use. This can improve the
startup time of new clients in this scenario.

%prep
%autosetup -n %{real_name}-%{version}
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
install -Dpm644 %{SOURCE1} -t %{buildroot}%{_unitdir}

install -Dpm644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{real_name}.conf

%post
%systemd_post %{real_name}.service

%preun
%systemd_preun %{real_name}.service

%postun
%systemd_postun_with_restart %{real_name}.service

%files
%license COPYING
%{_mandir}/man1/%{real_name}.1.*
%{_bindir}/%{real_name}
%{_unitdir}/%{real_name}.service
%{_sysusersdir}/%{real_name}.conf

%changelog
* Fri Jul 10 2026 Gilver E. <roachy@fyralabs.com> - 3:580.173.02-2
- Update files
* Mon Apr 13 2026 Gilver E. <roachy@fyralabs.com> - 3:580.142-3
- Update spec for Terra packaging team
