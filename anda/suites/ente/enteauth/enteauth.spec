%global appid io.ente.enteauth
%global tag auth-v4.4.23

Name:           enteauth
Version:        %(echo %tag | sed 's/^auth-v//')
Release:        1%{?dist}
Summary:        2FA app with free end-to-end encrypted backup and sync
License:        AGPL-3.0-only
URL:            https://ente.com
Source0:        https://github.com/ente-io/ente/archive/refs/tags/%tag.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  flutter

%description
%summary.

%prep
%autosetup -n ente-%tag

%build
pushd mobile/apps/auth
flutter config --enable-linux-desktop
flutter build linux --release

%install

%terra_appstream mobile/apps/auth/linux/packaging/enteauth.appdata.xml
%desktop_file_install mobile/apps/auth/linux/packaging/enteauth.desktop

%files
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md SECURITY.md SUPPORT.md README.md
%license LICENSE

%changelog
* Tue Jun 16 2026 madonuko <mado@fyralabs.com> - 4.4.23-1
- Initial package.
