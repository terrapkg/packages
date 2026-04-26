%global commit 842d02fdd9d4308fb7108a65cb5b10583f46d22e
%global commit_date 20260426
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           cloud-hypervisor-nightly
License:        Apache-2.0 AND MPL-2.0 AND (Unlicense OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND MIT AND BSD-3-Clause AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND CC-BY-4.0 AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR MIT)
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        A Virtual Machine Monitor for modern Cloud workloads
URL:            https://github.com/cloud-hypervisor/cloud-hypervisor
Source0:        %{url}/archive/%{commit}/cloud-hypervisor-%{commit}.tar.gz
BuildRequires:  perl
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(openssl)
Conflicts:      cloud-hypervisor

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A Virtual Machine Monitor for modern Cloud workloads. Features include CPU,
memory and device hotplug, support for running Windows and Linux guests,
device offload with vhost-user and a minimal compact footprint.
Written in Rust with a strong focus on security.

%package        doc
Summary:        Documentation for cloud-hypervisor
Requires:       %{name} = %{evr}

%description    doc
%{summary}.

%prep
%autosetup -n cloud-hypervisor-%{commit}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/cloud-hypervisor %{buildroot}%{_bindir}/cloud-hypervisor
install -Dm755 target/rpm/ch-remote %{buildroot}%{_bindir}/ch-remote
install -Dm755 target/rpm/vhost_user_block %{buildroot}%{_bindir}/vhost_user_block
install -Dm755 target/rpm/vhost_user_net %{buildroot}%{_bindir}/vhost_user_net

%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE.dependencies LICENSES/
%doc CODEOWNERS CODE_OF_CONDUCT.md CONTRIBUTING.md CREDITS.md MAINTAINERS.md README.md release-notes.md
%caps(cap_net_admin=ep) %{_bindir}/cloud-hypervisor
%{_bindir}/ch-remote
%{_bindir}/vhost_user_block
%{_bindir}/vhost_user_net

%changelog
* Tue Apr 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable spec)
