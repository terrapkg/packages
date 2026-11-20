%global commit 82b4fce10ac78ca11567e822b678ee50f463b2fa
%global commit_date 20261118
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 2.0.0.0

%global lsp_client lsp-types-client-0.1.0.0
%global subpkgs %{lsp_client}

%global appid io.github.leksah.Leksah
%global appstream_component desktop-application

%global ghc_without_dynamic 1
%{?haskell_setup}

Name:           leksah
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Haskell IDE written in Haskell
License:        Apache-2.0 AND MIT AND OFL-1.1
URL:            https://leksah.github.io
Source0:        https://github.com/leksah/leksah/archive/%{commit}/leksah-%{commit}.tar.gz
Source1:        %{appid}.metainfo.xml

BuildRequires:  desktop-file-utils
BuildRequires:  terra-appstream-helper
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-clay-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cpphs-devel
BuildRequires:  ghc-criterion-measurement-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-dependent-map-devel
BuildRequires:  ghc-dependent-sum-devel
BuildRequires:  ghc-dependent-sum-template-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exception-transformers-devel
BuildRequires:  ghc-executable-path-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-fsnotify-devel
BuildRequires:  ghc-generic-deriving-devel
BuildRequires:  ghc-ghc-lib-parser-devel
BuildRequires:  ghc-ghcjs-dom-devel
BuildRequires:  ghc-gi-gdk4-devel
BuildRequires:  ghc-gi-gio-devel
BuildRequires:  ghc-gi-glib-devel
BuildRequires:  ghc-gi-gtk4-devel
BuildRequires:  ghc-gi-webkit-devel
BuildRequires:  ghc-haskell-gi-base-devel
BuildRequires:  ghc-hslogger-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-jsaddle-devel
BuildRequires:  ghc-jsaddle-terminal-devel
BuildRequires:  ghc-jsaddle-warp-devel
BuildRequires:  ghc-jsaddle-webkitgtk-devel
BuildRequires:  ghc-keycode-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-lsp-types-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-posix-pty-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-reflex-devel
BuildRequires:  ghc-reflex-dom-core-devel
BuildRequires:  ghc-reflex-dom-svg-devel
BuildRequires:  ghc-regex-base-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-shakespeare-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-strict-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-replace-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-app-static-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-wai-websockets-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-websockets-devel
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(webkitgtk-6.0)

Requires:       hicolor-icon-theme
Requires:       tmux
Recommends:     cabal-install
Recommends:     ghc
Recommends:     git-core

Provides:       bundled(ghc-lsp-types-client) = 0.1.0.0
Provides:       bundled(js-codemirror) = 6
Provides:       bundled(js-monaco-editor)
Provides:       bundled(js-xterm)
Provides:       bundled(hasklig-fonts)

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
A fast, hackable development environment written in Haskell. The UI is a
reflex-dom program hosted in a native GTK4/WebKitGTK window, and it can also
serve itself to a browser. It has deep Haskell tooling (cabal workspaces,
haskell-language-server, GHCi debugging), multi-language LSP support,
tmux-backed terminals and built-in git panes.

%prep
%autosetup -n leksah-%{commit}
mv lsp-types-client %{lsp_client}
sed -Ei 's/ *&& *< *[0-9.]+//' leksah/leksah.cabal %{lsp_client}/lsp-types-client.cabal

%build
%ghc_libs_build -H -P %{subpkgs}
cd leksah
%ghc_bin_build

%install
cd leksah
%ghc_bin_install
rm -rf %{buildroot}%{_libdir} %{buildroot}%{_datadir}/%{name}-%{ver} %{buildroot}%{_docdir}

install -d %{buildroot}%{_datadir}/%{name}
cp -r cm6 monaco xterm fonts pics %{buildroot}%{_datadir}/%{name}/
rm -rf %{buildroot}%{_datadir}/%{name}/{cm6,monaco}/{src,package.json,.gitignore}

%desktop_file_install linux/applications/%{name}.desktop
install -Dpm644 linux/applications/%{name}.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml
install -Dpm644 linux/icons/hicolor/48x48/apps/%{name}.png %{buildroot}%{_hicolordir}/48x48/apps/%{name}.png
%terra_appstream -o %{S:1}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{name}.desktop

%files
%license LICENSE leksah/LICENSE
%doc Readme.md CHANGELOG.md
%{_bindir}/%{name}
%{_bindir}/%{name}-cmd
%{_bindir}/%{name}-warp
%{_datadir}/%{name}/
%{_appsdir}/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_hicolordir}/48x48/apps/%{name}.png
%{_metainfodir}/%{appid}.metainfo.xml


%changelog
* Wed Nov 18 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
