Name:           wavemon
Version:        0.9.7
Release:        1%{?dist}
Summary:        ncurses-based monitoring application for wireless network devices on Linux
License:        GPL-3.0-or-later
URL:            https://github.com/uoaerg/wavemon
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  autoconf
BuildRequires:  automake

%description
%{summary}.

%prep
%autosetup
sed -e '/^CFLAGS=/d' -i configure.ac
sed -r 's|\?=|=|g' -i Makefile.in
autoreconf -fiv

%conf
CFLAGS="$RPM_OPT_FLAGS -fPIC -pie -Wl,-z,relro -Wl,-z,now"
CXXFLAGS="$RPM_OPT_FLAGS -fPIC -pie -Wl,-z,relro -Wl,-z,now"
export CFLAGS
export CXXFLAGS
%configure

%build
%make_build

%install
%make_install
# Delete wrong placed readme and license
rm -rf %{buildroot}%{_datadir}/%{name}/*

%files
%doc README.md
%license LICENSE
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}

%changelog
* Tue May 19 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
