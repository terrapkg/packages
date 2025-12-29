%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}
Name: nekobox
Version: 5.9.20
Release: 0%{?autorelease}
Summary: Qt based cross-platform GUI proxy configuration manager (backend: sing-box)
URL: https://github.com/qr243vbi/nekobox
License: GPLv3

Source0: %{url}/releases/download/%{version}/nekobox-unified-source-%{version}.tar.xz
Source1: nekobox.desktop
Source2: start.sh

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libcurl)
BuildRequires: cmake(yaml-cpp)
BuildRequires: pkgconfig(openssl)
BuildRequires: cmake(ZXing)
BuildRequires: cmake(absl)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Qml)
BuildRequires: (libboost-devel or boost-devel)
BuildRequires: thrift
BuildRequires: (libthrift-devel or thrift-devel)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Linguist)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: chrpath
BuildRequires: make
BuildRequires: sed
BuildRequires: (ninja or ninja-build)
BuildRequires: golang >= 1.24
Requires: nekobox-core

%define main %{name}
%define core nekobox_core

%package -n nekobox-core
Summary: %{summary}

%description
%{summary}.

%description -n nekobox-core
%{summary}.

%prep
%autosetup -p1 -n nekobox-unified-source-%{version}

%build

(
DEST=$PWD/build
SKIP_UPDATER=y
GOFLAGS='-mod=vendor %{?gobuildflags}'
VERSION_SINGBOX="$(cat SingBox.Version)"
. script/build_go.sh
)

%if %{undefined optflags}
%define optflags -O2 -g -m64 -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables
%endif

(
export INPUT_VERSION="%{version}"
%cmake -DSKIP_UPDATE_BUTTON=ON
%cmake_build
)

%install
(
%cmake_install
)
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons

install -Dm644 %{SOURCE1}   %{buildroot}%{_datadir}/applications/%{main}.desktop
install -Dm755 %{SOURCE2}   %{buildroot}%{_bindir}/%{main}

cp      build/%{core}       %{buildroot}%{_libexecdir}/%{name}/%{core}
echo    "%{version}"      > %{buildroot}%{_libexecdir}/%{name}/public/version.txt
cp      srslist.json        %{buildroot}%{_libexecdir}/%{name}/public/srslist.json

cp      res/%{main}.ico     %{buildroot}%{_datadir}/icons/%{main}.ico
chrpath -d                  %{buildroot}%{_libexecdir}/%{name}/%{main}

sed -i 's~@NAME@~%{name}~g;s~@START@~%{_bindir}/%{main}~g;s~@ICON@~%{_datadir}/icons/%{main}.ico~g;' %{buildroot}%{_datadir}/applications/%{main}.desktop
sed -i 's~@SH@~/bin/sh~g;s~@MAIN@~%{_libexecdir}/%{name}/%{main}~g;' %{buildroot}%{_bindir}/%{main}

%files
%attr(0755, -, -) %{_bindir}/%{main}
%attr(0755, -, -) %{_libexecdir}/%{name}/%{main}
%dir %{_libexecdir}/%{name}/public
%attr(0644, -, -) %{_libexecdir}/%{name}/public/*.*
%attr(0644, -, -) %{_datadir}/icons/%{main}.ico
%attr(0644, -, -) %{_datadir}/applications/%{main}.desktop

%files -n nekobox-core
%dir %{_libexecdir}/%{name}
%caps(cap_net_admin=pe) %attr(0755, -, -) %{_libexecdir}/%{name}/%{core}
