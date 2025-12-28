%dnl %define debug_package %{nil}

Name:           luamake
Version:        1.7
Release:        1%?dist
License:        MIT
URL:            https://github.com/actboy168/luamake
Source:         https://github.com/actboy168/luamake/archive/refs/tags/v%version.tar.gz
Summary:        A platform independent configuration and build system that uses the standard Lua command-line interpreter

BuildRequires:  gcc-c++ make ninja-build glibc lua gcc cmake libstdc++-devel libstdc++-static libstdc++ libcxx libcxx-devel

%description

%prep
%git_clone

%build
compile/build.sh notest
%ninja_build

%install
install -Dm755 luamake %{buildroot}%{_bindir}/luamake

%files
%license LICENSE
%doc README.md
%{_bindir}/luamake

%changelog
* Sun Dec 28 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
