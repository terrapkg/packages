%global     debug_package %{nil}
%define     target_pkg %(t=%{name}; echo ${t#lpf-})

Name:       lpf-xone-firmware
Summary:    Linux driver for the Xbox One wireless dongle.
Version:    0.3

Release:    1%{?dist}
License:    GPLv2
URL:        https://github.com/medusalix/xone/
BuildArch:  noarch
Source0:    xone-firmware.spec.in
Source1:    eula.txt
BuildRequires:  desktop-file-utils
BuildRequires:  lpf >= 0.1
Requires:       lpf >= 0.1
Conflicts:      lpf-xow-firmware <= 0.5
Obsoletes:      lpf-xow-firmware <= 0.5

%description
Bootstrap package allowing the LPF system to build the non-redistributable
XONE firmware package

%prep
%setup -cT

%build

%install
/usr/share/lpf/scripts/lpf-setup-pkg -e %{SOURCE1} %{buildroot} %{SOURCE0}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
%lpf_check %{SOURCE0}

%post
%lpf_post

%postun
%lpf_postun
%lpf_triggerpostun

%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}

%changelog
%autochangelog

