%global tag 2022-12-15

Name:           fluent-theme
Version:        20221215
Release:        1%{?dist}
Summary:        Fluent is a Fluent design theme for GNOME/GTK based desktop environments.

License:        GPLv3
URL:            https://github.com/vinceliuice/Fluent-gtk-theme
Source0:        https://github.com/vinceliuice/Fluent-gtk-theme/archive/refs/tags/%{tag}.tar.gz

BuildArch:      noarch
BuildRequires:  sassc

Requires:       gtk-murrine-engine

%description
Fluent is a Fluent design theme for GNOME/GTK based desktop environments.

%prep
%autosetup -n Fluent-gtk-theme-%{tag}

%build
./parse-sass.sh

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh --tweaks round -d %{buildroot}%{_datadir}/themes

%files
%license COPYING
%doc README.md

%{_datadir}/themes/Fluent*/

%changelog
* Thu Jun 01 2023 Lleyton Gray <lleyton@fyralabs.com> - 20221215-1
- Initial Package
