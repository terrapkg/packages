%define version_alsa_lib  1.2.15.3
%define version_alsa_ucm  1.2.15.3
%define version_tree_ucm  0.8

Name:       alsa-ucm-cros
Summary:    ALSA Use Case Manager configuration for ChromeOS devices
Version:    %{version_alsa_ucm}
Release:    1%?dist
Epoch:      1
License:    BSD-3-Clause
URL:        https://github.com/WeirdTreeThing/alsa-ucm-conf-cros
Source0:    https://github.com/WeirdTreeThing/alsa-ucm-conf-cros/archive/refs/tags/%{version_tree_ucm}.tar.gz
Source1:    ftp://ftp.alsa-project.org/pub/lib/alsa-ucm-conf-%{version_alsa_ucm}.tar.bz2
BuildArch:  noarch
Packager:   Owen Zimmerman <owen@fyralabs.com>

Requires:   alsa-lib >= %{version_alsa_lib}
Conflicts:  alsa-ucm

%description
%summary.

%prep
%autosetup -n alsa-ucm-conf-cros-%{version_tree_ucm}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/alsa/ucm
mkdir -p %{buildroot}/%{_datadir}/alsa/ucm2

# Unpack UCMs
tar xvjf %{SOURCE1} -C %{buildroot}/%{_datadir}/alsa --strip-components=1 "*/ucm" "*/ucm2"
cp -r ucm2/ %{buildroot}/%{_datadir}/alsa/

%files
%license LICENSE
%doc README.md
%{_datadir}/alsa/ucm
%{_datadir}/alsa/ucm2

%changelog
* Tue Jan 27 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
