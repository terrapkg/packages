%define debug_package %{nil}
# no matter what i did build makes no debug info

Name:           open-wallpaper-engine
Version:        0.4.1
Release:        1%{?dist}
License:        GPL-2.0-only
Summary:        Open source wallpaper engine implement mostly for linux
URL:            https://github.com/waywallen/open-wallpaper-engine
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake >= 4.0
BuildRequires:  lito >= 0.3.0
BuildRequires:  clang >= 22
BuildRequires:  ninja-build
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  cef-devel
BuildRequires:  quickjs-ng-devel
BuildRequires:  waywallen-devel
BuildRequires:  waywallen-libs
BuildRequires:  glslang

Requires:       cef

Packager:       L1oly <lid2011@ukr.net>

%description
%{summary}.

%package -n      waywallen-%{name}
Summary:         %{summary} (waywallen plugin)
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires:        waywallen
Supplements:     (%{name} and waywallen)
%description -n  waywallen-%{name}
%{description}

%prep
%autosetup
mkdir -p .lito
cat > .lito/config.toml <<'EOF'
[tools.cmake.overrides.Eigen3]
source = "installed"

[tools.cmake.overrides.glslang]
source = "installed"

[tools.cmake.overrides.qjs]
source = "installed"

[tools.cmake.overrides.CEF]
source = "installed"
EOF

%build
OWE_WAYWALLEN_PLUGIN_BUNDLE_LAYOUT=ON
lito build -p owe-waywallen-plugin --profile release

%install
lito install -p owe-waywallen-plugin --prefix %{buildroot}%{_prefix} --profile release
ln -sf ./weweb/owe-web %{buildroot}%{_bindir}/owe-web

%files
%license LICENSE
%doc README.md
%{_bindir}/owe-web
%{_bindir}/owe-scene
%{_bindir}/weweb/owe-web

%files -n waywallen-%{name}
%{_datadir}/waywallen/plugins/org.waywallen.open-wallpaper-engine

%changelog
* Sat Nov 28 2026 L1oly <lid2011@ukr.net>
- Spilt packages cuz standalone binaries where added

* Thu Oct 29 2026 L1oly <lid2011@ukr.net>
- Initial commit
