%global gcc_major 13

Name:           cuda-gcc
Version:        13.3.1
Release:        2%{?dist}
Summary:        GNU Compiler Collection CUDA compatibility package
License:        BSD
URL:            http://gcc.gnu.org

BuildArch:      noarch

Requires:       gcc%{gcc_major}-c++

Provides:       cuda-gcc = %{version}-%{release}
Obsoletes:      cuda-gcc < %{version}-%{release}
Provides:       cuda-gcc-c++ = %{version}-%{release}
Obsoletes:      cuda-gcc-c++ < %{version}-%{release}
Provides:       cuda-gcc-gfortran = %{version}-%{release}
Obsoletes:      cuda-gcc-gfortran < %{version}-%{release}

%description
The %{name} package contains scripts that are sourced in the environment to use
the GCC compatibility packages when invoking NVCC.

%install
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/

cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh <<EOF
export NVCC_CCBIN='g++-%{gcc_major}'

# Alternatively you can use the following:
export NVCC_PREPEND_FLAGS='-ccbin %{_bindir}/g++-%{gcc_major}'
EOF

cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh <<EOF
setenv NVCC_CCBIN 'g++-%{gcc_major}'

# Alternatively you can use the following:
setenv NVCC_PREPEND_FLAGS '-ccbin %{_bindir}/g++-%{gcc_major}'
EOF

%files
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.csh
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh

%changelog
%autochangelog
