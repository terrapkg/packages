#? https://src.fedoraproject.org/rpms/hyprland-protocols/blob/rawhide/f/hyprland-protocols.spec

%global realname hyprland-protocols
%global ver 0.7.0
%global commit 3f3860b869014c00e8b9e0528c7b4ddc335c21ab
%global commit_date 20251209
%global shortcommit %{sub %commit 1 7}

Name:           %realname.nightly
Version:        %ver^%{commit_date}git.%shortcommit
Release:        1%?dist
Summary:        Wayland protocol extensions for Hyprland
BuildArch:      noarch

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-protocols
Source0:        %url/archive/%commit.tar.gz

BuildRequires:  meson
Packager:		madonuko <mado@fyralabs.com>
Provides:		%realname = %evr
Conflicts:		%realname

%description
%{summary}.

%package        devel
Summary:        Wayland protocol extensions for Hyprland
Provides:		%realname-devel = %evr
Conflicts:		%realname-devel

%description    devel
%{summary}.


%prep
%autosetup -p1 -n %realname-%commit


%build
%meson
%meson_build


%install
%meson_install


%files devel
%license LICENSE
%doc README.md
%{_datadir}/pkgconfig/%{realname}.pc
%{_datadir}/%{realname}/
