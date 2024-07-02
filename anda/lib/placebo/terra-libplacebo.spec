Name:           terra-libplacebo
Version:        7.349.0
Release:        1%?dist
Summary:        Reusable library for GPU-accelerated video/image rendering primitives

License:        LGPLv2+
URL:            https://github.com/haasn/libplacebo
Source0:        %{url}/archive/v%{version}%{?prerelease}/libplacebo-%{version}%{?prerelease}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  glad2 >= 2.0.0
BuildRequires:  lcms2-devel
BuildRequires:  libdovi-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libunwind-devel
BuildRequires:  libshaderc-devel >= 2018.0-1
BuildRequires:  python3-mako
BuildRequires:  spirv-tools-devel
BuildRequires:  vulkan-devel
BuildRequires:  glslang-devel
BuildRequires:  xxhash-devel


%description
libplacebo is essentially the core rendering algorithms and ideas of
mpv turned into a library. This grew out of an interest to accomplish
the following goals:

- Clean up mpv's internal API and make it reusable for other projects.
- Provide a standard library of useful GPU-accelerated image processing
  primitives based on GLSL, so projects like VLC or Firefox can use them
  without incurring a heavy dependency on `libmpv`.
- Rewrite core parts of mpv's GPU-accelerated video renderer on top of
  redesigned abstractions. (Basically, I wanted to eliminate code smell
  like `shader_cache.c` and totally redesign `gpu/video.c`)


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n libplacebo-%{version}%{?prerelease}


%build
%meson \
 -Dd3d11=disabled \
 -Ddemos=False

%meson_build


%install
%meson_install


%ldconfig_scriptlets


%files
%license LICENSE
%doc README.md
%{_libdir}/libplacebo.so.338

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libplacebo.pc


%changelog
%autochangelog
