%global _desc Automatic CPU speed & power optimizer for Linux.

Name:			python-auto-cpufreq
Version:		3.0.0
Release:		1%?dist
Summary:		Automatic CPU speed & power optimizer for Linux
License:		LGPL-3.0-or-later
URL:			https://foolcontrol.org/?p=4603
Source0:		https://github.com/AdnanHodzic/auto-cpufreq/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-installer
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-poetry-core
BuildRequires:  python3-poetry-dynamic-versioning
BuildArch:      noarch

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-auto-cpufreq
Summary:        %{summary}
%{?python_provide:%python_provide python3-auto-cpufreq}

%description -n python3-auto-cpufreq
%_desc

%prep
%git_clone https://github.com/AdnanHodzic/auto-cpufreq.git %{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files auto_cpufreq
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions/
install -Dm644 scripts/org.auto-cpufreq.pkexec.policy %{buildroot}%{_datadir}/polkit-1/actions/
install -Dm644 images/icon.png %{buildroot}%{_hicolordir}/512x512/apps/auto-cpufreq.png
install -Dm644 images/icon.png %{buildroot}%{_datadir}/%{name}/icon.png

mkdir -p %{buildroot}%{_datadir}/%{name}/scripts/
mkdir -p %{buildroot}/opt/auto-cpufreq/
mkdir -p %{buildroot}%{_appsdir}/
mkdir -p %{buildroot}%{_unitdir}/

install -Dm755 scripts/auto-cpufreq-install.sh %{buildroot}%{_datadir}/%{name}/scripts/
install -Dm755 scripts/auto-cpufreq-remove.sh %{buildroot}%{_datadir}/%{name}/scripts/
install -Dm644 scripts/auto-cpufreq.service %{buildroot}%{_unitdir}/auto-cpufreq.service
install -Dm755 scripts/cpufreqctl.sh %{buildroot}%{_datadir}/%{name}/scripts/
install -Dm644 scripts/style.css %{buildroot}%{_datadir}/%{name}/scripts/
install -Dm644 scripts/auto-cpufreq-gtk.desktop %{buildroot}%{_appsdir}/

%post
%systemd_post auto-cpufreq.service

%preun
%systemd_preun auto-cpufreq.service

%postun
%systemd_postun_with_restart auto-cpufreq.service

%files -n python3-auto-cpufreq -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/auto-cpufreq
%{_bindir}/auto-cpufreq-gtk
%{_datadir}/polkit-1/actions/org.auto-cpufreq.pkexec.policy
%{_hicolordir}/512x512/apps/auto-cpufreq.png
%{_datadir}/%{name}/icon.png
%{_unitdir}/auto-cpufreq.service
%{_datadir}/%{name}/scripts/
%{_appsdir}/auto-cpufreq-gtk.desktop

%changelog
* Sun Apr 05 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
