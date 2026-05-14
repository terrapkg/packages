%global crate rioterm
%global appid com.rioterm.Rio
%global _description %{expand:
A hardware-accelerated terminal emulator focusing to run in desktops and browsers.}

Name:          rio
Version:       0.4.4
Release:       1%{?dist}
Summary:       A hardware-accelerated terminal written in Rust.
SourceLicense: MIT
License:       ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND BSD-2-Clause AND BSL-1.0 AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CC0-1.0 AND ISC AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND (MPL-2.0 OR GPL-3.0-only) AND MPL-2.0+ AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
URL:           https://rioterm.com/
Source0:       https://github.com/raphamorim/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: freetype-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glslc
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-devel
BuildRequires: mold
BuildRequires: sed
BuildRequires: pkgconfig(alsa)
Requires:      freetype
Requires:      fontconfig
Requires:      hicolor-icon-theme
Requires:      ncurses-term
Obsoletes:     %{crate} < %{version}-%{release}
Obsoletes:     %{name}-doc < %{evr}
Packager:      Gilver E. <roachy@fyralabs.com>

%description %_description

%package       devel
Summary:       Development files for Rio
Requires:      %{name} = %{version}-%{release}

%description   devel
This package contains the development libraries for Rio.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online
sed -i 's/Exec=.*/Exec=%{crate}/g' misc/%{name}.desktop

%build
%cargo_build -a

%install
install -Dm755 target/rpm/%{name} %{buildroot}%{_bindir}/%{crate}
install -Dm755 target/rpm/*.so -t %{buildroot}%{_libdir}
install -Dm644 misc/logo.svg %{buildroot}%{_scalableiconsdir}/%{name}.svg
install -Dm644 misc/%{appid}.metainfo.xml -t %{buildroot}%{_metainfodir}
desktop-file-install misc/%{name}.desktop
%{cargo_license_online -a} > LICENSE.dependencies

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/%{crate}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{appid}.metainfo.xml

%files devel
%{_libdir}/librio_backend.so
%{_libdir}/libsugarloaf.so

%changelog
* Mon May 5 2025 Gilver E. <rockgrub@disroot.org> - 0.2.13-1
- Added doc package
* Sat Mar 8 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
