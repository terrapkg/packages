# rustix 0.37.x enables obsolete rustc_attrs when RUSTC_BOOTSTRAP=1.
# The cargo macros normally set it for -Z avoid-dev-deps, which is unnecessary
# here and incompatible with the system compiler.
%global __cargo_common_opts %{?_smp_mflags}

%ifarch x86_64
%global scarch x64
%else
%ifarch aarch64
%global scarch arm64
%endif
%endif

Name:           rustdesk
Version:        1.4.9
Release:        1%{?dist}
Summary:        Open-source remote desktop software
ExclusiveArch:  x86_64 aarch64
SourceLicense:  AGPL-3.0-only
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND Unlicense AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND IJG AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND BSD-2-Clause AND Zlib AND MIT AND WTFPL AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND IJG AND Zlib AND BSD-3-Clause AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND GPL-3.0+ AND Apache-2.0 AND ISC AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (BSD-3-Clause OR MIT) AND BSL-1.0 AND ISC AND (MIT OR X11 OR Apache-2.0) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://rustdesk.com
Source0:        https://github.com/c-smile/sciter-sdk/raw/master/bin.lnx/%{scarch}/libsciter-gtk.so
Source1:        rustdesk.te
Patch0:         scrap-use-pkg-config-for-libyuv.patch
BuildRequires:  alsa-lib-devel
BuildRequires:  anda-srpm-macros
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  curl
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gstreamer1-devel
BuildRequires:  gtk3-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libaom-devel
BuildRequires:  libvpx-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxdo-devel
BuildRequires:  libyuv-devel
BuildRequires:  nasm
BuildRequires:  opus-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  rust-gstreamer-devel
BuildRequires:  rust-packaging
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  wget
BuildRequires:  yasm
BuildRequires:  perl
Requires:       alsa-lib
Requires:       gstreamer1-plugins-base
Requires:       gtk3
Requires:       libXfixes
Requires:       libappindicator
Requires:       libva2
Requires:       libvdpau1
Requires:       libxcb
Requires:       libxdo
Requires:       pam
Requires:       (%{name}-selinux = %{evr} if selinux-policy-%{selinuxtype})

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
The best open-source remote desktop client software, written in Rust.

%package selinux
Summary:        SELinux policy module for RustDesk
BuildArch:      noarch
Requires:       %{name} = %{evr}
%{?selinux_requires}

%description selinux
This package contains the SELinux policy module necessary to run RustDesk.

%prep
%git_clone https://github.com/rustdesk/rustdesk.git %{version}
%patch -P 0 -p1
sed -i 's|magnum-opus = { git = "https://github.com/rustdesk-org/magnum-opus" }|magnum-opus = { git = "https://github.com/rustdesk-org/magnum-opus", features = ["linux-pkg-config"] }|' Cargo.toml
sed -i 's|scrap = { path = "libs/scrap", features = ["wayland"] }|scrap = { path = "libs/scrap", features = ["wayland", "linux-pkg-config"] }|' Cargo.toml
%cargo_prep_online

%build
export OPENSSL_NO_VENDOR=true
# rust-webm's bundled libwebm uses uint32_t/uint64_t without including <cstdint>.
export CXXFLAGS="${CXXFLAGS} -include cstdint"
%global __cargo /usr/bin/env CARGO_HOME=.cargo RUSTFLAGS='%{build_rustflags}' /usr/bin/cargo
%cargo_build

# Keep the established Cargo macro environment for the dependency license scan.
%global __cargo /usr/bin/env CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 RUSTFLAGS='%{build_rustflags}' /usr/bin/cargo
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

mkdir SELinux
cp %{SOURCE1} SELinux/rustdesk.te
%{__make} -C SELinux NAME=%{selinuxtype} -f %{_datadir}/selinux/devel/Makefile

%install
install -Dpm755 target/rpm/rustdesk %{buildroot}%{_bindir}/rustdesk
install -Dpm755 target/rpm/naming %{buildroot}%{_bindir}/naming
install -Dpm755 %{SOURCE0} %{buildroot}/usr/lib/rustdesk/libsciter-gtk.so
install -Dpm644 SELinux/rustdesk.pp %{buildroot}%{_datadir}/selinux/%{selinuxtype}/rustdesk.pp
install -Dpm644 res/rustdesk.service %{buildroot}%{_datadir}/rustdesk/files/rustdesk.service
install -Dpm644 res/128x128@2x.png %{buildroot}%{_iconsdir}/hicolor/256x256/apps/rustdesk.png
install -Dpm644 res/scalable.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/rustdesk.svg
install -Dpm644 res/rustdesk.desktop %{buildroot}%{_datadir}/rustdesk/files/rustdesk.desktop
install -Dpm644 res/rustdesk-link.desktop %{buildroot}%{_datadir}/rustdesk/files/rustdesk-link.desktop
install -Dpm644 res/rustdesk.desktop %{buildroot}%{_appsdir}/rustdesk.desktop
install -Dpm644 res/rustdesk-link.desktop %{buildroot}%{_appsdir}/rustdesk-link.desktop
install -Dpm644 res/rustdesk.service %{buildroot}%{_unitdir}/rustdesk.service

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/%{selinuxtype}/rustdesk.pp
%selinux_relabel_post -s %{selinuxtype}

%postun selinux
if [ "$1" -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} rustdesk
    %selinux_relabel_post -s %{selinuxtype}
fi

%post
%systemd_post rustdesk.service

%preun
%systemd_preun rustdesk.service

%postun
%systemd_postun_with_restart rustdesk.service

%files
%license LICENSE LICENSE.dependencies
%doc README.md docs/*
%{_bindir}/rustdesk
%{_bindir}/naming
/usr/lib/rustdesk/libsciter-gtk.so
%{_datadir}/rustdesk/files/rustdesk.service
%{_iconsdir}/hicolor/256x256/apps/rustdesk.png
%{_iconsdir}/hicolor/scalable/apps/rustdesk.svg
%{_datadir}/rustdesk/files/rustdesk.desktop
%{_datadir}/rustdesk/files/rustdesk-link.desktop
%{_appsdir}/rustdesk.desktop
%{_appsdir}/rustdesk-link.desktop
%{_unitdir}/rustdesk.service

%files selinux
%{_datadir}/selinux/%{selinuxtype}/rustdesk.pp

%changelog
%autochangelog
