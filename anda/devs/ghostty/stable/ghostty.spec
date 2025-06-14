# Signing key from https://github.com/ghostty-org/ghostty/blob/main/PACKAGING.md
%global public_key RWQlAjJC23149WL2sEpT/l0QKy7hMIFhYdQOFy0Z7z7PbneUgvlsnYcV
%if 0%{?fedora} <= 40
%global cache_dir %{_builddir}/zig-cache
%else
%global cache_dir %{builddir}/zig-cache
%endif

Name:           ghostty
Version:        1.1.3
Release:        1%?dist
Summary:        A fast, native terminal emulator written in Zig.
License:        MIT AND MPL-2.0 AND OFL-1.1 AND (WTFPL OR CC0-1.0) AND Apache-2.0
URL:            https://ghostty.org/
Source0:        https://release.files.ghostty.org/%{version}/ghostty-%{version}.tar.gz
Source1:        https://release.files.ghostty.org/%{version}/ghostty-%{version}.tar.gz.minisig
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libX11-devel
BuildRequires:  minisign
BuildRequires:  ncurses
BuildRequires:  ncurses-devel
BuildRequires:  pandoc-cli
BuildRequires:  zig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(oniguruma)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-terminfo = %{version}-%{release}
Requires:       %{name}-shell-integration = %{version}-%{release}
Requires:       gtk4
Requires:       libadwaita
Conflicts:      ghostty-nightly
Packager:       Gilver E. <rockgrub@disroot.org>

%description
👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.

%package        bash-completion
Summary:        Ghostty Bash completion
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description    bash-completion
Bash shell completion for Ghostty.

%package        fish-completion
Summary:        Ghostty Fish completion
Requires:       %{name} = %{version}-%{release}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description    fish-completion
Fish shell completion for Ghostty.

%package        zsh-completion
Summary:        Ghostty Zsh completion
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description    zsh-completion
Zsh shell completion for Ghostty.

%package        shell-integration
Summary:        Ghostty shell integration
Supplements:    %{name}
BuildArch:      noarch

%description    shell-integration
This package contains files allowing Ghostty to integrate with various shells.

%package        terminfo
Summary:        Ghostty terminfo
Supplements:    %{name}
%if 0%{?fedora} >= 42
Requires:       ncurses-term >= 6.5-5.20250125%{?dist}
%endif
BuildArch:      noarch

%description    terminfo
Ghostty's terminfo. Needed for basic terminal function.

%package        terminfo-source
Summary:        Source files for Ghostty's terminfo
Requires:       %{name}
Requires:       %{name}-terminfo
BuildArch:      noarch

%description    terminfo-source
Source files for Ghostty's terminfo. Available for debugging use.

%prep
/usr/bin/minisign -V -m %{SOURCE0} -x %{SOURCE1} -P %{public_key}
%autosetup

export ZIG_GLOBAL_CACHE_DIR="%{cache_dir}"
zig build --fetch
zig fetch git+https://github.com/zigimg/zigimg#3a667bdb3d7f0955a5a51c8468eac83210c1439e
zig fetch git+https://github.com/mitchellh/libxev#f6a672a78436d8efee1aa847a43a900ad773618b

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
    -Dversion-string=%{version} \
    -Dcpu=baseline \
    -Dstrip=false \
    -Dpie=true \
    -Demit-docs \
    -Demit-termcap \
    -Demit-terminfo

#Don't conflict with ncurses-term on F42 and up
%if 0%{?fedora} >= 42
rm -rf %{buildroot}%{_datadir}/terminfo/g/ghostty
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/ghostty
%{_datadir}/applications/com.mitchellh.ghostty.desktop
%{_datadir}/bat/syntaxes/ghostty.sublime-syntax
%{_datadir}/ghostty/
%{_datadir}/kio/servicemenus/com.mitchellh.ghostty.desktop
%{_datadir}/nautilus-python/extensions/ghostty.py
%{_datadir}/nvim/site/compiler/ghostty.vim
%{_datadir}/nvim/site/ftdetect/ghostty.vim
%{_datadir}/nvim/site/ftplugin/ghostty.vim
%{_datadir}/nvim/site/syntax/ghostty.vim
%{_datadir}/vim/vimfiles/compiler/ghostty.vim
%{_datadir}/vim/vimfiles/ftdetect/ghostty.vim
%{_datadir}/vim/vimfiles/ftplugin/ghostty.vim
%{_datadir}/vim/vimfiles/syntax/ghostty.vim
%{_iconsdir}/hicolor/16x16/apps/com.mitchellh.ghostty.png
%{_iconsdir}/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%{_iconsdir}/hicolor/32x32/apps/com.mitchellh.ghostty.png
%{_iconsdir}/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%{_iconsdir}/hicolor/128x128/apps/com.mitchellh.ghostty.png
%{_iconsdir}/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%{_iconsdir}/hicolor/256x256/apps/com.mitchellh.ghostty.png
%{_iconsdir}/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%{_iconsdir}/hicolor/512x512/apps/com.mitchellh.ghostty.png
%{_iconsdir}/hicolor/1024x1024/apps/com.mitchellh.ghostty.png
%{_mandir}/man1/ghostty.1.gz
%{_mandir}/man5/ghostty.5.gz

%files bash-completion
%{bash_completions_dir}/ghostty.bash

%files fish-completion
%{fish_completions_dir}/ghostty.fish

%files zsh-completion
%{zsh_completions_dir}/_ghostty

%files shell-integration
%{_datadir}/ghostty/shell-integration/bash/bash-preexec.sh
%{_datadir}/ghostty/shell-integration/bash/ghostty.bash
%{_datadir}/ghostty/shell-integration/elvish/lib/ghostty-integration.elv
%{_datadir}/ghostty/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish
%{_datadir}/ghostty/shell-integration/zsh/.zshenv
%{_datadir}/ghostty/shell-integration/zsh/ghostty-integration

%files terminfo
%if 0%{?fedora} < 42
%{_datadir}/terminfo/g/ghostty
%endif
%{_datadir}/terminfo/x/xterm-ghostty

%files terminfo-source
%{_datadir}/terminfo/ghostty.termcap
%{_datadir}/terminfo/ghostty.terminfo

%changelog
* Fri Jan 31 2025 Gilver E. <rockgrub@disroot.org>
- Update to 1.1.0-1%{?dist}
 * Low GHSA-98wc-794w-gjx3: Ghostty leaked file descriptors allowing the shell and any of its child processes to impact other Ghostty terminal instances
 * Ghostty terminfo source files are now a subpackage
 * Shell integration and completion and terminfo subpackages are now properly noarch
* Tue Dec 31 2024 Gilver E. <rockgrub@disroot.org>
- Update to 1.0.1
 * High CVE-2003-0063: Allows execution of arbitrary commands
 * Medium CVE-2003-0070: Allows execution of arbitrary commands

* Thu Dec 26 2024 Gilver E. <rockgrub@disroot.org>
- Initial package
