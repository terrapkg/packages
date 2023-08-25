%global real_name vala-lint

%global commit 6c4eda0ccc040eb950eedc532607903cc7f9e2b7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global commit_date %(date '+%Y%m%d')
%global snapshot_info %{commit_date}.%{shortcommit}

Name:			vala-lint-nightly
Summary:		Check Vala code files for code-style errors
Version:		0.1.0^%{snapshot_info}
Release:		1%{?dist}
License:		GPL-2.0-or-later

URL:			https://github.com/vala-lang/vala-lint
Source0:		https://github.com/vala-lang/vala-lint/archive/%{commit}/%{real_name}-%{shortcommit}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	ninja-build
BuildRequires:	vala		= 0.56.4
BuildRequires:	vala-devel	= 0.56.4

%description
Small command line tool and library for checking Vala code files for code-style
errors. Based on the elementary Code-Style guidelines.

%package devel
Summary:	Development files for vala-lint
Requires:	vala-lint-nightly = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed
for using vala-lint as a library.

%prep
%autosetup -n %{real_name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install
ln -sf %{_bindir}/io.elementary.vala-lint %{buildroot}%{_bindir}/vala-lint

%files
%license COPYING
%doc README.md
%{_bindir}/io.elementary.vala-lint
%{_bindir}/vala-lint
%{_libdir}/libvala-linter-1.0.so.*

%files devel
%doc README.md
%license COPYING
%{_includedir}/vala-linter-1.0/vala-linter.h
%{_libdir}/pkgconfig/vala-linter-1.pc
%{_libdir}/libvala-linter-1.0.so
%{_datadir}/vala/vapi/vala-linter-1.vapi

%changelog
* Tue Feb 7 2023 lleyton <lleyton@fyralabs.com> - 0.1.0.20230208.923adb5-1
- Initial package
