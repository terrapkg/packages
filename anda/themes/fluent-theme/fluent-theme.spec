%global tag 2024-06-12

Name:           fluent-theme
Version:        20240612
Release:        1%?dist
Summary:        Fluent design theme for GNOME/GTK based desktop environments

License:        GPL-3.0
URL:            https://github.com/vinceliuice/Fluent-gtk-theme
Source0:        https://github.com/vinceliuice/Fluent-gtk-theme/archive/refs/tags/%{tag}.tar.gz

BuildArch:      noarch
BuildRequires:  sassc

Requires:       gtk-murrine-engine

%description
Fluent is a %summary.

%prep
%autosetup -n Fluent-gtk-theme-%{tag}

%build
./parse-sass.sh

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -i simple -t all -d %{buildroot}%{_datadir}/themes
./install.sh -i simple -t all --tweaks round float -d %{buildroot}%{_datadir}/themes

%files
%license COPYING
%doc README.md

%{_datadir}/themes/Fluent*/

%changelog
* Sun Jun 05 2023 Dipta Biswas <dabiswas112@gmail.com@> - 20221215-2
- Included both regular and round variant

* Thu Jun 01 2023 Lleyton Gray <lleyton@fyralabs.com> - 20221215-1
- Initial Package
