Name:           rustnet
Version:        1.0.0
Release:        1%?dist
Summary:        A cross-platform network monitoring terminal UI tool built with Rust
License:        Apache-2.0 AND (MIT OR Apache-2.0) AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (LGPL-2.1-only OR BSD-2-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
URL:            https://github.com/domcyrus/rustnet
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  cargo-rpm-macros
BuildRequires:  libpcap-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  clang
BuildRequires:  llvm

Requires:       libpcap
Requires:       elfutils-libelf

%description
A cross-platform network monitoring tool built with Rust. RustNet provides
real-time visibility into network connections with detailed state information,
connection lifecycle management, deep packet inspection, and a terminal user
interface.

Features include:
- Real-time Network Monitoring for TCP, UDP, ICMP, and ARP connections
- Deep Packet Inspection (DPI) for HTTP/HTTPS, DNS, SSH, and QUIC protocols
- Connection lifecycle management with protocol-aware timeouts
- Process identification and service name resolution
- Cross-platform support (Linux, macOS, Windows, BSD)
- Advanced filtering with vim/fzf-style search
- eBPF-enhanced process detection (enabled by default with automatic fallback)

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
# Cargo macros fail due to RUSTC_BOOTSTRAP and build target
cargo build

%install
install -Dm755 target/debug/rustnet -t %{buildroot}%{_bindir}/
install -Dm644 assets/services -t %{buildroot}%{_datadir}/%{name}/
install -Dm644 resources/packaging/linux/graphics/rustnet.png -t %{buildroot}%{_hicolordir}/256x256/apps/
install -Dm644 resources/packaging/linux/rustnet.desktop -t %{buildroot}%{_appsdir}/

%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE
%license LICENSE.dependencies
%doc *.md
%{_bindir}/rustnet
%{_datadir}/%{name}/services
%{_hicolordir}/256x256/apps/rustnet.png
%{_appsdir}/rustnet.desktop

%changelog
* Mon Jan 12 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
