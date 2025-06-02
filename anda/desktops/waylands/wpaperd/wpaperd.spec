%bcond check 0

Name:           wpaperd
Version:        1.2.2
Release:        2%?dist
Summary:        Modern wallpaper daemon for Wayland
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND (CC0-1.0 OR Artistic-2.0) AND GPL-3.0+ AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR NCSA) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
SourceLicense:  GPL-3.0-or-later
URL:            https://github.com/danyspin97/wpaperd
Source0:		%url/archive/refs/tags/%version.tar.gz
Provides:       wpaperctl = %version-%release
Recommends:     %name-doc
BuildRequires:  cargo-rpm-macros rust-packaging anda-srpm-macros mold
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  scdoc
Packager:       madonuko <mado@fyralabs.com>

%description
wpaperd is the modern wallpaper daemon for Wayland. It dynamically changes the
current wallpaper, either after a certain amount of time or via a command-line
interface. It uses OpenGL ES to render the images and have beautiful hardware-
accelerated transitions, while being easy on resources.

%package doc
Summary:        Man pages for %name
Recommends:     wpaperd
Supplements:    wpaperd

%description doc
Man papes for %name.

%pkg_completion -befz wpaperctl wpaperd


%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies
scdoc < man/wpaperd-output.5.scd > target/rpm/man/wpaperd-output.5

%install
rm target/rpm/completions/*.ps1
install -Dpm755 -t %buildroot%_bindir target/rpm/wpaperctl
install -Dpm755 -t %buildroot%_bindir target/rpm/wpaperd
install -Dpm644 -t %buildroot%_mandir/man1/ target/rpm/man/wpaperctl.1
install -Dpm644 -t %buildroot%_mandir/man1/ target/rpm/man/wpaperd.1
install -Dpm644 -t %buildroot%_mandir/man5/ target/rpm/man/wpaperd-output.5
install -Dpm644 -t %buildroot%bash_completions_dir target/rpm/completions/*.bash
# https://github.com/elves/elvish/issues/1564
install -Dpm644 -t %buildroot%elvish_completions_dir target/rpm/completions/*.elv
install -Dpm644 -t %buildroot%fish_completions_dir target/rpm/completions/*.fish
install -Dpm644 -t %buildroot%zsh_completions_dir target/rpm/completions/_*


%if %{with check}
%check
%cargo_test
%endif


%files
%doc README.md
%license LICENSE.md
%license LICENSE.dependencies
%_bindir/wpaperctl
%_bindir/wpaperd

%files doc
%_mandir/man1/wpaperctl.1.gz
%_mandir/man1/wpaperd.1.gz
%_mandir/man5/wpaperd-output.5.gz

%changelog
* Fri Dec 20 2024 madonuko <mado@fyralabs.com> - 1.1.1-1
- Initial package
