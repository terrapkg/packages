%global debug_package %{nil}


Name:           adwaita++-icons
Version:        6.0
Release:        1%{?dist}
Summary:        GNOME++, a third-party icons theme, based on new GNOME 3.32's Adwaita

License:        GPL-3.0 and LGPL-3.0 and CC-BY-SA
URL:            https://github.com/Bonandry/adwaita-plus
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
%description
%summary.

%prep
%autosetup -n adwaita-plus-%{version}
%build

%install
%make_install

chmod -R -x %buildroot%_datadir/icons/*


%files
%license COPYING COPYING_CCBYSA3 COPYING_LGPL

%{_datadir}/icons/*

%changelog
* Wed Oct 19 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 6.1-1
- new package
