%global appid com.championpeak87.cosmic-ext-classic-menu

Name:           cosmic-ext-flux
Version:        3.1.1
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
Summary:        Animated desktop wallpapers for COSMIC — play any video or GIF as your background
URL:            https://www.franz-e.net/cosmic-ext-flux/
Source0:        https://github.com/franz-net/cosmic-ext-flux/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  wayland-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  just
Requires:       cosmic-osd
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
just rootdir=%{buildroot} install

%files
%doc README.md
%license LICENSE LICENSE.dependencies

%changelog
* Wed Jul 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
