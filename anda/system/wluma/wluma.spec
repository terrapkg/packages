Name:           wluma
Version:        4.10.0
Release:        3%?dist
Summary:        Automatic brightness adjustment based on screen contents and ALS
URL:            https://github.com/max-baz/wluma
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
License:        ISC
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold v4l-utils libv4l-devel rust-libudev-devel vulkan-loader-devel dbus-devel clang systemd-rpm-macros
Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies
install -Dm 644 %{name}.service %{buildroot}%{_userunitdir}/%{name}.service
install -Dm 644 90-%{name}-backlight.rules %{buildroot}%{_udevrulesdir}/90-%{name}-backlight.rules
install -Dm 644 config.toml %{buildroot}%{_datadir}/%{name}/config.toml

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/wluma
%{_userunitdir}/%{name}.service
%{_udevrulesdir}/90-%{name}-backlight.rules
%{_datadir}/%{name}/config.toml

%changelog
* Tue Apr 14 2026 Its-J <jonah@fyralabs.com>
- Add email to my previous contributor attributions

* Sat Nov 29 2025 metcya <metcya@gmail.com>
- Package systemd service, example config, and udev rules

* Fri Nov 28 2025 Its-J <jonah@fyralabs.com>
- Package wluma
