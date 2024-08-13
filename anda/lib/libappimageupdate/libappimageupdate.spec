%global git_commit 0b200115d33257ea0ceab1d03cc25f5b52c6ad77

%global commit_short %(c=%{git_commit}; echo ${c:0:7})

%global libver  2.0.0-alpha-1-20220304.git%{commit_short}

# replace - with ~
%global libver_format %(v=%{libver}; sed 's/-/~/g' <<< $v)

Name:           libappimageupdate

Version:        %{libver_format}
Release:        3%{?dist}
Summary:        AppImageUpdate lets you update AppImages in a decentral way using information embedded in the AppImage itself.

License:        MIT
URL:            https://github.com/AppImageCommunity/AppImageUpdate
#Source0:        %%{url}/archive/refs/%%{libver}.tar.gz
Source0:        %{url}/archive/%{git_commit}.tar.gz

BuildRequires:  make
BuildRequires:  cmake3
BuildRequires:  cpr-devel
BuildRequires:  gcc-c++
BuildRequires:  libappimage-devel curl-devel libX11-devel zlib-devel fuse-devel librsvg2-devel cairo-devel git-core
BuildRequires:  json-devel
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  openssl-devel
BuildRequires:  inotify-tools-devel
BuildRequires:  argagg-devel
BuildRequires:  zsync2-devel

%description
Implements functionality for dealing with AppImage files. It is written in C++ and is using Boost.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n AppImageUpdate-%{git_commit}

%build
# add include path for argagg
%cmake -DBUILD_QT_UI=ON \
    -DBUILD_LIBAPPIMAGEUPDATE_ONLY=ON \
    -DUSE_SYSTEM_LIBAPPIMAGE=ON \
    -DUSE_SYSTEM_ZSYNC2=ON \
    -DCPR_FORCE_USE_SYSTEM_CURL=ON \
    -DUSE_SYSTEM_CPR=ON
%cmake_build


%install
%cmake_install

%{?ldconfig_scriptlets}


%files
%{_libdir}/*.so
%{_libdir}/*.a
# what is this?
%exclude %{_bindir}/validate


%files devel
%{_includedir}/{appimage,cpr,zs*.h}
%{_prefix}/lib/cmake/AppImageUpdate/

%changelog
* Tue Oct 25 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial build
