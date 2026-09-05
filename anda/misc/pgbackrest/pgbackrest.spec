Name:           pgbackrest
Version:        2.59.1
Release:        1%?dist
Summary:        Reliable PostgreSQL Backup & Restore
URL:            https://github.com/pgbackrest/pgbackrest
Source0:        %{url}/archive/refs/tags/release/%{version}.tar.gz
License:        MIT

BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  bzip2-devel
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libzstd)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
pgBackRest is a reliable backup and restore solution for PostgreSQL
that seamlessly scales up to the largest databases and workloads.

%prep
%autosetup -C

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%doc README.md CODING.md CONTRIBUTING.md doc/*
%license LICENSE
%{_bindir}/pgbackrest

%changelog
* Sat Sep 05 2026 Owen Zimmerman <owen@fyralabs.com> - 2.59.1-1
- Initial commit
