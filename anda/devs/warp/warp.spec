%global appid dev.warp.WarpOss
%undefine __brp_mangle_shebangs
%global __requires_exclude ^libm\\.so\\.6$

Name:           warp
Version:        0.2026.06.09.19.54
Release:        1%{?dist}
Summary:        Warp is an agentic development environment, born out of the terminal
URL:            https://warp.dev/
Source0:        https://github.com/warpdotdev/warp/archive/refs/tags/v%{version}.dev_00.tar.gz
SourceLicense:  AGPL-3.0-only AND MIT
License:        AGPL-3.0-only AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (0BSD OR MIT OR Apache-2.0) AND 0BSD AND AGPL-3.0-only AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT/MPL-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND APACHE-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR MIT OR Apache-2.0) AND BSD-2-Clause AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (BSD-3-Clause OR MIT) AND BSD-3-Clause AND BSL-1.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CC0-1.0 AND CDLA-Permissive-2.0 AND (GPL-3.0-or-later OR BSD-3-Clause) AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND (ISC AND (Apache-2.0 OR ISC)) AND ISC AND (LGPL-3.0-or-later OR MPL-2.0) AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR BSD-3-Clause) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Unlicense AND (Zlib OR Apache-2.0 OR MIT) AND Zlib AND (zlib-acknowledgement OR MIT)
BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cargo-rpm-macros
BuildRequires:  protobuf-devel
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/warp-oss                          %{buildroot}%{_bindir}/warp-terminal-oss
install -Dm644 app/channels/oss/%{appid}.desktop            %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm644 app/channels/oss/icon/no-padding/512x512.png %{buildroot}%{_hicolordir}/512x512/apps/%{appid}.png

# Launcher: picks up ~/.config/%{name}-flags.conf, mirroring upstream.
cat > %{buildroot}%{_bindir}/warp-terminal <<EOF
#!/bin/bash
XDG_CONFIG_HOME=\${XDG_CONFIG_HOME:-~/.config}
if [[ -f \$XDG_CONFIG_HOME/%{name}-flags.conf ]]; then
WARP_USER_FLAGS="\$(grep -v '^#' \$XDG_CONFIG_HOME/%{name}-flags.conf)"
fi
exec %{_bindir}/warp-terminal-oss \$WARP_USER_FLAGS "\$@"
EOF

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md SECURITY.md
%license LICENSE-AGPL LICENSE-MIT
%license LICENSE.dependencies
%{_bindir}/warp-terminal
%{_bindir}/warp-terminal-oss
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/512x512/apps/%{appid}.png

%changelog
* Mon Aug 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit

