%global gomodulesmode GO111MODULE=on
Name: nekoray
Version: 5.0.2
Release: 1%?dist
Summary: Qt based cross-platform GUI proxy configuration manager (backend: sing-box)
URL: https://github.com/qr243vbi/nekobox
License: GPLv3

Source0: %{url}/releases/download/%{version}/nekobox-unified-source-%{version}.tar.xz
Source1: %{url}/releases/download/%{version}/nekobox-unified-source-%{version}.tar.xz.sha256sum

BuildRequires: rpm_macro(cmake)
BuildRequires: rpm_macro(cmake_build)
BuildRequires: rpm_macro(cmake_install)
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(protobuf)
BuildRequires: pkgconfig(libcurl)
BuildRequires: cmake(yaml-cpp)
BuildRequires: cmake(ZXing)
BuildRequires: cmake(absl)
BuildRequires: cmake(cpr)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Linguist)
BuildRequires: cmake(Qt6Charts)
BuildRequires: patchelf

BuildRequires: sed
BuildRequires: golang > 1.21

%package -n nekobox
Summary: %{summary}
Provides: nekoray = %{version}-%{release}
Requires: nekobox-core
%define main nekobox
%define core nekobox_core

%package -n nekobox-core
Summary: %{summary}

%description
%{summary}.

%description -n nekobox
%{summary}.

%description -n nekobox-core
%{summary}.

%prep
%autosetup -p1 -n nekobox-unified-source-%{version}

%build
%{?!__builddir:%define __builddir build}
%{?!__cmake_builddir:%define __cmake_builddir %__builddir}

(
DEST=$PWD/%{__cmake_builddir}
GOARCH=""
GOOS=darwin
GOFLAGS='-mod=vendor %{?gobuildflags}'
VERSION_SINGBOX="$(cat SingBox.Version)"
. script/build_go.sh

)

(
export CXXFLAGS="$CXXFLAGS -Wno-error=return-type"
export CFLAGS="$CFLAGS -Wno-error=return-type"
%cmake
%cmake_build
)

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons

cat << EOF > %{buildroot}%{_bindir}/%{main}
#!%{_bindir}/sh
%{_libdir}/%{name}/%{main} -appdata "${@}"
EOF

cat << EOF > %{buildroot}%{_datadir}/applications/%{main}.desktop
[Desktop Entry]
Version=1.0
Terminal=false
Type=Application
Name=%{main}
Categories=Network;
Comment=Qt based cross-platform GUI proxy configuration manager (backend: sing-box)
Comment[zh_CN]=基于 Qt 的跨平台代理配置管理器 (后端 sing-box)
Keywords=Internet;VPN;Proxy;sing-box;
Exec=%{_bindir}/%{main}
Icon=%{_datadir}/icons/%{main}.ico
EOF

cp %{__cmake_builddir}/%{main} %{buildroot}%{_libdir}/%{name}/%{main}
cp %{__cmake_builddir}/%{core} %{buildroot}%{_libdir}/%{name}/%{core}
cp res/%{main}.ico %{buildroot}%{_datadir}/icons/%{main}.ico
patchelf --remove-rpath %{buildroot}%{_libdir}/%{name}/%{main}

%files -n nekobox
%attr(0755, -, -) %{_bindir}/%{main}
%attr(0755, -, -) %{_libdir}/%{name}/%{main}
%attr(0644, -, -) %{_datadir}/icons/%{main}.ico
%attr(0644, -, -) %{_datadir}/applications/%{main}.desktop

%files -n nekobox-core
%dir %{_libdir}/%{name}
%attr(0755, -, -) %{_libdir}/%{name}/%{core}

