%global tag 2025-02-26

Name:           fluent-icon-theme
Version:        20250226
Release:        2%?dist
Summary:        Fluent icon theme for linux desktops

License:        GPL-3.0
URL:            https://github.com/vinceliuice/Fluent-icon-theme/
Source0:        %{url}/archive/refs/tags/%{tag}.tar.gz

BuildArch:      noarch
BuildRequires:  gtk-update-icon-cache fdupes
Conflicts:      %name

%description
Fluent icon theme for linux desktops.

%prep
%autosetup -n Fluent-icon-theme-%{tag}

%build

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -a -d %{buildroot}%{_datadir}/icons

%fdupes %buildroot%_datadir/icons/

%files
%license COPYING
%doc README.md

%{_datadir}/icons/Fluent*/

%changelog
* Thu Jun 01 2023 Lleyton Gray <lleyton@fyralabs.com> - 20230201-1
- Initial Package
