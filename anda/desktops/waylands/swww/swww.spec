Name:           swww
Version:        0.10.3
Release:        1%?dist
Summary:        Wallpaper daemon for Wayland
SourceLicense:  GPL-3.0-only
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://github.com/LGFae/swww
Source0:		%url/archive/refs/tags/v%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  anda-srpm-macros rust-packaging rpm_macro(bash_completions_dir) mold
BuildRequires:  scdoc
BuildRequires:  zstd
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
swww is a wallpaper daemon for Wayland that is controlled
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
%autosetup
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies
./doc/gen.sh

%install
(cd client && %{cargo_install}) &
(cd daemon && %{cargo_install}) &
wait
install -Dm644 -T completions/swww.bash %buildroot%bash_completions_dir/swww
install -Dm644 -T completions/swww.fish %buildroot%fish_completions_dir/swww.fish
install -Dm644 -T completions/_swww %buildroot%zsh_completions_dir/_swww
install -Dm644 -t %buildroot%_mandir/man1 doc/generated/swww*1

%files
%doc CHANGELOG.md README.md
%license LICENSE LICENSE.dependencies
%_bindir/swww
%_bindir/swww-daemon
%_mandir/man1/%name-clear-cache.1.gz
%_mandir/man1/%name-clear.1.gz
%_mandir/man1/%name-daemon.1.gz
%_mandir/man1/%name-img.1.gz
%_mandir/man1/%name-kill.1.gz
%_mandir/man1/%name-query.1.gz
%_mandir/man1/%name-restore.1.gz
%_mandir/man1/%name.1.gz

%files bash-completion
%bash_completions_dir/swww

%files fish-completion
%fish_completions_dir/swww.fish

%files zsh-completion
%zsh_completions_dir/_swww

%changelog
* Tue Dec 24 2024 madonuko <mado@fyralabs.com> - 0.9.5-1
- Initial package
