%global commit 9ae02a326f62bd88f7f5508cf1807c67e7775cb5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global public_key RWQlAjJC23149WL2sEpT/l0QKy7hMIFhYdQOFy0Z7z7PbneUgvlsnYcV
%global ver 1.3.2
%global base_name ghostty
%global appid com.mitchellh.%{base_name}

Name:           %{base_name}-tip
Version:        202608200320
Release:        1%{?dist}
%if 0%{?fedora} <= 46
Epoch:          1
%endif
Summary:        A fast, native terminal emulator written in Zig; this is the Tip (nightly) build.
License:        MIT AND MPL-2.0 AND OFL-1.1 AND (WTFPL OR CC0-1.0) AND Apache-2.0
URL:            https://%{base_name}.org
Source0:        https://github.com/%{base_name}-org/%{base_name}/releases/download/tip/%{base_name}-source.tar.gz
Source1:        https://github.com/%{base_name}-org/%{base_name}/releases/download/tip/%{base_name}-source.tar.gz.minisig
Source2:        strip.sh
Patch0:         %{base_name}-translate.patch
BuildRequires:  anda-srpm-macros >= 0.2.15
BuildRequires:  gettext
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libX11-devel
BuildRequires:  minisign
BuildRequires:  ncurses
BuildRequires:  ncurses-devel
BuildRequires:  pandoc-cli
BuildRequires:  systemd-rpm-macros
BuildRequires:  zig
BuildRequires:  zig-rpm-macros
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(oniguruma)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-terminfo = %{evr}
Requires:       %{name}-shell-integration = %{evr}
Requires:       (%{name}-kio = %{evr} if kf5-kio-core)
Requires:       (%{name}-kio = %{evr} if kf6-kio-core)
Requires:       gtk4
Requires:       gtk4-layer-shell
Requires:       libadwaita
Conflicts:      %{base_name}
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly <= 1.3.2~tip^20260812gitc54ec80
%endif
Packager:       Gilver E. <roachy@fyralabs.com>

# Work around a Zig 0.16.0 mislinking bug
# I <3 Zig
%global __strip %{S:2}

%description
👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.

%package        bash-completion
Summary:        Ghostty Bash completion
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly-bash-completion <= 1.3.2~tip^20260812gitc54ec80
%endif
BuildArch:      noarch

%description    bash-completion
Bash shell completion for Ghostty.

%package        fish-completion
Summary:        Ghostty Fish completion
Requires:       %{name}
Requires:       fish
Supplements:    (%{name} and fish)
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly-fish-completion <= 1.3.2~tip^20260812gitc54ec80
%endif
BuildArch:      noarch

%description    fish-completion
Fish shell completion for Ghostty.

%package        zsh-completion
Summary:        Ghostty Zsh completion
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly-zsh-completion <= 1.3.2~tip^20260812gitc54ec80
%endif
BuildArch:      noarch

%description    zsh-completion
Zsh shell completion for Ghostty.

%package        devel
Summary:        Development files for Ghostty.
Requires:       %{name} = %{evr}

%description    devel
This package includes the development files for Ghostty.

%package        kio
Summary:        KIO support for Ghostty
Requires:       %{name} = %{evr}
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly-kio <= 1.3.2~tip^20260812gitc54ec80
%endif
BuildArch:      noarch

%description    kio
This package allows Ghostty to interact with KIO.

%package        nautilus
Summary:        Nautilus menu support for Ghostty
Supplements:    (%{name} and nautilus)
Requires:       %{name} = %{evr}
Requires:       nautilus-python
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly-nautilus <= 1.3.2~tip^20260812gitc54ec80
%endif
BuildArch:      noarch

%description    nautilus
This package enables Nautilus integration for Ghostty.

%package        vim
Summary:        Vim plugins for Ghostty
Supplements:    (%{name} and vim-filesystem)
Requires:       %{name} = %{evr}
Requires:       vim-enhanced
Requires:       vim-filesystem
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly-vim <= 1.3.2~tip^20260812gitc54ec80
%endif
BuildArch:      noarch

