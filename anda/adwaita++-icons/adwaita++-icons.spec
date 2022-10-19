%global debug_package %{nil}


Name:           adwaita++-icons
Version:        6.1
Release:        1%{?dist}
Summary:         GNOME++, a third-party icons theme, based on new GNOME 3.32's Adwaita

License:        GPLv3 and LGPLv3 and CC-BY-SA
URL:            https://github.com/Bonandry/adwaita-plus
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
%description


%prep
%autosetup -n adwaita-plus-%{version}
%build

%install
%make_install



%files
%license COPYING COPYING_CCBYSA3 COPYING_LGPL

%{_datadir}/icons/*

%changelog
* Wed Oct 19 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- new package
