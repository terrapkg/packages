%define debug_package %{nil}
%global _build_id_links none

%global __requires_exclude libffmpeg.so|libvk_swiftshader.so|libvulkan.so|libEGL.so|libGLESv2.so
%global __provides_exclude_from /opt/%{name}/.*\\.so

Name:           helium-browser
Version:        0.6.9.1
Release:        1%{?dist}
Summary:        Private, fast, and honest web browser based on Chromium

URL:            https://helium.computer
License:        GPL-3.0-only AND BSD-3-Clause

Source0:        https://github.com/imputnet/helium-linux/releases/download/%{version}/helium-%{version}-x86_64_linux.tar.xz
Source1:        https://github.com/imputnet/helium-linux/releases/download/%{version}/helium-%{version}-arm64_linux.tar.xz

ExclusiveArch:  x86_64 aarch64

Requires:       xdg-utils
Requires:       liberation-fonts

Packager:       Nadia P <nyadiia@pm.me>

%description
Private, fast, and honest web browser based on Chromium.
Based on ungoogled-chromium with additional privacy and usability improvements.

%prep
%ifarch x86_64
%autosetup -n helium-%{version}-x86_64_linux
%endif
%ifarch aarch64
%autosetup -n helium-%{version}-arm64_linux -T -b 1
%endif

sed -i \
    -e 's/Exec=chromium/Exec=helium-browser/' \
    -e 's/Name=Helium$/Name=Helium Browser/' \
    -e 's/Icon=helium/Icon=helium-browser/' \
    helium.desktop

%build

%install
install -dm755 %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}/

sed -i 's/exists_desktop_file || generate_desktop_file/true/' \
    %{buildroot}/opt/%{name}/chrome-wrapper

install -Dm644 helium.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -Dm644 %{buildroot}/opt/%{name}/product_logo_256.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm644 %{buildroot}/opt/%{name}/product_logo_256.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

install -dm755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
set -euo pipefail

XDG_CONFIG_HOME="\${XDG_CONFIG_HOME:-\"\$HOME/.config\"}"

SYS_CONF="%{_sysconfdir}/helium-browser-flags.conf"
USR_CONF="\${XDG_CONFIG_HOME}/helium-browser-flags.conf"

FLAGS=()

append_flags_file() {
    local file="\$1"
    [[ -r "\$file" ]] || return 0
    local line safe_line
    while IFS= read -r line; do
        [[ "\$line" =~ ^[[:space:]]*(#|\$) ]] && continue
        case "\$line" in
            *'\$('*|*'\`'*)
                echo "Warning: ignoring unsafe line in \$file: \$line" >&2
                continue
                ;;
        esac
        set -f
        safe_line=\${line//\$/\\\\\$}
        safe_line=\${safe_line//~/\\\\~}
        eval "set -- \$safe_line"
        set +f
        for token in "\$@"; do
            FLAGS+=("\$token")
        done
    done < "\$file"
}

append_flags_file "\$SYS_CONF"
append_flags_file "\$USR_CONF"

if [[ -n "\${HELIUM_USER_FLAGS:-}" ]]; then
    read -r -a ENV_FLAGS <<< "\$HELIUM_USER_FLAGS"
    FLAGS+=("\${ENV_FLAGS[@]}")
fi

exec /opt/helium-browser/chrome-wrapper "\${FLAGS[@]}" "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

%files
/opt/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
* Wed Dec 03 2025 Nadia P <nyadiia@pm.me> - 0.6.9.1-1
- Initial package
