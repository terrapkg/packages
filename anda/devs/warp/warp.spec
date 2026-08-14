%global appid dev.warp.WarpOss
%undefine __brp_mangle_shebangs
%global __requires_exclude ^libm\\.so\\.6$

Name:           warp
Version:        0.2026.06.09.19.54
Release:        1%{?dist}
Summary:        Warp is an agentic development environment, born out of the terminal
URL:            https://warp.dev/
Source0:        https://github.com/warpdotdev/warp/archive/refs/tags/v%{version}.dev_00.tar.gz
SourceLicense:  AGPL-3.0-only
License:        AGPL-3.0-only
BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cargo-rpm-macros
BuildRequires:	protobuf-devel
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

