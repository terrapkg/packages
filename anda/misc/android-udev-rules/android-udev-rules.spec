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

%description
Android udev rules list aimed to be the most comprehensive on the net.
Based on the official Android Studio documentation as well as suggestions from
the Archlinux and Github Communities.

%prep
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%install
mkdir -p %{buildroot}/etc/udev/rules.d/.
install -m 644 51-android.rules %{buildroot}/etc/udev/rules.d/.
mkdir -p %{buildroot}/usr/lib/sysusers.d/.
install -m 644 android-udev.conf %{buildroot}/usr/lib/sysusers.d/.

%files
%_udevrulesdir/51-android.rules
%_sysusersdir/android-udev.conf
%license LICENSE
%doc README.md
