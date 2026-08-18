%global debug_package %{nil}

Name:           inputactions
Version:        0.9.0
Release:        1%{?dist}
Summary:        Linux utility for binding keyboard. mouse, touchpad and touchscreen actions to system actions
License:        GPL-3.0-or-later
URL:            https://wiki.inputactions.org/main/
Source0:        https://github.com/taj-ny/InputActions/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake-rpm-macros
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  yaml-cpp-devel
BuildRequires:  kwin-devel
BuildRequires:  kf6-kcmutils-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  cmake(CLI11)
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%git_clone https://github.com/taj-ny/InputActions.git %{version}
sed -i '1i #include <unistd.h>' \
    kwin/lib/core/lib/libevdev-cpp/src/libevdev-cpp/Device.cpp \
    kwin/lib/core/src/libinputactions/interfaces/implementations/FileConfigProvider.cpp

%conf
%cmake \
    -DINPUTACTIONS_BUILD_KWIN=ON # \
    # -DINPUTACTIONS_BUILD_CTL=ON

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE


%changelog
* Fri Jul 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
