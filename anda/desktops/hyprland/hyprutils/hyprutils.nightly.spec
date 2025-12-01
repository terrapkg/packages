#? https://src.fedoraproject.org/rpms/hyprutils/blob/rawhide/f/hyprutils.spec

%global realname hyprutils
%global ver 0.10.4

%global commit 7e6346f84be8918e3eca405546c45fb37d74bdfe
%global commit_date 20251130
%global shortcommit %{sub %commit 1 7}

Name:           %realname.nightly
Version:        %ver^%{commit_date}git.%shortcommit
Release:        1%?dist
Summary:        Hyprland utilities library used across the ecosystem

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprutils
Source0:        %url/archive/%commit.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  cmake(GTest)

Provides:		%realname = %evr
Conflicts:		%realname

%description
%{summary}.

%package        devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:		%realname-devel = %evr
Conflicts:		%realname-devel
%pkg_devel_files

%prep
%autosetup -p1 -n %realname-%commit

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{realname}.so.%{ver}
%{_libdir}/lib%{realname}.so.*
