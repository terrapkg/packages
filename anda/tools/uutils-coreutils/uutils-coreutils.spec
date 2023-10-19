Name:			uutils-coreutils
Version:		0.0.22
Release:		1%?dist
Summary:		Cross-platform Rust rewrite of the GNU coreutils
License:		MIT
URL:			https://github.com/uutils/coreutils
Source0:		%url/archive/refs/tags/%version.tar.gz
Requires:		glibc gcc-devel
BuildRequires:	cargo make gcc-c++

%description
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

%prep
%autosetup -n coreutils-%version

%build
%make_build PROFILE=release

%install
%make_install PREFIX=%buildroot%_prefix MANDIR=%buildroot%_mandir/man1 PROFILE=release MULTICALL=y

%files
%doc README.md
%license LICENSE

%changelog
%autochangelog
