%global debug_package   %{nil}

%global ver 5.0.0

%global commit          a9cd1c86bdd6a231fc2b07c3b7a2505175a864d3
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20260824

Name:   	umbriel-nightly
Version:	%{ver}^%{commitdate}git.%{shortcommit}
Release:	1%{?dist}
Summary:	A work-in-progress Wayland compositor designed for daily use, with scrolling and dwindle layouts, per-output workspaces, window rules, blur, shadows, and fluid animations

License:	MIT
URL:		https://github.com/noctalia-dev/umbriel
Source0:	https://github.com/noctalia-dev/umbriel/archive/%{commit}/umbriel-%{commit}.tar.gz

BuildRequires:  wlroots-devel >= 0.20
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  sdbus-cpp-devel
BuildRequires:  tomlplusplus-devel
BuildRequires:  json-devel
BuildRequires:  md4c-devel
BuildRequires:  stb-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(scenefx-0.5)
BuildRequires:  pkgconfig(cairo)

Requires:       xwayland-satellite

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%{Summary}.

%prep
%autosetup -n umbriel-%{commit}

# Manually insert commit hash
sed -i "s/'unknown'/'%{shortcommit}'/g" meson.build

%conf
%meson -Duse_system_scenefx

%build
%meson_build

%install
%meson_install --skip-subprojects
install -d %{buildroot}%{_licensedir}/%{name}/third_party
find third_party -type f \( -name "LICENSE*" -o -name "COPYING*" -o -name "NOTICE*" \) | while read -r file; do
    # Create the destination subdirectory
    dest_dir="%{buildroot}%{_licensedir}/%{name}/$(dirname "$file")"
    install -d "$dest_dir"
    # Copy the file to its specific subfolder
    install -p -m 0644 "$file" "$dest_dir/"
done

%check
%desktop_file_validate %{buildroot}%{_appsdir}/dev.noctalia.Noctalia.desktop

%files
%doc README.md
%license LICENSE
%{_licensedir}/%{name}/third_party/
%{_bindir}/noctalia
%{_datadir}/noctalia/

%changelog
* Mon Aug 03 2026 Cypress Reed <cypress@fyralabs.com>
- Update description and summary per developer's request

* Thu Jul 16 2026 Cypress Reed <cypress@fyralabs.com>
- Add conflicts with noctalia

* Thu Jul 09 2026 Cypress Reed <cypress@fyralabs.com>
- Noctalia requires system libraries now, so remove the meson options

* Wed Jul 01 2026 Cypress Reed <cypress@fyralabs.com>
- Add md4c as a system library
- Add wireplumber build requirement

* Tue Jun 30 2026 Cypress Reed <cypress@fyralabs.com>
- Add tomlplusplus as a sytem library

* Wed Jun 24 2026 Cypress Reed <cypress@fyralabs.com>
- Add desktop file and icon

* Fri Jun 05 2026 Cypress Reed <cypress@fyralabs.com>
- Port to terra from Fedora COPR lionheartp/Hyprland
