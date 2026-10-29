%global commit 75a7dfaca5bc27cf285b886826c52e47006a194c
%global commit_date 20261015
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           singularity-authenticator
Summary:        Authenticator for the Singularity Desktop Environment
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://github.com/singularityos-lab/singularity-authenticator
Source0:        %url/archive/%commit/singularity-authenticator-%commit.tar.gz
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(singularity-1.0)
BuildRequires:  zbar-libs

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Authenticator for the Singularity Desktop Environment:
two-factor sign-in codes for your accounts.

%prep
%autosetup -C

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/singularity-authenticator
%{_appsdir}/dev.sinty.authenticator.desktop
%{_datadir}/dbus-1/services/dev.sinty.authenticator.service
%{_datadir}/glib-2.0/schemas/dev.sinty.authenticator.gschema.xml
%{_scalableiconsdir}/dev.sinty.authenticator.svg
%{_datadir}/singularity/app-settings/dev.sinty.authenticator.json
%{_datadir}/singularity/search-providers/dev.sinty.authenticator.ini

%changelog
* Sat Oct 17 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
