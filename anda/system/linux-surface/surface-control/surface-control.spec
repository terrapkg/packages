%global ver v0.5.0-1

%define debug_package %{nil}

Name:           surface-control
Version:        0.5.0.1
Release:        1%{?dist}
Summary:        Control various aspects of Microsoft Surface devices from the shell

SourceLicense:  MIT
License:        %{sourcelicense} AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:            https://github.com/linux-surface/surface-control
Source0:        %{url}/archive/refs/tags/%{ver}.tar.gz

Requires:       dbus
Requires:       libgcc
Requires:       systemd-libs
BuildRequires:  cargo-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Control various aspects of Microsoft Surface devices on Linux from the shell.
Aims to provide a unified front-end to the various sysfs-attributes and special
devices.

%prep
%autosetup -C
%cargo_prep_online
%cargo_license_summary_online

%pkg_completion -bfz -n surface

%build
export CARGO_TARGET_DIR="$PWD/target"
%cargo_build

%install
install -Dm755 target/rpm/surface                   %{buildroot}%{_bindir}/surface
install -Dm644 target/surface.bash                  %{buildroot}%{bash_completions_dir}/surface.bash
install -Dm644 target/_surface                      %{buildroot}%{zsh_completions_dir}/_surface
install -Dm644 target/surface.fish                  %{buildroot}%{fish_completions_dir}/surface.fish
install -Dm644 target/systemd/surface-rapl.service  %{buildroot}%{_unitdir}/surface-rapl.service
install -Dm744 target/systemd/surface-rapl.sh       %{buildroot}%{_libexecdir}/surface-rapl.sh
%{cargo_license_online} > LICENSE.dependencies

%post
%systemd_post surface-rapl.service

%preun
%systemd_preun surface-rapl.service

%postun
%systemd_postun_with_restart surface-rapl.service

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/surface
%{_unitdir}/surface-rapl.service
%{_libexecdir}/surface-rapl.sh

%changelog
* Sat Aug 29 2026 Owen Zimmerman <owen@fyralabs.com> - 0.5.0-1-1
- Initial commit, port to Terra from linux-surface
