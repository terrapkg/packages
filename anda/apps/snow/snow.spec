Name:           snow
Version:        1.3.1
Release:        1%?dist
Summary:        Classic Macintosh emulator
URL:            https://github.com/twvd/snow
Source0:        %url/archive/refs/tags/v%version.tar.gz
License:        MIT AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Apache-2.0 AND BSD-2-Clause AND Zlib AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (BSD-3-Clause OR Apache-2.0) AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 OR MIT-0 OR Apache-2.0 AND ISC AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND

BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  mold
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  SDL2-devel
Provides:       snowemu

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Snow emulates classic (Motorola 68k-based) Macintosh computers.
It features a graphical user interface to operate and debug the emulated machine.
The aim of this project is to emulate the Macintosh on a hardware-level as much as possible,
as opposed to emulators that patch the ROM or intercept system calls.

%package doc
Summary:        Documentation files for %{name}

%description doc
Documentation files for %{name}

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
mkdir -p %{buildroot}%{_pkgdocdir}
install -Dm755 target/rpm/snowemu                   %{buildroot}%{_bindir}/snowemu
install -Dm644 assets/snow_icon.png                 %{buildroot}%{_hicolordir}/1024x1024/apps/snow_icon.png
%desktop_file_install assets/snow.desktop
install -Dm644 assets/dev.thomasw.snow.metainfo.xml %{buildroot}%{_metainfodir}/dev.thomasw.snow.metainfo.xml

cp -a docs/*                                        %{buildroot}%{_pkgdocdir}/
rm %{buildroot}%{_pkgdocdir}/*.toml
rm -r %{buildroot}%{_pkgdocdir}/theme

%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/snowemu
%{_hicolordir}/1024x1024/apps/snow_icon.png
%{_appsdir}/snow.desktop
%{_metainfodir}/dev.thomasw.snow.metainfo.xml

%files doc
%license LICENSE
%doc %{_pkgdocdir}/*

%changelog
* Tue Dec 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
