# Signing key from https://github.com/ghostty-org/ghostty/blob/main/PACKAGING.md
%global public_key RWQlAjJC23149WL2sEpT/l0QKy7hMIFhYdQOFy0Z7z7PbneUgvlsnYcV
%global appid com.mitchellh.ghostty

Name:           ghostty
Version:        1.1.3
Release:        2%?dist
Summary:        A fast, native terminal emulator written in Zig.
License:        MIT AND MPL-2.0 AND OFL-1.1 AND (WTFPL OR CC0-1.0) AND Apache-2.0
URL:            https://ghostty.org/
Source0:        https://release.files.ghostty.org/%{version}/ghostty-%{version}.tar.gz
Source1:        https://release.files.ghostty.org/%{version}/ghostty-%{version}.tar.gz.minisig
BuildRequires:  anda-srpm-macros >= 0.2.15
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libX11-devel
BuildRequires:  minisign
BuildRequires:  ncurses
BuildRequires:  ncurses-devel
BuildRequires:  pandoc-cli
BuildRequires:  zig >= 0.14.0
BuildRequires:  zig-rpm-macros
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
Requires:       (%{name}-kio = %{evr} if kf6-kio)
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

%package        kio
Summary:        KIO support for Ghostty
Requires:       %{name} = %{evr}
BuildArch:      noarch

%description    kio
This package allows Ghostty to interact with KIO.

%package        nautilus
Summary:        Nautilus menu support for Ghostty
Supplements:    (%{name} and nautilus)
Requires:       %{name} = %{evr}
BuildArch:      noarch

%description    nautilus
This package enables Nautilus integration for Ghostty.

%package        vim
Summary:        Vim plugins for Ghostty
Supplements:    (%{name} and vim-filesystem)
Requires:       %{name} = %{evr}
Requires:       vim-enhanced
Requires:       vim-filesystem
BuildArch:      noarch

%description    vim
This package provides the Ghostty Vim plugins.

%package        neovim
Summary:        Neovim plugins for Ghostty
Supplements:    (%{name} and neovim)
Requires:       %{name} = %{evr}
Requires:       neovim
BuildArch:      noarch

%description    neovim
This package provides the Neovim plugins for Ghostty.

%package        bat-syntax
Summary:        Bat syntax for Ghostty
Supplements:    (%{name} and bat)
Requires:       %{name} = %{evr}
Requires:       bat
BuildArch:      noarch

%description    bat-syntax
This package provides the Bat syntax files for Ghostty.

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
Obsoletes:      %{name}-terminfo-source < %{evr}
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

export ZIG_GLOBAL_CACHE_DIR="%{_zig_cache_dir}"
zig build --fetch
zig fetch git+https://github.com/zigimg/zigimg#3a667bdb3d7f0955a5a51c8468eac83210c1439e
zig fetch git+https://github.com/mitchellh/libxev#f6a672a78436d8efee1aa847a43a900ad773618b

%build

%install
DESTDIR="%{buildroot}" \
%{zig_build_target -r fast} \
    --prefix "%{_prefix}" --prefix-lib-dir "%{_libdir}" \
    --prefix-exe-dir "%{_bindir}" --prefix-include-dir "%{_includedir}" \
    -Dversion-string="%{version}" \
    -Dstrip=false \
    -Dpie=true \
    -Demit-docs

#Don't conflict with ncurses-term on F42 and up
%if 0%{?fedora} >= 42
rm -rf %{buildroot}%{_datadir}/terminfo/g/ghostty
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/doc
%{_datadir}/%{name}/themes
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_iconsdir}/hicolor/16x16/apps/%{appid}.png
%{_iconsdir}/hicolor/16x16@2/apps/%{appid}.png
%{_iconsdir}/hicolor/32x32/apps/%{appid}.png
%{_iconsdir}/hicolor/32x32@2/apps/%{appid}.png
%{_iconsdir}/hicolor/128x128/apps/%{appid}.png
%{_iconsdir}/hicolor/128x128@2/apps/%{appid}.png
%{_iconsdir}/hicolor/256x256/apps/%{appid}.png
%{_iconsdir}/hicolor/256x256@2/apps/%{appid}.png
%{_iconsdir}/hicolor/512x512/apps/%{appid}.png
%{_iconsdir}/hicolor/1024x1024/apps/%{appid}.png
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man5/%{name}.5.gz
%{_userunitdir}/%{appid}.service
%{_prefix}/lib/dbus-1/services/%{appid}.service

%files bash-completion
%{bash_completions_dir}/%{name}.bash

%files fish-completion
%{fish_completions_dir}/%{name}.fish

%files zsh-completion
%{zsh_completions_dir}/_%{name}

%files kio
%{_datadir}/kio/servicemenus/%{appid}.desktop

%files nautilus
%{_datadir}/nautilus-python/extensions/%{name}.py

%files vim
%{_datadir}/vim/vimfiles/compiler/%{name}.vim
%{_datadir}/vim/vimfiles/ftdetect/%{name}.vim
%{_datadir}/vim/vimfiles/ftplugin/%{name}.vim
%{_datadir}/vim/vimfiles/syntax/%{name}.vim

%files neovim
%{_datadir}/nvim/site/compiler/%{name}.vim
%{_datadir}/nvim/site/ftdetect/%{name}.vim
%{_datadir}/nvim/site/ftplugin/%{name}.vim
%{_datadir}/nvim/site/syntax/%{name}.vim

%files bat-syntax
%{_datadir}/bat/syntaxes/%{name}.sublime-syntax

%files shell-integration
%dir %{_datadir}/%{name}/shell-integration
%{_datadir}/%{name}/shell-integration/bash/bash-preexec.sh
%{_datadir}/%{name}/shell-integration/bash/%{name}.bash
%{_datadir}/%{name}/shell-integration/elvish/lib/%{name}-integration.elv
%{_datadir}/%{name}/shell-integration/fish/vendor_conf.d/%{name}-shell-integration.fish
%{_datadir}/%{name}/shell-integration/zsh/.zshenv
%{_datadir}/%{name}/shell-integration/zsh/%{name}-integration

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
