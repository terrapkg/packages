%global forgeurl https://gitlab.com/ubports/development/core/lomiri-schemas
%global commit 814c0b16b3753fef918bfe624710cb4809a690fa
%forgemeta

Name:       lomiri-schemas
Version:    0.1.5
Release:    1%?dist
Summary:    Configuration schemas for lomiri
License:    LGPL-2.0-or-later
URL:        https://gitlab.com/ubports/development/core/lomiri-schemas
Source0:    %url/-/archive/%commit/lomiri-schemas-%commit.tar.gz
Source1:    com.lomiri.Shell.gschema.xml
BuildArch:  noarch

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: glib2-devel
BuildRequires: gettext
BuildRequires: intltool

%description
Configuration schemas for lomiri desktop enviroment.

%prep
%autosetup -n %{name}-%commit

%build
%cmake -DCMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT=true
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_datadir}/glib-2.0/schemas/%{SOURCE1}
cp %{SOURCE1} %{buildroot}%{_datadir}/glib-2.0/schemas/

%files
%{_datadir}/accountsservice/interfaces/*.xml
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pkgconfig/lomiri-schemas.pc
%{_datadir}/polkit-1/actions/com.lomiri.AccountsService.policy
%{_sharedstatedir}/polkit-1/localauthority/10-vendor.d/50-com.lomiri.AccountsService.pkla

%changelog
%autochangelog
