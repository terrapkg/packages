# https://ziglang.org/download/VERSION/release-notes.html#Support-Table
%global         zig_arches x86_64 aarch64 riscv64 %{mips64}
# Signing key from https://ziglang.org/download/
%global         public_key RWSGOq2NVecA2UPNdBUZykf1CCb147pkmdtYxgb3Ti+JO/wCYvhbAb/U
# Not needed yet
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 9
%define         llvm_compat 20
%endif
%global         llvm_version 20.0.0
%global         ver 0.15.0-dev.919+044ccf413
%bcond bootstrap 1
%bcond docs      %{without bootstrap}
%bcond test      1
%global zig_cache_dir %{builddir}/zig-cache
%global zig_build_options %{shrink: \
    --verbose \
    --release=fast \
    --summary all \
    \
    -Dtarget=native \
    -Dcpu=baseline \
    --zig-lib-dir lib \
    --build-id=sha1 \
    \
    --cache-dir "%{zig_cache_dir}" \
    --global-cache-dir "%{zig_cache_dir}" \
    \
    -Dversion-string="%(v=%{ver}; echo ${v:0:6})" \
    -Dstatic-llvm=false \
    -Denable-llvm=true \
    -Dno-langref=true \
    -Dstd-docs=false \
    -Dpie \
    -Dconfig_h="%{__cmake_builddir}/config.h" \
}
%global zig_install_options %zig_build_options %{shrink: \
    --prefix "%{_prefix}" \
}

Name:           zig-master-bootstrap
Version:        %(echo %{ver} | sed 's/-/~/g')
Release:        1%?dist
Summary:        Boostrap builds for Zig.
License:        MIT AND NCSA AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later AND GPL-2.0-or-later WITH GCC-exception-2.0 AND BSD-3-Clause AND Inner-Net-2.0 AND ISC AND LicenseRef-Fedora-Public-Domain AND GFDL-1.1-or-later AND ZPL-2.1
URL:            https://ziglang.org
Source0:        %{url}/builds/zig-%{ver}.tar.xz
Source1:        %{url}/builds/zig-%{ver}.tar.xz.minisig
Patch0:         0000-remove-native-lib-directories-from-rpath.patch
Patch3:         0005-link.Elf-add-root-directory-of-libraries-to-linker-p.patch
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  llvm-devel
BuildRequires:  clang-devel
BuildRequires:  lld-devel
BuildRequires:  zlib-devel
# for man page generation
BuildRequires:  help2man
# for signature verification
BuildRequires:  minisign
%if %{without bootstrap}
BuildRequires:  %{name} = %{version}
%endif
%if %{with test}
BuildRequires:  elfutils-libelf-devel
BuildRequires:  libstdc++-static
%endif
Requires:       %{name}-libs = %{version}
# Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
Provides:       bundled(compiler-rt) = %{llvm_version}
# LGPL-2.1-or-later AND SunPro AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later WITH GNU-compiler-exception AND GPL-2.0-only AND ISC AND LicenseRef-Fedora-Public-Domain AND HPND AND CMU-Mach AND LGPL-2.0-or-later AND Unicode-3.0 AND GFDL-1.1-or-later AND GPL-1.0-or-later AND FSFUL AND MIT AND Inner-Net-2.0 AND X11 AND GPL-2.0-or-later WITH GCC-exception-2.0 AND GFDL-1.3-only AND GFDL-1.1-only
Provides:       bundled(glibc) = 2.41
# Apache-2.0 WITH LLVM-exception OR MIT OR NCSA
Provides:       bundled(libcxx) = %{llvm_version}
# Apache-2.0 WITH LLVM-exception OR MIT OR NCSA
Provides:       bundled(libcxxabi) = %{llvm_version}
# NCSA
Provides:       bundled(libunwind) = %{llvm_version}
# BSD, LGPG, ZPL
Provides:       bundled(mingw) = 3839e21b08807479a31d5a9764666f82ae2f0356
# MIT
Provides:       bundled(musl) = 1.2.5
# Apache-2.0 WITH LLVM-exception AND Apache-2.0 AND MIT AND BSD-2-Clause
Provides:       bundled(wasi-libc) = d03829489904d38c624f6de9983190f1e5e7c9c5
Conflicts:      zig
ExclusiveArch:  %{zig_arches}
Packager:       Gilver E. <rockgrub@disroot.org>

