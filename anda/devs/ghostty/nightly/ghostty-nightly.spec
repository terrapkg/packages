%global commit 72d085525b22d66468c5969a4d507a0fa68d4a04
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250118
%global public_key RWQlAjJC23149WL2sEpT/l0QKy7hMIFhYdQOFy0Z7z7PbneUgvlsnYcV
%global cache_dir %{builddir}/zig-cache

Name:           ghostty-nightly
Version:        %{commit_date}.%{shortcommit}
Release:        2%?dist
Summary:        A fast, native terminal emulator written in Zig; this is the Tip (nightly) build.
License:        MIT AND MPL-2.0 AND OFL-1.1 AND (WTFPL OR CC0-1.0) AND Apache-2.0
URL:            https://ghostty.org/
Source0:        https://github.com/ghostty-org/ghostty/releases/download/tip/ghostty-source.tar.gz
Source1:        https://github.com/ghostty-org/ghostty/releases/download/tip/ghostty-source.tar.gz.minisig
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  minisign
BuildRequires:  ncurses
BuildRequires:  ncurses-devel
BuildRequires:  pandoc-cli
BuildRequires:  zig
Requires:       %{name}-terminfo = %{version}-%{release}
Requires:       %{name}-shell-integration = %{version}-%{release}
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(oniguruma)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  libX11-devel
Conflicts:      ghostty
Provides:       ghostty-tip = %{version}-%{release}
Packager:       ShinyGil <rockgrub@protonmail.com>

%description
👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.

%package        bash-completion
Summary:        Ghostty Bash completion
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description    bash-completion
%summary.

%package        fish-completion
Summary:        Ghostty Fish completion
Requires:       fish
Supplements:    (%{name} and fish)

%description    fish-completion
%summary.

%package        zsh-completion
Summary:        Ghostty Zsh completion
Requires:       zsh
Supplements:    (%{name} and zsh)

%description    zsh-completion
%summary.

%package        shell-integration
Summary:        Ghostty shell integration
Supplements:    %{name}

%description    shell-integration
%summary.

%package        terminfo
Summary:        Ghostty terminfo
Supplements:    %{name}

%description    terminfo
%summary.

%prep
/usr/bin/minisign -V -m %{SOURCE0} -x %{SOURCE1} -P %{public_key}
%autosetup -n ghostty-source

# Download everything ahead of time so we can enable system integration mode
ZIG_GLOBAL_CACHE_DIR="%{cache_dir}" ./nix/build-support/fetch-zig-cache.sh

%build

%install
DESTDIR="%{buildroot}" \
zig build \
    --summary all \
    --release=fast \
    --system "%{cache_dir}/p" \
    --prefix "%{_prefix}" --prefix-lib-dir "%{_libdir}" \
    --prefix-exe-dir "%{_bindir}" --prefix-include-dir "%{_includedir}" \
    --verbose \
    -Dcpu=baseline \
    -Dstrip=false \
    -Dpie=true \
    -Demit-docs \
    -Demit-termcap \
    -Demit-terminfo

%files
%doc README.md
%license LICENSE
%_bindir/ghostty
%_datadir/applications/com.mitchellh.ghostty.desktop
%_datadir/bat/syntaxes/ghostty.sublime-syntax
%_datadir/ghostty/
%_datadir/kio/servicemenus/com.mitchellh.ghostty.desktop
%_datadir/nautilus-python/extensions/com.mitchellh.ghostty.py
%_datadir/nvim/site/compiler/ghostty.vim
%_datadir/nvim/site/ftdetect/ghostty.vim
%_datadir/nvim/site/ftplugin/ghostty.vim
%_datadir/nvim/site/syntax/ghostty.vim
%_datadir/vim/vimfiles/compiler/ghostty.vim
%_datadir/vim/vimfiles/ftdetect/ghostty.vim
%_datadir/vim/vimfiles/ftplugin/ghostty.vim
%_datadir/vim/vimfiles/syntax/ghostty.vim
%_iconsdir/hicolor/16x16/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/32x32/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/128x128/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/256x256/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/512x512/apps/com.mitchellh.ghostty.png
%_iconsdir/hicolor/1024x1024/apps/com.mitchellh.ghostty.png
%_mandir/man1/ghostty.1.gz
%_mandir/man5/ghostty.5.gz

%files bash-completion
%bash_completions_dir/ghostty.bash

%files fish-completion
%fish_completions_dir/ghostty.fish

%files zsh-completion
%zsh_completions_dir/_ghostty

%files shell-integration
%_datadir/ghostty/shell-integration/bash/bash-preexec.sh
%_datadir/ghostty/shell-integration/bash/ghostty.bash
%_datadir/ghostty/shell-integration/elvish/lib/ghostty-integration.elv
%_datadir/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish
%_datadir/ghostty/shell-integration/zsh/.zshenv
%_datadir/ghostty/shell-integration/zsh/ghostty-integration

%files terminfo
%_datadir/terminfo/ghostty.termcap
%_datadir/terminfo/ghostty.terminfo
%_datadir/terminfo/g/ghostty
%_datadir/terminfo/x/xterm-ghostty

%changelog
* Tue Dec 31 2024 ShinyGil <rockgrub@protonmail.com>
- Update to 20241231.3f7c3af
 * High CVE-2003-0063: Allows execution of arbitrary commands
 * Medium CVE-2003-0070: Allows execution of arbitrary commands

* Thu Dec 26 2024 ShinyGil <rockgrub@protonmail.com>
- Initial package