%description    vim
This package provides the Ghostty Vim plugins.

%package        neovim
Summary:        Neovim plugins for Ghostty
Supplements:    (%{name} and neovim)
Requires:       %{name} = %{evr}
Requires:       neovim
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly-neovim <= 1.3.2~tip^20260812gitc54ec80
%endif
BuildArch:      noarch

%description    neovim
This package provides the Neovim plugins for Ghostty.

%package        bat-syntax
Summary:        Bat syntax for Ghostty
Supplements:    (%{name} and bat)
Requires:       %{name} = %{evr}
Requires:       bat
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly-bat-syntax <= 1.3.2~tip^20260812gitc54ec80
%endif
BuildArch:      noarch

%description    bat-syntax
This package provides the Bat syntax files for Ghostty.

%package        shell-integration
Summary:        Ghostty shell integration
Supplements:    %{name}
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly-shell-integration <= 1.3.2~tip^20260812gitc54ec80
%endif
BuildArch:      noarch

%description    shell-integration
This package contains files allowing Ghostty to integrate with various shells.

%package        terminfo
Summary:        Ghostty terminfo
%if 0%{?fedora} >= 42
Requires:       ncurses-term >= 6.5-5.20250125
%endif
Supplements:    %{name}
%if 0%{?fedora} <= 46
Obsoletes:      %{base_name}-nightly-terminfo < %{evr}
%endif
Obsoletes:      %{name}-terminfo-source <= 1.3.2~tip^20260812gitc54ec80
BuildArch:      noarch

%description    terminfo
Ghostty's terminfo. Needed for basic terminal function.

%package -n     libghostty-vt-tip
Summary:        The libghostty-vt libraries
%if 0%{?fedora} <= 46
Obsoletes:      libghostty-vt-nightly <= 1.3.2~tip^20260812gitc54ec80
%endif

%description -n libghostty-vt-tip
This package contains the libghostty-vt libraries, the first of many libghostty libaries in development.

%package -n     libghostty-vt-tip-devel
Summary:        Development files for libghostty-vt
Requires:       libghostty-vt-tip = %{evr}
%if 0%{?fedora} <= 46
Obsoletes:      libghostty-vt-nightly-devel <= 1.3.2~tip^20260812gitc54ec80
%endif

%description -n libghostty-vt-tip-devel
This package contains the libraries and header files that are needed for developing with libghostty-vt.

%package -n     libghostty-vt-tip-static
Summary:        Static files for libghostty-vt
Requires:       libghostty-vt-tip = %{evr}

%description -n libghostty-vt-tip-static
This package contains the static files that are used for developing with libghostty-vt.

%prep
/usr/bin/minisign -V -m %{SOURCE0} -x %{SOURCE1} -P %{public_key}
%setup -qn %{base_name}-%{ver}-main-+%{shortcommit}

%zig_prep
ZIG_GLOBAL_CACHE_DIR="%{_zig_cache_dir}" ./nix/build-support/fetch-zig-cache.sh

# Patch Ghostty's broken translate_c fork
pushd zig-pkg/translate_c*
%autopatch -p1
popd

%build

%install
%{zig_install_target -r fast} \
    --prefix "%{_prefix}" --prefix-lib-dir "%{_libdir}" \
    --prefix-exe-dir "%{_bindir}" --prefix-include-dir "%{_includedir}" \
    -Dversion-string="%{ver}-dev+%{shortcommit}" \
    -Dstrip=false \
    -Dpie=true \
    -Demit-docs \
    -Demit-themes=false

# Don't conflict with ncurses-term on F42 and up
%if 0%{?fedora} >= 42
rm -rf %{buildroot}%{_datadir}/terminfo/g/%{base_name}
%endif

%find_lang %{appid}

