Name:           wluma
Version:        5.0.2
Release:        2%{?dist}
Summary:        Automatic brightness adjustment based on screen contents and ALS
URL:            https://github.com/max-baz/wluma
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
SourceLicense:  ISC
License:        %{SourceLicense} AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT OR Zlib) AND MIT AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (BSD-2-Clause OR MIT OR Apache-2.0) AND (Unlicense OR MIT)

BuildRequires:  cargo-rpm-macros
BuildRequires:  v4l-utils
BuildRequires:  libv4l-devel
BuildRequires:  rust-libudev-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  dbus-devel
BuildRequires:  clang
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(libpipewire-0.3)
Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
%{cargo_license_online -a} > LICENSE.dependencies
install -Dm 755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 644 %{name}.service %{buildroot}%{_userunitdir}/%{name}.service
install -Dm 644 90-%{name}-backlight.rules %{buildroot}%{_udevrulesdir}/90-%{name}-backlight.rules

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

%changelog
* Wed Sep 23 2026 Its-J <jonah@fyralabs.com> - 5.0.2-2
- Fix licences, build deps, and building twice

* Sun Jul 19 2026 Olivia <git@olivia.sh> - 4.11.1-2
- Update packager

* Tue Apr 14 2026 Its-J <jonah@fyralabs.com>
- Add email to my previous contributor attributions

* Sat Nov 29 2025 Olivia <git@olivia.sh>
- Package systemd service, example config, and udev rules

* Fri Nov 28 2025 Its-J <jonah@fyralabs.com>
- Package wluma
