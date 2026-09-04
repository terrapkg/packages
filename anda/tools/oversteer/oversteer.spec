%define debug_package %{nil}

Name:           oversteer
Version:        0.8.3
Release:        1%{?dist}
Summary:        Steering Wheel Manager for GNU/Linux
Packager:       Jan200101 <sentrycraft123@gmail.com>

License:        GPL-3.0-only
URL:            https://github.com/berarma/oversteer
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-pyudev
BuildRequires:  python3-pyxdg
BuildRequires:  python3-evdev
BuildRequires:  python3-matplotlib
BuildRequires:  python3-scipy
BuildRequires:  python3-numpy
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros

# None of these are detected as required dependencies
Requires:  python3-gobject
Requires:  python3-pyudev
Requires:  python3-pyxdg
Requires:  python3-evdev
Requires:  python3-matplotlib
Requires:  python3-scipy
Requires:  python3-numpy

%description
Oversteer manages steering wheels on Linux using the
features provided by the loaded modules.
It doesn't provide hardware support, you'll still need a
driver module that enables the hardware on Linux.

%prep
%autosetup

%conf
%meson \
    -Dpython="%{python3}" \
    -Dudev_rules_dir="%{_udevrulesdir}"

%build
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%{_bindir}/oversteer
%{_scalableiconsdir}/io.github.berarma.Oversteer.svg
%{_appsdir}/io.github.berarma.Oversteer.desktop
%{_metainfodir}/io.github.berarma.Oversteer.appdata.xml
%{_udevrulesdir}/99-thrustmaster-wheel-perms.rules
%{_udevrulesdir}/99-logitech-wheel-perms.rules
%{_udevrulesdir}/99-fanatec-wheel-perms.rules
%{python3_sitelib}/oversteer/main.css
%{python3_sitelib}/oversteer/main.ui
%pycached %{python3_sitelib}/oversteer/*.py

%changelog
* Sun Jul 05 2026 Jan200101 <sentrycraft123@gmail.com> - 1.0.18-1
- Package oversteer
