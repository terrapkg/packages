%define debug_package %{nil}

%global __requires_exclude libffmpeg.so|libvk_swiftshader.so|libvulkan.so|libEGL.so|libGLESv2.so
%global __provides_exclude_from %{_libdir}/%{name}/.*\\.so
%global appid net.imput.helium

%ifarch x86_64
%define arch x86_64
%elifarch aarch64
%define arch arm64
%endif

Name:           helium-browser-bin
Version:        0.9.2.1
Release:        1%?dist
Summary:        Private, fast, and honest web browser based on Chromium

URL:            https://helium.computer
License:        GPL-3.0-only AND BSD-3-Clause

Source0:        https://github.com/imputnet/helium-linux/releases/download/%{version}/helium-%{version}-%{arch}_linux.tar.xz
Source1:        https://github.com/imputnet/helium-linux/archive/refs/tags/%{version}.tar.gz
Source2:        net.imput.helium.metainfo.xml
Source3:        net.imput.helium.desktop

ExclusiveArch:  x86_64 aarch64

BuildRequires:  terra-appstream-helper
BuildRequires:  desktop-file-utils

Requires:       xdg-utils
Requires:       liberation-fonts

Packager:       Nadia P <nyadiia@pm.me>

%description
Private, fast, and honest web browser based on Chromium.
Based on ungoogled-chromium with additional privacy and usability improvements.

%prep
%autosetup -n helium-%{version}-%{arch}_linux
tar --strip-components=1 -zxvf %{SOURCE1}

%build

%install
install -dm755 %{buildroot}%{_libdir}/%{name}
cp -a * %{buildroot}%{_libdir}/%{name}/

install -Dm644 %{SOURCE3} %{buildroot}%{_appsdir}/%{appid}.desktop

install -Dm644 product_logo_256.png %{buildroot}%{_hicolordir}/256x256/apps/%{appid}.png

rm -f %{buildroot}%{_libdir}/%{name}/helium.desktop
rm -f %{buildroot}%{_libdir}/%{name}/product_logo_256.png

install -dm755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << 'EOF'

#!/bin/bash
set -euo pipefail

XDG_CONFIG_HOME="${XDG_CONFIG_HOME:-"$HOME/.config"}"
SYS_CONF="%{_sysconfdir}/helium-browser-flags.conf"
USR_CONF="${XDG_CONFIG_HOME}/helium-browser-flags.conf"

FLAGS=()

append_flags_file() {
    local file="$1"
    [[ -r "$file" ]] || return 0
    local line safe_line
    while IFS= read -r line; do
        [[ "$line" =~ ^[[:space:]]*(#|$) ]] && continue
        case "$line" in
            *'$('*|*'`'*)
                echo "Warning: ignoring unsafe line in $file: $line" >&2
                continue
                ;;
        esac
        set -f
        safe_line=${line//$/\\$}
        safe_line=${safe_line//~/\\~}
        eval "set -- $safe_line"
        set +f
        for token in "$@"; do
            FLAGS+=("$token")
        done
    done < "$file"
}

append_flags_file "$SYS_CONF"
append_flags_file "$USR_CONF"

if [[ -n "${HELIUM_USER_FLAGS:-}" ]]; then
    read -r -a ENV_FLAGS <<< "$HELIUM_USER_FLAGS"
    FLAGS+=("${ENV_FLAGS[@]}")
fi

export CHROME_WRAPPER="$(readlink -f "$0")"
export CHROME_VERSION_EXTRA="stable"

exec -a "$0" %{_libdir}/%{name}/chrome "${FLAGS[@]}" "$@"
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

%terra_appstream -o %{SOURCE2}

%files
%doc README.md
%license LICENSE LICENSE.ungoogled_chromium
%{_libdir}/%{name}/
# shebang reasons
%attr(0755,root,root) %{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/256x256/apps/%{appid}.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Feb 15 2026 Jaiden Rirordan <jade@fyralabs.com>
- Use downstream desktop file and recombobulate

* Wed Dec 03 2025 Nadia P <nyadiia@pm.me> - 0.6.9.1-1
- Initial package
