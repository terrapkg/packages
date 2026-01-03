Name:               breakpad
Version:            2024.02.16
Release:            2%?dist
Summary:            Google Breakpad crash-reporting system
License:            BSD-3-Clause
Group:		        System
URL:                https://github.com/google/breakpad
Source0:            https://github.com/google/breakpad/archive/refs/tags/v%{version}.tar.gz
Source1:            https://chromium.googlesource.com/linux-syscall-support/+archive/refs/heads/main.tar.gz#/lss.tar.gz

BuildRequires:      gcc-c++
BuildRequires:      pkgconfig(gmock)
BuildRequires:      pkgconfig(gtest)
BuildRequires:      pkgconfig(zlib)
BuildRequires:      anda-srpm-macros

Packager:           Willow Reed (willow@willowidk.dev)

%description
A set of client and server components which implement a crash-reporting system.

%package devel
Requires:	%{name} = %{evr}
%pkg_devel_files

%package static
%pkg_static_files

%prep
%autosetup -n breakpad-%{version}
mkdir -p src/third_party/lss
cd src/third_party/lss
tar -xzf %{SOURCE1} --strip-components=0

%build
export CFLAGS="$CFLAGS -Wno-error"
export CXXFLAGS="$CXXFLAGS -Wno-error"

%configure
%make_build

%install
%make_install

rm -rf %{buildroot}%{_docdir}/breakpad-0.1

%files
%license LICENSE
%doc README.md AUTHORS ChangeLog INSTALL NEWS
%{_bindir}/core2md
%{_bindir}/dump_sym*
%{_bindir}/microdump_stackwalk
%{_bindir}/minidump-2-core
%{_bindir}/minidump_dump
%{_bindir}/minidump_stackwalk
%{_bindir}/minidump_upload
%{_bindir}/pid2md
%{_bindir}/sym_upload
%{_libexecdir}/core_handler

%changelog
* Fri Jan 02 2026 Willow Reed <willow@willowidk.dev>
- Initial commit
