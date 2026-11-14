Name:           cicpoffs
Version:        master
Release:        1%{?dist}
Summary:        Case-insensitive case-preserving overlay FUSE file system
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

License:        GPL-2.0-only
URL:            https://github.com/ublue-os/cicpoffs
Source0:        %{url}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libattr)

Requires:       fuse3

%description
A case-insensitive overlay FUSE file system that preserves the original case
of file names. It allows games and mods that rely on Windows-style
case-insensitive file access to work on Linux.

%prep
%autosetup

%build
# Upstream makefile uses CXX_FLAGS instead of CXXFLAGS and LDFLAGS
%make_build CXX_FLAGS="%{build_cxxflags} %{build_ldflags}"

%install
%make_install
# Upstream makefile does not create this file, but the cicpoffs github builder does.
%{__ln_s} cicpoffs %{buildroot}%{_bindir}/mount.cicpoffs

%files
%license LICENSE
%doc README.md CHANGELOG
%{_bindir}/cicpoffs
%{_bindir}/mount.cicpoffs

%changelog
* Sun Oct 18 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 1.0.0-1
- Initial package
