%undefine __brp_mangle_shebangs

Name:           yazi
Version:        26.1.22
Release:        2%?dist
Summary:        Blazing fast terminal file manager written in Rust, based on async I/O
URL:            https://yazi-rs.github.io/
Source0:        https://github.com/sxyazi/yazi/archive/refs/tags/v%version.tar.gz
License:        MIT AND (MIT OR Apache-2.0) AND NCSA AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND ISC AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND ISC AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (MIT OR Apache-2.0 OR CC0-1.0) AND MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Yazi (means "duck") is a terminal file manager written in Rust, based on non-blocking async I/O. It aims to provide an efficient, user-friendly, and customizable file management experience.

A new article explaining its internal workings: Why is Yazi Fast?

- Full Asynchronous Support: All I/O operations are asynchronous, CPU tasks are spread across multiple threads, making the most of available resources.
- Powerful Async Task Scheduling and Management: Provides real-time progress updates, task cancellation, and internal task priority assignment.
- Built-in Support for Multiple Image Protocols: Also integrated with Überzug++ and Chafa, covering almost all terminals.
- Built-in Code Highlighting and Image Decoding: Combined with the pre-loading mechanism, greatly accelerates image and normal file loading.
- Concurrent Plugin System: UI plugins (rewriting most of the UI), functional plugins, custom previewer/preloader/spotter/fetcher; Just some pieces of Lua.
- Data Distribution Service: Built on a client-server architecture (no additional server process required), integrated with a Lua-based publish-subscribe model, achieving cross-instance communication and state persistence.
- Package Manager: Install plugins and themes with one command, keeping them up-to-date, or pin them to a specific version.
- Integration with ripgrep, fd, fzf, zoxide
- Vim-like input/pick/confirm/which/notify component, auto-completion for cd paths
- Multi-Tab Support, Cross-directory selection, Scrollable Preview (for videos, PDFs, archives, code, directories, etc.)
- Bulk Renaming, Archive Extraction, Visual Mode, File Chooser, Git Integration, Mount Manager
- Theme System, Mouse Support, Trash Bin, Custom Layouts, Virtual Filesystem, CSI u, OSC 52
... and more!


%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/ya        %{buildroot}%{_bindir}/ya
install -Dm755 target/rpm/yazi      %{buildroot}%{_bindir}/yazi
install -Dm644 assets/logo.png      %{buildroot}%{_hicolordir}/1024x1024/apps/yazi.png
install -Dm644 assets/yazi.desktop  %{buildroot}%{_appsdir}/yazi.desktop
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE LICENSE-ICONS LICENSE.dependencies
%doc README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%{_bindir}/ya
%{_bindir}/yazi
%{_hicolordir}/1024x1024/apps/yazi.png
%{_appsdir}/yazi.desktop

%changelog
* Sat Dec 27 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
