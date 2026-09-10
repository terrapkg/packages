%global commit fdd0e4fe378210e7ef2c5f965e2c85f63de6c3be
%global shortcommit %{sub %{commit} 0 7}
%global commitdate 20260904

Name:          	fedora-updater
Version:        0^%{commitdate}.git%{shortcommit}
Release:        1%{?dist}
Summary:        Alternative desktop application to Gnome Software Update to use on Fedora Desktop 
SourceLicense:  Apache-2.0
License:	%{sourcelicense} AND (Apache-2.0 OR MIT) AND MIT AND (Unlicense OR MIT)
URL:            https://github.com/rkalla/fedora-updater
Source0:        %{url}/archive/%{commit}.tar.gz
Source1:	fedora-updater.desktop

BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:	blueprint-compiler
BuildRequires:	gtk4-devel
BuildRequires:	libadwaita-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Alternative desktop application to Gnome Software Update to use on Fedora
Desktop. More detail, better UX experience, precision of DNF without all
the pauses and long-winded reloads. Updates DNF, Flatpack, FW
and everything else Software Update does

%prep
%autosetup -C
%cargo_prep_online
%cargo_license_summary_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/fedora-updater                       %{buildroot}%{_bindir}/fedora-updater
install -Dm0644 data/icons/dev.fedora.Updater.png		%{buildroot}%{_hicolordir}/512x512/apps/dev.fedora.Updater.png
%desktop_file_install %{S:1}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/fedora-updater.desktop

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%{_bindir}/fedora-updater
%{_appsdir}/fedora-updater.desktop
%{_hicolordir}/512x512/apps/dev.fedora.Updater.png

%changelog
* Thu Sep 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit

