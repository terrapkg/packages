Name:           cpuid2cpuflags
Summary:        Tool to generate CPU_FLAGS_* for your CPU
Version:        18
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/gentoo/cpuid2cpuflags
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
The program attempts to obtain the
identification and capabilities of the
currently used CPU, and print the matching
set of CPU_FLAGS_* flags for Gentoo.

%prep
%autosetup -C

%conf
autoreconf -vi
%configure

%build
%make_build

%install
%make_install

%files
%doc README.rst CONTRIBUTING.rst
%license COPYING
%{_bindir}/cpuid2cpuflags

%changelog
* Fri Nov 13 2026 Owen Zimmerman <owen@fyralabs.com> - 18-1
- Initial commit
