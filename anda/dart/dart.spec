Name: dart
Version: 2.18.2
Release: 1%{?dist}
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

%description
Dart is a client-optimized language for fast apps on any platform. This package contains the SDK used to develop and compile Dart applications.

%prep
%setup -n dart-sdk

%install
# install the folders inside
install -vd %{buildroot}%{_bindir}
install -vd %{buildroot}%{_libdir}/dart

cp -rv ./* %{buildroot}%{_libdir}/dart

ln -sf /usr/lib/dart/bin/dart %{buildroot}/usr/bin/dart
ln -sf /usr/lib/dart/bin/dartaotruntime %{buildroot}/usr/bin/dartaotruntime

%files
%{_libdir}/dart/
%{_bindir}/dart
%{_bindir}/dartaotruntime

%license LICENSE
%doc README

%changelog
* Tue Oct 11 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 2.18.2-1
- Repackaged dart for Terra
