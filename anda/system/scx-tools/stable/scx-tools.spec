%global appid com.sched_ext.scx
%global developer "sched-ext Contributors"
%global org "com.sched_ext"

Name:           scx-tools
Version:        1.0.20
Release:        1%?dist
Summary:        Sched_ext Tools
License:        ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND GPL-2.0-only AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0) AND MIT AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
SourceLicense:  GPL-2.0-only
URL:            https://github.com/sched-ext/scx-loader
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  bpftool
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang >= 17
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  libseccomp-devel
BuildRequires:  lld >= 17
BuildRequires:  llvm >= 17
BuildRequires:  mold
BuildRequires:  python3
BuildRequires:  rust
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
Requires:       (scx-scheds or scx-scheds-nightly)
Suggests:       scx-scheds
Obsoletes:      scxctl <= 0.3.4
Provides:       scxctl = %{evr}
Conflicts:      scx-tools-git
Conflicts:      scx-tools-nightly
Packager:       Gilver E. <roachy@fyralabs.com>

%description
scx_loader: A D-Bus interface for managing sched_ext schedulers

%prep
%autosetup -n scx-loader-%{version}
%cargo_prep_online

%build
%{cargo_build -a} \
     --workspace

%install
find target/rpm \
    -maxdepth 1 -type f -executable ! -name '*.so' ! -name 'xtask' \
    -exec install -Dm755 -t %{buildroot}%{_bindir} {} +

# Install runtime assets via xtask
./target/rpm/xtask install --destdir %{buildroot}

install -Dm755 target/rpm/*.so -t %{buildroot}%{_libdir} || :

%{cargo_license_online} > LICENSE.dependencies

%terra_appstream

%post
%systemd_post scx_loader.service

%preun
%systemd_preun scx_loader.service

%postun
%systemd_postun_with_restart scx_loader.service

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/scx*
%{_unitdir}/scx_loader.service
%{_datadir}/dbus-1/interfaces/org.scx.Loader.xml
%{_datadir}/dbus-1/system-services/org.scx.Loader.service
%{_datadir}/dbus-1/system.d/org.scx.Loader.conf
%{_datadir}/polkit-1/actions/org.scx.Loader.policy
%{_datadir}/scx_loader/config.toml
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Nov 16 2025 Gilver E. <rockgrub@disroot.org> - 1.0.18-1
- Initial package
