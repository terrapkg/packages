%define debug_package %{nil}

Name:           luamake
Version:        1.7
Release:        1%?dist
License:        MIT
URL:            https://github.com/actboy168/luamake
Source:         https://github.com/actboy168/luamake/archive/refs/tags/v%version.tar.gz
Summary:        A platform independent configuration and build system that uses the standard Lua command-line interpreter

BuildRequires:  gcc-c++ make ninja-build glibc lua gcc cmake libstdc++-devel libstdc++-static libcxx libcxx-devel

%description
%summary.

%prep
%git_clone
sed -i 's|-O2 -Wall |%{build_cflags}|g' compile/ninja/linux.ninja
sed -i 's|-lstdc++ |%{build_ldflags} -lstdc++ |g' compile/ninja/linux.ninja

%build
%{ninja_build} -f compile/ninja/linux.ninja notest

%install
mkdir -p %{buildroot}%{_bindir}
ln -sf %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm755 luamake -t %{buildroot}%{_datadir}/%{name}
install -Dm755 main.lua -t %{buildroot}%{_datadir}/%{name}
cp -r scripts -t %{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/luamake
%{_datadir}/%{name}/%{name}
%{_datadir}/%{name}/main.lua
%{_datadir}/%{name}/scripts/

%changelog
* Sun Dec 28 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
