%global git_commit 87fb5a0f3c14d3cf35aa6547cc60d099c89ca532

%global commit_short %(c=%{git_commit}; echo ${c:0:7})

%global ver     2.0.0-alpha-1-20230304
%global libver  %ver.git%{commit_short}

# replace - with ~
%global libver_format %(v=%{libver}; sed 's/-/~/g' <<< $v)

Name:           zsync2

Version:        %{libver_format}
Release:        1%{?dist}
Summary:        A rewrite of the advanced file download/sync tool zsync.

License:        Artistic-2.0
URL:            https://github.com/AppImageCommunity/zsync2
#Source0:        %%{url}/archive/refs/%%{libver}.tar.gz
Source0:        %{url}/archive/%{git_commit}.tar.gz

BuildRequires:  make
BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  curl-devel zlib-devel git-core
BuildRequires:  openssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  libssh-devel
BuildRequires:  gtest-devel
BuildRequires:  cpr-devel
BuildRequires:  libgcrypt-devel


%description
A rewrite of the advanced file download/sync tool zsync.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n zsync2-%{git_commit} -p1

%build
export CFLAGS="$CFLAGS -Wno-incompatible-pointer-types"
%cmake -DCPR_FORCE_USE_SYSTEM_CURL=ON \
    -DUSE_SYSTEM_CURL=ON \
    -DUSE_SYSTEM_CPR=ON
%cmake_build


%install
%cmake_install

%{?ldconfig_scriptlets}


%files
%license COPYING
%doc README.md
%{_bindir}/zsync2
%{_bindir}/zsyncmake2
%{_libdir}/*.so*


%files devel
%{_includedir}/*.h
# cmake
%{_libdir}/cmake/zsync2*
# will be packaged separately
%exclude %{_libdir}/pkgconfig/args.pc



%changelog
* Sat Jul 22 2023 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial build
