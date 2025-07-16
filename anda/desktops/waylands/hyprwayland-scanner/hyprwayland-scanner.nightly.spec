#? https://src.fedoraproject.org/rpms/hyprwayland-scanner/blob/rawhide/f/hyprwayland-scanner.spec

%global realname hyprwayland-scanner
%global ver 0.4.5
%global commit fcca0c61f988a9d092cbb33e906775014c61579d
%global shortcommit %{sub %commit 1 7}
%global commit_date 20250708

Name:           %realname.nightly
Version:        %ver^%{commit_date}git.%shortcommit
Release:        1%?dist
Summary:        A Hyprland implementation of wayland-scanner, in and for C++

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprwayland-scanner
Source0:        %url/archive/%commit.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  cmake(pugixml)
BuildRequires:  gcc-c++

Provides:		%realname = %evr
Conflicts:		%realname
Packager:		madonuko <mado@fyralabs.com>

%description
%{summary}.

%package        devel
Summary:        A Hyprland implementation of wayland-scanner, in and for C++
Provides:		%realname-devel = %evr
Conflicts:		%realname-devel

%description    devel
%{summary}.

%prep
%autosetup -p1 -n %realname-%commit

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_bindir}/%{realname}
%{_libdir}/pkgconfig/%{realname}.pc
%{_libdir}/cmake/%{realname}/
