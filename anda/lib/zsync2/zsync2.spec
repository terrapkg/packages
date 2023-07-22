%global git_commit 1608115705047d6826bcd7b35a6988deaf3dbfec

%global commit_short %(c=%{git_commit}; echo ${c:0:7})

%global libver  2.0.0-alpha-1-20220304.git%{commit_short}

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
%autosetup -n zsync2-%{git_commit}

git init .
git remote add origin %{url}
git fetch origin
git checkout %{git_commit} --force
git pull origin %{git_commit} --force
git submodule update --init --recursive

%build

%cmake -DCPR_FORCE_USE_SYSTEM_CURL=ON \
    -DUSE_SYSTEM_CURL=ON \
    -DUSE_SYSTEM_CPR=ON
%cmake_build


%install
%cmake_install

%{?ldconfig_scriptlets}


%files
%{_libdir}/*.so
%{_libdir}/*.a


%files devel
/usr/lib/debug/usr/bin/zsync*.debug
/usr/lib64/cmake/zsync2/zsync2Config.cmake
/usr/lib64/cmake/zsync2/zsync2ConfigVersion.cmake
/usr/lib64/cmake/zsync2/zsync2Targets-debug.cmake
/usr/lib64/cmake/zsync2/zsync2Targets.cmake

%changelog
* Sat Jul 22 2023 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial build
