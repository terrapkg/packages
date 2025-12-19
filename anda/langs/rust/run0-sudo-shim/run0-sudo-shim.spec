Name:			run0-sudo-shim
Version:		1.2.0
Release:		1%?dist
Summary:		An imitation of sudo, using run0 internally
SourceLicense:	BSD-3-Clause
License:		(Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT
URL:			https://github.com/LordGrimmauld/run0-sudo-shim
Source0:		%url/archive/refs/tags/%version.tar.gz
BuildRequires:	rpm_macro(cargo_install) rust-packaging
Conflicts:		sudo

%description
run0-sudo-shim attempts to imitate sudo as close as possible, while actually using run0 in the back.

run0 does not rely on SUID binaries, which makes it a more secure option. It is also included in any systemd-based linux installation.

However, many programs just expect sudo to exist, so a shim is necessary to make those programs work.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install
ln -s %_bindir/run0-sudo-shim %buildroot%_bindir/sudo

%files
%doc README.md
%license LICENSE.dependencies
%_bindir/run0-sudo-shim
%_bindir/sudo
