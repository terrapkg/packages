#? https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=throne-git

Name: throne
Version: 1.0.13
Release: 1%?dist
Summary: Qt based cross-platform GUI proxy configuration manager (backend: sing-box)
URL: https://github.com/throneproj/Throne
License: GPLv3

Obsoletes: nekoray < 4.3.7-2

Source0: https://github.com/throneproj/Throne/archive/refs/tags/%{version}.tar.gz#/throne-%{version}.tar.gz
Packager: bunzuhbu <g89156436@gmail.com>

Source2: Sagernet.SingBox.Version.txt
%define singbox_version $(cat %{SOURCE2})

Source3: %{name}.desktop
Source4: %{name}.sh
Source5: https://raw.githubusercontent.com/throneproj/routeprofiles/rule-set/srslist.h

BuildRequires: rpm_macro(cmake)
BuildRequires: rpm_macro(cmake_build)
BuildRequires: rpm_macro(cmake_install)
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Linguist)
BuildRequires: cmake(Qt6Charts)
BuildRequires: patchelf
BuildRequires: sed
BuildRequires: golang
BuildRequires: rpm_macro(gobuildflags)
BuildRequires: protobuf-compiler
BuildRequires: desktop-file-utils
Requires: %{name}-core
%define core Core

%package core
Summary: %{summary}

%description
%{summary}

%description core
%{summary}

%prep
%autosetup -p1 -n Throne-%{version}
sed -i 's~find_package(Protobuf CONFIG REQUIRED)~find_package(Protobuf REQUIRED)~' cmake/myproto.cmake
sed -i 's~add_library(qhotkey 3rdparty/QHotkey/qhotkey.cpp)~add_library(qhotkey STATIC 3rdparty/QHotkey/qhotkey.cpp)~' cmake/QHotkey.cmake
# sed -i 's~ImageFormat::BGRA~ImageFormat::BGR~' 3rdparty/ZxingQtReader.hpp
pushd core/server
export GOBIN=$(pwd)/gobin
export PATH="${PATH}:${GOBIN}"
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install github.com/chai2010/protorpc/protoc-gen-protorpc@latest

cd gen
protoc -I . --go_out=. --protorpc_out=. libcore.proto

%build
mkdir -p %__cmake_builddir
cp %{S:5} %__cmake_builddir/
%cmake
%cmake_build
DEST=$PWD/%{__cmake_builddir}/%{core}
pushd core/server
export GOBIN=$(pwd)/gobin
export PATH="${PATH}:${GOBIN}"
%define currentgoldflags -w -s -X github.com/sagernet/sing-box/constant.Version=%{singbox_version}
%define gomodulesmode GO111MODULE=on
%define build_ldflags %nil
export GO_LDFLAGS=' '
export GO_BUILDTAGS="with_clash_api with_gvisor with_quic with_wireguard with_utls with_dhcp with_tailscale"
%gobuild -o $DEST -mod=readonly -modcacherw
popd

%install
install -Dm755 %__cmake_builddir/Throne %buildroot%_libdir/%name/%name
install -Dm755 %__cmake_builddir/%core %buildroot%_libdir/%name/%core
install -Dpm755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}
install -Dpm644 %{SOURCE3} %{buildroot}%{_appsdir}/%{name}.desktop
install -Dpm644 res/Throne.ico -t %buildroot%_iconsdir/
install -Dpm644 res/public/Throne.png -t %buildroot%_datadir/pixmaps/
patchelf --remove-rpath %{buildroot}%{_libdir}/%{name}/%{name}
patchelf --remove-rpath %{buildroot}%{_libdir}/%{name}/%{core}

%check
desktop-file-validate %{buildroot}%{_appsdir}/%{name}.desktop

%files
%attr(0755, -, -) %{_bindir}/%{name}
%attr(0755, -, -) %{_libdir}/%{name}/%{name}
%attr(0644, -, -) %{_iconsdir}/Throne.ico
%attr(0644, -, -) %{_appsdir}/%{name}.desktop
%_datadir/pixmaps/Throne.png

%files core
%dir %{_libdir}/%{name}
%attr(0755, -, -) %{_libdir}/%{name}/%{core}

