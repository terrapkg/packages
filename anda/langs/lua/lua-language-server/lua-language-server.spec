%define debug_package %{nil}

Name:           lua-language-server
Version:        3.17.1
Release:        1%?dist
License:        MIT
URL:            https://luals.github.io/
Source:         https://github.com/LuaLS/lua-language-server/archive/refs/tags/%version.tar.gz
Summary:        A language server that offers Lua language support

BuildRequires:  gcc-c++ make ninja-build glibc lua gcc cmake libstdc++-devel libstdc++-static libcxx libcxx-devel

%description
A language server that offers Lua language support - programmed in Lua.

%prep
%git_clone https://github.com/LuaLS/lua-language-server.git %{version}

%build
# The funny
chmod +x make.sh
./make.sh

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/
install -Dm755 bin/lua-language-server %{buildroot}%{_libexecdir}/%{name}/%{name}
install -Dm644 bin/main.lua            %{buildroot}%{_libexecdir}/%{name}/main.lua
install -Dm644 debugger.lua            %{buildroot}%{_libexecdir}/%{name}/debugger.lua
cp -av \
    debugger.lua \
    main.lua \
    locale \
    script \
    meta \
    %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/

%changelog
* Sun Dec 28 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
