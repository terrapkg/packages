%define debug_package %nil

Name:			btdu
Version:		0.6.0
Release:		1%?dist
Summary:		Sampling disk usage profiler for btrfs
License:		GPL-2.0-only
URL:			https://github.com/CyberShadow/btdu
Source0:		%url/archive/refs/tags/v%version.tar.gz
# gcc-gdc is built using ldc ironically
# let's just use ldc instead, they have the funny macros
BuildRequires:	dub ldc mold
BuildRequires:	pkgconfig(ncurses)
ExclusiveArch:	%ldc_arches

%description
%summary.

%prep
%autosetup

%build
# see macro _d_optflags
# got rid of -release
export DFLAGS="-O -gc -wi --linker=mold"
dub build -b release --parallel -n -y --compiler=ldmd2 # release-debug doesn't work

%install
install -Dpm755 btdu	-t %buildroot%_bindir
install -Dpm644 btdu.1	-t %buildroot%_mandir/man1

%files
%doc README.md
%license COPYING
%_bindir/btdu
%_mandir/man1/btdu.1.gz

%changelog
* Sun May 05 2024 madonuko <mado@fyralabs.com> - 0.5-1
- Initial package.
