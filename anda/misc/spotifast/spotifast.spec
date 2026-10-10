Name:           spotifast
Version:        0.11.2
Release:        1%?dist
Summary:        Spotify client rewritten in Rust
URL:            https://github.com/crmne/spotifast
Source0:        %url/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  MIT
License:        %{sourcelicense}

BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  clang-devel
%dnl waiting on Neal to fix libprojectM-devel https://src.fedoraproject.org/rpms/libprojectM
BuildRequires:  libprojectM-devel

Provides:       fastpotify

Packager:       Its-J <jonah@fyralabs.com>

%description
Spotify client written in Rust. It plays music through librespot, uses 100–250 MB of RAM, while Spotify's desktop app often uses 600 MB to over 1 GB.

%package       docs
Summary:       Documentation files for spotifast

%description   docs
Documentation files for spotifast.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}

%files docs
%doc docs/*.md

%changelog
* Wed Sep 30 2026 Its-J <jonah@fyralabs.com> - 0.11.2-1
- Initial commit
