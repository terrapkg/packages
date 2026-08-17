Name:           ananicy-cpp
Release:        1%{?dist}
Version:	    1.2.0
Summary:        Rewrite of ananicy in c++ for lower cpu and memory usage
License:        GPL-3.0-or-later
URL:            https://gitlab.com/ananicy-cpp/ananicy-cpp
Source0:        %{url}/-/archive/v%{version}/ananicy-cpp-v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  bpftool
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  json-devel
BuildRequires:  libbpf-devel
BuildRequires:  ninja-build
BuildRequires:  spdlog-devel
BuildRequires:  systemd-devel

Requires:       elfutils-libelf
Requires:       fmt
Requires:       libbpf
Requires:       spdlog
Requires:       systemd
Requires:       systemd-libs
Requires:       zlib-ng-compat
Recommends:     cachyos-ananicy-rules

%description
%{summary}.

%prep
%autosetup -n ananicy-cpp-v%{version}

%conf
%cmake \
    -GNinja \
    -DENABLE_SYSTEMD=ON \
    -DUSE_BPF_PROC_IMPL=ON \
    -DBPF_BUILD_LIBBPF=OFF \
    -DUSE_EXTERNAL_FMTLIB=ON \
    -DUSE_EXTERNAL_JSON=ON \
    -DUSE_EXTERNAL_SPDLOG=ON \
    -DCMAKE_CXX_FLAGS="%{build_cxxflags} -include unistd.h" \
    -DVERSION=%{version}

%build
%cmake_build --target %{name}

%install
%cmake_install --component Runtime

%post
%systemd_user_post ananicy-cpp.service

%preun
%systemd_user_preun ananicy-cpp.service

%postun
%systemd_user_postun_with_restart ananicy-cpp.service

%files
%license LICENSE
%doc README.md
%{_bindir}/ananicy-cpp
%{_unitdir}/ananicy-cpp.service

%changelog
* Thu Jul 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
