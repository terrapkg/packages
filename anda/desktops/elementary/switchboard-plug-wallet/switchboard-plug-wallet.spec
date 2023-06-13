%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-wallet

%global plug_type personal
%global plug_name wallet
%global plug_rdnn io.elementary.switchboard.wallet

Name:           switchboard-plug-wallet
Summary:        Switchboard Wallet Plug
Version:        bfe73df
Release:        1%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%name
Source0:        %url/archive/%version/%srcname-%version.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  gtk3-devel
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  switchboard-devel

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
Manage Payment Methods and related settings.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so


%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - bfe73dfb95d9b46a0a34e0db35a178233c8552b0-1
- Initial package.
