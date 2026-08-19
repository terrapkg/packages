%global commit a038194566187f5df282c5fd551bf60ed745b9d6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260723

Name:           libmemscan
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Zig rewrite of scanmem, a Linux memory scanner library
License:        LGPL-3.0-or-later
URL:            https://github.com/brkzlr/libmemscan
Packager:       madonuko <mado@fyralabs.com>
Source0:        %url/archive/%commit/%name-%commit.tar.gz
BuildRequires:  zig

%description
A Zig rewrite of a PINCE specialized fork of scanmem.

Made for PINCE in mind but usable for other purposes as well.

%prep
%autosetup -n %name-%commit
%zig_prep

%build

%install
# When DNF supports microarchitectures the fallback option for -c can be used here instead
%ifarch x86_64
%{zig_install_target -r fast -Cx86_64_v2 -s}
%elifarch aarch64
%{zig_install_target -r fast -s}
%endif

%files
%doc README.md
%license LICENSE.txt
%_libdir/%name.so

%changelog
* Wed Aug 19 2026 madonuko <mado@fyralabs.com> - 0~20260723git.a038194-1
- Initial package
