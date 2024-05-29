%define debug_package %{nil}

Name: dart
Version: 3.4.2
Release: 1%?dist
Summary: The Dart Language
License: BSD-3-Clause
URL: https://dart.dev/

%ifarch x86_64
%define arch x64
%elifarch aarch64
%define arch arm64
%elifarch i386
%define arch ia32
%elifarch armv7l
%define arch arm
%endif

Source0: https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-%{arch}-release.zip
BuildRequires: fdupes

%description
Dart is a client-optimized language for fast apps on any platform.
This package contains the SDK used to develop and compile Dart applications.

%prep
%setup -q -n dart-sdk

%build

%install
# install the folders inside
install -vd %{buildroot}%{_bindir}
install -vd %{buildroot}%{_libdir}/dart

cp -rv ./* %{buildroot}%{_libdir}/dart

ln -sf %{_libdir}/dart/bin/dart %{buildroot}%{_bindir}/dart
ln -sf %{_libdir}/dart/bin/dartaotruntime %{buildroot}%{_bindir}/dartaotruntime

%fdupes %buildroot%_libdir/dart/bin/

%files
%{_libdir}/dart/
%{_bindir}/dart
%{_bindir}/dartaotruntime

%license LICENSE
%doc README

%changelog
* Thu Nov 17 2022 windowsboy111 <windowsboy111@fyralabs.com> - 2.18.4-1
- Bump

* Tue Oct 11 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 2.18.2-1
- Repackaged dart for Terra
