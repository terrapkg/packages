%global commit dba72ec721a9caee8ad5b91d26ad92a5af133aae
%global commit_date 20261015
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           singularity-accounts
Summary:        Online accounts for the Singularity Desktop Environment
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://github.com/singularityos-lab/singularity-accounts
Source0:        %url/archive/%commit/singularity-accounts-%commit.tar.gz
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vetro
BuildRequires:  vala
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(gee-0.8)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

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
%{_libexecdir}/singularity-accounts
%{_datadir}/dbus-1/services/dev.sinty.Accounts.service
%{_scalableiconsdir}/singularity-account-*.svg

%changelog
* Fri Oct 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
