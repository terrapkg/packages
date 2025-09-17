Name:			bup
Version:		0.33.9
Release:		1%?dist
Summary:		Efficient backup system based on the git packfile format
License:		LGPL-2.0-only
URL:			https://bup.github.io
Source0:		https://github.com/bup/bup/archive/refs/tags/%version.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(libacl)

%description
bup is a program that backs things up. It's short for "backup." Can you believe that nobody else has named an open source program "bup" after all this time? Me neither.

%prep
%autosetup

%build
./configure
%make_build

%install
%make_install

%files
%doc README.md DESIGN.md HACKING.md
%license LICENSE
