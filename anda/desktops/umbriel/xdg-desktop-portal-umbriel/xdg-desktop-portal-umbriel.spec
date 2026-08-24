%global debug_package   %{nil}

%global commit          515c9f70f13ba4b4b9e19930b3e899c4ac8a50a4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20260824

Name:   	xdg-desktop-portal-umbriel
Version:	0^%{commitdate}git.%{shortcommit}
Release:	1%{?dist}
Summary:    An xdg-desktop-portal backend for the Umbriel compositor

License:	MIT
URL:		https://github.com/noctalia-dev/xdg-desktop-portal-umbriel
Source0:	https://github.com/noctalia-dev/xdg-desktop-portal-umbriel/archive/%{commit}/xdg-desktop-portal-umbriel-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(gtk4)

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n xdg-desktop-portal-umbriel-%{commit}

# Manually insert commit hash
sed -i "s/'unknown'/'%{shortcommit}'/g" meson.build

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE

%changelog
* Mon Aug 24 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
