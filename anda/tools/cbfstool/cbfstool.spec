Name:           cbfstool
Version:        25.03
Release:        2%?dist
Summary:        Management utility for CBFS formatted ROM images
URL:            https://doc.coreboot.org/lib/fw_config.html#cbfs
License:        GPLv2
BuildRequires:  gcc g++ gcc-gnat make cmake ncurses-devel iasl anda-srpm-macros
%if 0%{?fedora} >= 42
BuildRequires: gcc14 gcc14-c++
%endif
Requires:       glibc
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Management utility for CBFS formatted ROM images.

%prep
%git_clone https://review.coreboot.org/coreboot.git %version

%build
%if 0%{?fedora} >= 42
export CC=gcc-14
export CXX=g++-14
%endif
%make_build -C util/cbfstool

%install
install -Dm 777 util/cbfstool/cbfstool %buildroot%_bindir/cbfstool

%files
/usr/bin/cbfstool

%changelog
* Wed Apr 02 2025 Owen Zimmerman <owen@fyralabs.com>
- Add macros and specify fedora version release exports
* Sun Aug 25 2024 Owen Zimmerman <owen@fyralabs.com>
- Initial Package
