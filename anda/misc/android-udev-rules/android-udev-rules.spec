#? https://github.com/M0Rf30/android-udev-rules/blob/main/rpm/android-udev-rules.spec
Name:           android-udev-rules
Version:        20250314
Release:        1%{?dist}
Summary:        Udev rules to connect Android devices to your linux box
License:        GPL-3.0-or-later
URL:            https://github.com/M0Rf30/android-udev-rules
Source0:        https://raw.githubusercontent.com/M0Rf30/android-udev-rules/%version/51-android.rules
Source1:        https://raw.githubusercontent.com/M0Rf30/android-udev-rules/%version/README.md
Source2:        https://raw.githubusercontent.com/M0Rf30/android-udev-rules/%version/LICENSE
Source3:        https://raw.githubusercontent.com/M0Rf30/android-udev-rules/%version/android-udev.conf
BuildArch:      noarch
BuildRequires:  rpm_macro(_udevrulesdir)
BuildRequires:  rpm_macro(udev_rules_update)
Requires:       systemd-udev

%description
Android udev rules list aimed to be the most comprehensive on the net.
Based on the official Android Studio documentation as well as suggestions from
the Archlinux and Github Communities.

%prep
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%install
install -Dm644 51-android.rules -t %buildroot%_udevrulesdir
install -Dm644 android-udev.conf -t %buildroot%_sysusersdir

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%_udevrulesdir/51-android.rules
%_sysusersdir/android-udev.conf
%license LICENSE
%doc README.md
