%global forgeurl https://github.com/nakst/gf

%global commit 9a5dbcc90dc9ca9580f6ce2854cd67e2e507b0c1
%global shortcommit %{sub %{commit} 0 7}
%global commitdate 20251231

%forgemeta

Name:           gf
Version:        0^%{commitdate}.git%{shortcommit}
Release:        1%{?dist}
Summary:        A GDB frontend for Linux

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         01-fix-designated-initializers.patch

BuildRequires:  gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  libX11-devel
# the build script wants gdb to be installed when it's executed
BuildRequires:  gdb
Requires:       gdb

Packager:       metcya <metcya@gmail.com>

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
* Thu Feb 19 2026 metcya <metcya@gmail.com>
- Initial package
