%global debug_package %{nil}
%global prjname zenmonitor3
%global commit ecd9bf31dd532ac53f305e10378e637cd1cc4bbe
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: %{prjname}
Version: 2.0.0^2.git%{shortcommit}
Release: 2%{?dist}
Summary: GUI monitoring software for AMD Zen-based CPUs.
Packager: Cappy Ishihara <cappy@cappuchino.xyz>
License: MIT
URL: https://gitlab.com/shdwchn10/%{prjname}
Source0: https://gitlab.com/shdwchn10/%{prjname}/-/archive/%{commit}/%{prjname}-%{commit}.tar.gz
Source1: modules-load.conf

BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd-rpm-macros
BuildRequires: sed
BuildRequires: gtk3-devel

%description
Zenmonitor3 is GTK3 monitoring software for AMD Zen-based CPUs.

It can monitor these values:
- CPU Temperature
- CPU Core (SVI2) Voltage, Current and Power
- SOC (SVI2) Voltage, Current and Power
- Package and Core Power (RAPL)
- Core Frequency (from OS)


%package cli
Summary: CLI monitoring software for AMD Zen-based CPUs.
BuildRequires: ncurses-devel

%description cli
Zenmonitor3 is ncurses monitoring software for AMD Zen-based CPUs.

It can monitor these values:
- CPU Temperature
- CPU Core (SVI2) Voltage, Current and Power
- SOC (SVI2) Voltage, Current and Power
- Package and Core Power (RAPL)
- Core Frequency (from OS)


%prep
%setup -q -n %{prjname}-%{commit}


%build
make %{?_smp_mflags} DESTDIR=%{buildroot} build build-cli


%install
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} install install-cli

mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions/

sed -e "s|@APP_EXEC@|%{_bindir}/zenmonitor|" data/zenmonitor.desktop.in > \
    %{buildroot}%{_datadir}/applications/zenmonitor.desktop
sed -e "s|@APP_EXEC@|%{_bindir}/zenmonitor|" data/zenmonitor-root.desktop.in > \
    %{buildroot}%{_prefix}/share/applications/zenmonitor-root.desktop
sed -e "s|@APP_EXEC@|%{_bindir}/zenmonitor|" data/org.pkexec.zenmonitor.policy.in > \
    %{buildroot}%{_datadir}/polkit-1/actions/org.pkexec.zenmonitor.policy

install -Dpm 0644 %{S:1} %{buildroot}%{_modulesloaddir}/%{name}.conf


%files
%{_bindir}/zenmonitor
%{_datadir}/applications/zenmonitor.desktop
%{_datadir}/applications/zenmonitor-root.desktop
%{_datadir}/polkit-1/actions/org.pkexec.zenmonitor.policy
%{_modulesloaddir}/%{name}.conf


%files cli
%{_bindir}/zenmonitor-cli


%changelog
* Thu Dec 19 2024 Andrey Brusnik <dev@shdwchn.io> - 2.0.0^2.gitecd9bf3-2
- fix: Update broken link to mirror

* Tue Nov 07 2023 Andrey Brusnik <dev@shdwchn.io> - 2.0.0^1.gita09f0b25d3-1
- Initial package