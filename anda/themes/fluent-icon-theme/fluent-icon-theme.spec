%global tag 2024-02-25

Name:           fluent-icon-theme
Version:        20240225
Release:        1%?dist
Summary:        Fluent icon theme for linux desktops

License:        GPL-3.0
URL:            https://github.com/vinceliuice/Fluent-icon-theme/
Source0:        %{url}/archive/refs/tags/%{tag}.tar.gz

BuildArch:      noarch
BuildRequires:  gtk-update-icon-cache fdupes

%description
Fluent icon theme for linux desktops.

%prep
%autosetup -n Fluent-icon-theme-%{tag}

%build

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -r -a -d %{buildroot}%{_datadir}/icons

%fdupes %buildroot%_datadir/icons/

%files
%license COPYING
%doc README.md

%{_datadir}/icons/Fluent*/

%changelog
* Thu Jun 01 2023 Lleyton Gray <lleyton@fyralabs.com> - 20230201-1
- Initial Package
