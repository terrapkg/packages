Name:           wallr
Version:        0.6.0
Release:        1%{?dist}
Summary:        GPU accelerated animated wallpaper engine for Wayland
URL:            https://github.com/programmersd21/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  MIT
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND WTFPL AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND ISC AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

BuildRequires:  rust cargo-rpm-macros ffmpeg-free-devel libglvnd libxkbcommon wayland-devel wayland-protocols-devel cmake git pkgconfig(libavutil) pkgconfig(libavformat) pkgconfig(libswscale) clang-devel

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm 755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/%{name}
%license LICENSE LICENSE.dependencies
%doc README.md docs/*

%changelog
* Thu Sep 17 2026 Its-J <jonah@fyralabs.com> - 0.5.0-1
- Initial commit
