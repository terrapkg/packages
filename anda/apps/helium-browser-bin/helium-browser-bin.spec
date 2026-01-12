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
Version:        0.7.10.1
Release:        1%?dist
Summary:        Private, fast, and honest web browser based on Chromium

URL:            https://helium.computer
License:        GPL-3.0-only AND BSD-3-Clause

Source0:        https://github.com/imputnet/helium-linux/releases/download/%{version}/helium-%{version}-%{arch}_linux.tar.xz
Source1:        https://github.com/imputnet/helium-linux/archive/refs/tags/%{version}.tar.gz
Source2:        net.imput.helium.metainfo.xml

ExclusiveArch:  x86_64 aarch64

BuildRequires:  terra-appstream-helper

Requires:       xdg-utils
Requires:       liberation-fonts

Packager:       Nadia P <nyadiia@pm.me>

%description
Private, fast, and honest web browser based on Chromium.
Based on ungoogled-chromium with additional privacy and usability improvements.

%prep
%autosetup -n helium-%{version}-%{arch}_linux
tar --strip-components=1 -zxvf %{SOURCE1}

sed -i 's/Exec=helium\b/Exec=helium-browser-bin/g' helium.desktop

%build

%install
install -dm755 %{buildroot}%{_libdir}/%{name}
cp -a * %{buildroot}%{_libdir}/%{name}/

sed -i 's/exists_desktop_file || generate_desktop_file/true/' \
    %{buildroot}%{_libdir}/%{name}/chrome-wrapper

install -Dm644 helium.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 product_logo_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{appid}.png

rm -f %{buildroot}%{_libdir}/%{name}/helium.desktop
rm -f %{buildroot}%{_libdir}/%{name}/product_logo_256.png

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

exec %{_libdir}/%{name}/chrome-wrapper "\${FLAGS[@]}" "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

%terra_appstream -o %{SOURCE2}

%files
%doc README.md
%license LICENSE LICENSE.ungoogled_chromium
%{_libdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{appid}.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Dec 03 2025 Nadia P <nyadiia@pm.me> - 0.6.9.1-1
- Initial package
