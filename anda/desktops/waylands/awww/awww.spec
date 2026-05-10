Name:           awww
Version:        0.12.1
Release:        1%?dist
Summary:        Wallpaper daemon for Wayland
SourceLicense:  GPL-3.0-only
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://codeberg.org/LGFae/awww
Source0:		%url/archive/v%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  anda-srpm-macros rust-packaging rpm_macro(bash_completions_dir) mold
BuildRequires:  scdoc
BuildRequires:  zstd
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
awww is a wallpaper daemon for Wayland that is controlled
at runtime. It uses LZ4 compression for frame animations
for animated wallpapers.

%package        bash-completion
Summary:        Bash Completion for %{name}
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -n %{name}
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies
./doc/gen.sh

%install
(cd client && %{cargo_install}) &
(cd daemon && %{cargo_install}) &
wait
install -Dm644 -T completions/awww.bash %buildroot%bash_completions_dir/awww
install -Dm644 -T completions/awww.fish %buildroot%fish_completions_dir/awww.fish
install -Dm644 -T completions/_awww %buildroot%zsh_completions_dir/_awww
install -Dm644 -t %buildroot%_mandir/man1 doc/generated/awww*1

%files
%doc CHANGELOG.md README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/awww
%{_bindir}/awww-daemon
%{_mandir}/man1/%name.1.gz
%{_mandir}/man1/%name-*.1.gz

%files bash-completion
%bash_completions_dir/awww

%files fish-completion
%fish_completions_dir/awww.fish

%files zsh-completion
%zsh_completions_dir/_awww

%changelog
* Sat May 09 2026 <aagarwalpdx@gmail.com> - 0.12.1-1
- replace swww with awww
* Tue Dec 24 2024 madonuko <mado@fyralabs.com> - 0.9.5-1
- Initial package