%description
Zig is an open source alternative to C. 
This package provides the bootstrap to build full "prerelease"/master builds of Zig.
It is not recommended to use this build on its own.

# The Zig stdlib only contains uncompiled code
%package libs
Summary:        Zig Standard Library
Conflicts:      zig-libs
BuildArch:      noarch

%description libs
Zig Standard Library

%prep
/usr/bin/minisign -V -m %{SOURCE0} -x %{SOURCE1} -P %{public_key}
%autosetup -p1 -n zig-%{ver}
%if %{without bootstrap}
# Ensure that the pre-build stage1 binary is not used
rm -f stage1/zig1.wasm
%endif

%build
# zig doesn't know how to dynamically link llvm on its own so we need cmake to generate a header ahead of time
# if we provide the header we need to also build zigcpp

# C_FLAGS: wasm2c output generates a lot of noise with -Wunused.
# EXTRA_BUILD_ARGS: explicitly specify a build-id
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
    -DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING="-DNDEBUG -Wno-unused" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="-DNDEBUG -Wno-unused" \
    \
    -DZIG_EXTRA_BUILD_ARGS:STRING="--verbose;--build-id=sha1" \
    -DZIG_SHARED_LLVM:BOOL=true \
    -DZIG_PIE:BOOL=true \
    \
    -DZIG_TARGET_MCPU:STRING=baseline \
    -DZIG_TARGET_TRIPLE:STRING=native \
    \
    -DZIG_VERSION:STRING="%(v=%{ver}; echo ${v:0:6})"

%if %{with bootstrap}
%cmake_build --target stage3
%else
%cmake_build --target zigcpp
zig build %{zig_build_options}

# Zig has no official manpage
# https://github.com/ziglang/zig/issues/715
help2man --no-discard-stderr --no-info "./zig-out/bin/zig" --version-option=version --output=zig.1
%endif


%if %{with docs}
# Use the newly made stage 3 compiler to generate docs
# Zig has an extremely annoying issue with transitive failures when trying to build the docs, retry until it succeeds
max=3
attempt=1
while ./zig-out/bin/zig build docs \
    --verbose \
    --global-cache-dir "%{zig_cache_dir}" \
    -Dversion-string="%(v=%{ver}; echo ${v:0:6})"; [[ $? -ne 0 ]];
do
  echo "Transitive failure. Trying again."

  if [[ $attempt -eq $max ]]
  then
    break
  fi

  sleep 1
  ((attempt++))  
done
%endif

%install
%if %{with bootstrap}
%cmake_install
%else
DESTDIR="%{buildroot}" zig build install %{zig_install_options}

install -Dpm644 zig.1 -t %{buildroot}%{_mandir}/man1/ 
%endif

%if %{with test}
%check
# Run reduced set of tests, based on the Zig CI
"%{buildroot}%{_bindir}/zig" test test/behavior.zig -Itest
%endif

%files
%license LICENSE
%{_bindir}/zig
%if %{without bootstrap}
%{_mandir}/man1/zig.1.*
%endif

%files libs
%{_prefix}/lib/zig

%if %{with docs}
%files doc
%doc README.md
%doc zig-out/doc/langref.html
%doc zig-out/doc/std
%endif

%changelog
* Sat May 10 2025 Gilver E. <rockgrub@disroot.org> - 0.15.0~dev.482+2c241b263-2
- Added GCC runtime dependency to pass system information to Zig
* Fri Apr 25 2025 Gilver E. <rockgrub@disroot.org> - 0.15.0~dev.384+c06fecd46-2
- Ported Fedora Zig patches
* Wed Apr 23 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
