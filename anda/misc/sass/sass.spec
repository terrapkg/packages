# https://file.coffee/u/Gz5mMFn8_KItLQ.jpg
%global debug_package %{nil}
%global __os_install_post %{nil}
%define _build_id_links none

Name: sass
Version: 1.77.5
Release: 1%?dist
Summary: The reference implementation of Sass, written in Dart
License: MIT
URL: https://sass-lang.com/dart-sass

Source0: https://github.com/sass/dart-sass/archive/refs/tags/%{version}.tar.gz

BuildRequires: dart git

%description
Dart Sass is the primary implementation of Sass, which means it gets new
features before any other implementation. It's fast, easy to install, and it
compiles to pure JavaScript which makes it easy to integrate into modern web
development workflows.

%prep
%setup -q -n dart-sass-%{version}
/usr/bin/dart pub get

%build
# first install `buf`
curl -sSL "https://github.com/bufbuild/buf/releases/download/v1.21.0/buf-$(uname -s)-$(uname -m)" -o buf
chmod +x buf
cp buf /bin/ # this is stupid but maybe it works and I can finally die "piecefully"

dart run grinder protobuf
dart compile exe ./bin/sass.dart -o sass

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 sass %{buildroot}%{_bindir}/sass

%files
%{_bindir}/sass
%license LICENSE
%doc README.md

%changelog
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 1.56.1-1
- new version

* Tue Oct 11 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.53.0-5
- Repackaged from tauOS repository
