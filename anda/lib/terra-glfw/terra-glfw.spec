Name:           terra-glfw
%global cleanarch %(echo %{_arch} | sed 's/_/-/g')
%global _default_patch_fuzz 3
Version:        3.4
Release:        2%{?dist}
Epoch:          1
Summary:        A multi-platform library for OpenGL, OpenGL ES, Vulkan, window and input (wayland, patched for Minecraft)
License:        Zlib
URL:            https://github.com/BoyOrigin/glfw-wayland
Obsoletes:      glfw <= %{version}
Provides:       glfw = %{epoch}:%{version}-%{release}
Provides:       glfw(%{cleanarch}) = %{epoch}:%{version}-%{release}
Conflicts:      glfw
Packager:      Cappy Ishihara <cappy@fyralabs.com>
Source0:       https://github.com/glfw/glfw/archive/%{version}/glfw-%{version}.tar.gz
Patch1:        0001-Key-Modifiers-Fix.patch
Patch2:        0002-Fix-duplicate-pointer-scroll-events.patch
Patch3:        0003-Implement-glfwSetCursorPosWayland.patch
Patch4:        0004-Fix-Window-size-on-unset-fullscreen.patch
Patch5:        0005-Implement-glfwSetWindowIcon.patch
Patch6:        0006-Fix-fullscreen-location.patch
Patch7:        0007-Fix-forge-crash.patch

Supplements:   prismlauncher
Supplements:   minecraft-launcher

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)

BuildRequires:  extra-cmake-modules
BuildRequires:  libxkbcommon-devel
BuildRequires:  vulkan-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

%description
GLFW is a multi-platform library for OpenGL, OpenGL ES, Vulkan, window and input.

This is a fedora port of the AUR package under the same name.
It fixes various issues when using this library with minecraft on wayland.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig(dri)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xi)
Requires:       pkgconfig(xinerama)
Requires:       pkgconfig(xrandr)

%description devel
The glfw-devel package contains header files for developing glfw
applications.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation for developing applications
with %{name}.


%prep
%autosetup -n glfw-%{version} -p1

%build
%cmake
%cmake_build --target all

%install
%cmake_install

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libglfw.so.3*

%files devel
%{_includedir}/GLFW/
%{_libdir}/libglfw.so
%{_libdir}/pkgconfig/glfw3.pc
%{_libdir}/cmake/glfw3/

%files doc
%doc %{_docdir}/GLFW/

%changelog
%autochangelog
