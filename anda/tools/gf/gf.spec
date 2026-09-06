%global forgeurl https://github.com/nakst/gf

%global commit 1c04ed95d45d49fb4b06cbc620c61acd58818977
%global shortcommit %{sub %{commit} 0 7}
%global commitdate 20251231

%forgemeta

Name:           gf
Version:        0^%{commitdate}.git%{shortcommit}
Release:        2%{?dist}
Summary:        A GDB frontend for Linux

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  libX11-devel
# the build script wants gdb to be installed when it's executed
BuildRequires:  gdb
Requires:       gdb

Packager:       Olivia <git@olivia.sh>

%description
%{summary}.

%prep
%forgeautosetup -p1

%build
export extra_flags="%optflags"
./build.sh

%install
install -Dm 755 gf2 %{buildroot}%{_bindir}/gf2

%files
%license LICENSE
%doc README.md
%{_bindir}/gf2

%changelog
* Sun Jul 19 2026 Olivia <git@olivia.sh> - 0^20251231.git1c04ed9-2
- Update packager

* Thu Feb 19 2026 Olivia <git@olivia.sh>
- Initial package
