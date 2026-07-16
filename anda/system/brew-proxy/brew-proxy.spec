# This spec file contains portions of code licensed under the MIT license.
# 
# MIT License
#
# Copyright (c) 2026 Contributors to brew-proxy <https://codeberg.org/HastD/brew-proxy>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Globals.
%global proxy_dbus_name sh.brew.BrewProxy
%global with_selinux 1
%global modulename brew-proxy
%global selinuxtype targeted

# Metadata.
Name:    brew-proxy
Version: 0.3.2
Release: 1%{?dist}
Summary: DBus-activated proxy service for a more secure Homebrew setup on Linux 
License:        %{shrink:
    ((MIT OR Apache-2.0) AND Unicode-3.0)
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND MIT
}
SourceLicense: Apache-2.0 OR MIT
Packager: libffi <contact@ffi.lol>

# Links.
URL:     https://codeberg.org/HastD/%{name}
Source0: %{url}/archive/v%{version}.tar.gz

# Macros.
BuildRequires: systemd-rpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: anda-srpm-macros
BuildRequires: rust-srpm-macros

# Build tooling.
BuildRequires: meson
BuildRequires: clang
BuildRequires: mold

# Subpackages.
Recommends: %{name}-selinux

%package selinux
# Meta.
Summary: SELinux policy for %{name}
Requires:       %{name}
BuildArch:      noarch

# Libraries.
BuildRequires: selinux-policy-devel
%selinux_requires

%description
brew-proxy is a DBus-activated service that facilitates configuring a
Homebrew installation on Linux more securely.

%description selinux
SELinux policy for %{name}.

%prep
%autosetup -C
%cargo_prep_online
%meson

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies
%meson_build

%install
%meson_install

%check
# Tests from the `tests/` directory are not feasible to run as they are E2E
# tests that require a working dbus instance and a configured service.
%cargo_test -- --lib --bin brew-proxy --bin brew-proxy-daemon
%cargo_test -- --doc
%cargo_test -- -p %{name}-utils

%post
%systemd_post %{name}-daemon.service
%systemd_post %{name}-setup.service

%preun
%systemd_preun %{name}-daemon.service
%systemd_preun %{name}-setup.service

%postun
%systemd_postun_with_restart %{name}-daemon.service
%systemd_postun_with_reload %{name}-setup.service

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun selinux
if [ "$1" -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%files
%license LICENSE.dependencies
%license LICENSES/Apache-2.0.txt
%license LICENSES/MIT.txt
%license LICENSES/CC0-1.0.txt
%doc README.md
%doc CHANGELOG.md
%{_sysconfdir}/profile.d/%{name}.*
%{_bindir}/%{name}
%{_unitdir}/%{name}-daemon.service
%{_unitdir}/%{name}-setup.service
%{_sysusersdir}/%{name}.conf
%{_libexecdir}/%{name}/
%{_datadir}/dbus-1/system-services/{%proxy_dbus_name}.service
%{_datadir}/dbus-1/system.d/{%proxy_dbus_name}.conf
%{_datadir}/fish/vendor_conf.d/%{name}.fish
%{_datadir}/polkit-1/actions/%{proxy_dbus_name}.policy
%{_datadir}/polkit-1/rules.d/%{proxy_dbus_name}.rules
%{_environmentdir}/30-%{name}.conf

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}

%changelog
* Tue Jun 30 2026 libffi <contact@ffi.lol> - 0.3.1
- Initial release