%files -f %{appid}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{base_name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/%{base_name}/doc/
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/dbus-1/services/%{appid}.service
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
%{_mandir}/man1/%{base_name}.1.gz
%{_mandir}/man5/%{base_name}.5.gz
%{_userunitdir}/app-%{appid}.service

%files bash-completion
%{bash_completions_dir}/%{base_name}.bash

%files fish-completion
%{fish_completions_dir}/%{base_name}.fish

%files zsh-completion
%{zsh_completions_dir}/_%{base_name}

%files devel
%{_includedir}/ghostty/

%files kio
%{_datadir}/kio/servicemenus/%{appid}.desktop

%files nautilus
%{_datadir}/nautilus-python/extensions/%{base_name}.py

%files vim
%{_datadir}/vim/vimfiles/compiler/%{base_name}.vim
%{_datadir}/vim/vimfiles/ftdetect/%{base_name}.vim
%{_datadir}/vim/vimfiles/ftplugin/%{base_name}.vim
%{_datadir}/vim/vimfiles/syntax/%{base_name}.vim

%files neovim
%{_datadir}/nvim/site/compiler/%{base_name}.vim
%{_datadir}/nvim/site/ftdetect/%{base_name}.vim
%{_datadir}/nvim/site/ftplugin/%{base_name}.vim
%{_datadir}/nvim/site/syntax/%{base_name}.vim

%files bat-syntax
%{_datadir}/bat/syntaxes/%{base_name}.sublime-syntax

%files shell-integration
%{_datadir}/%{base_name}/shell-integration/

%files terminfo
%if 0%{?fedora} < 42
%{_datadir}/terminfo/g/%{base_name}
%endif
%{_datadir}/terminfo/x/xterm-%{base_name}

%files -n libghostty-vt-tip
%{_libdir}/libghostty-vt.so.*

%files -n libghostty-vt-tip-devel
%{_libdir}/libghostty-vt.so
%{_datadir}/pkgconfig/libghostty-vt.pc

%files -n libghostty-vt-tip-static
%{_libdir}/libghostty-vt.a
%{_datadir}/pkgconfig/libghostty-vt-static.pc

%post
%systemd_user_post app-%{appid}.service

%preun
%systemd_user_preun app-%{appid}.service

%postun
%systemd_user_postun app-%{appid}.service

%changelog
* Sun Aug 16 2026 Gilver E. <roachy@fyralabs.com> - 1:202608122048-1
- Switch to tracking each Tip release
* Sat Nov 29 2025 Gilver E. <rockgrub@disroot.org> - 1.3.0~tip^20251128git9baf37a-1
- Initial libghostty-vt packages
* Tue Oct 28 2025 Gilver E. <rockgrub@disroot.org> - 1.3.0~tip^20251027gitd40321a-2
- Disabled bundled themes
 * This is necessary to address licensing issues in the themes repo Ghostty uses
 * See: https://github.com/mbadolato/iTerm2-Color-Schemes/issues/638
* Sat May 31 2025 Gilver E. <rockgrub@disroot.org> - 1.1.4~tip^20250531git1ff9162
- Updated for Zig 0.14.0
- Updated for ncurses-term compatibility in Fedora 42 and Rawhide
* Wed Mar 05 2025 Gilver E. <rockgrub@disroot.org>
- Update to 1.1.3~tip^20250305git66e8d91-2
 * Ghostty now has localization support via gettext as well as corresponding localization files
* Fri Jan 31 2025 Gilver E. <rockgrub@disroot.org>
- Update to 1.1.1~tip^20250131git5508e7-1
 * Low GHSA-98wc-794w-gjx3: Ghostty leaked file descriptors allowing the shell and any of its child processes to impact other Ghostty terminal instances
 * Better Git versioning scheme
 * Ghostty terminfo source files are now a subpackage
 * Shell integration and completion and terminfo subpackages are now properly noarch
* Tue Dec 31 2024 Gilver E. <rockgrub@disroot.org>
- Update to 20241231.3f7c3af
 * High CVE-2003-0063: Allows execution of arbitrary commands
 * Medium CVE-2003-0070: Allows execution of arbitrary commands
* Thu Dec 26 2024 Gilver E. <rockgrub@disroot.org>
- Initial package
