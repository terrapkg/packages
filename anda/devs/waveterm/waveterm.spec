%global appid dev.waveterm

%global _missing_build_ids_terminate_build 0
%global _build_id_links none

%define go_task(p:) \
    go-task -p -v -y \

%define _optdir /opt/Wave

%dnl %define npm

Name:           waveterm
Version:        0.12.5
Release:        1%?dist
Summary:        An open-source, cross-platform terminal for seamless workflows
License:        Apache-2.0
URL:            https://github.com/wavetermdev/waveterm
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{appid}.metainfo.xml

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  go
BuildRequires:  go-task
BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  zig
BuildRequires:  zip
BuildRequires:  libxcrypt-compat
BuildRequires:  glib2-devel
BuildRequires:  nspr
BuildRequires:  nss
BuildRequires:  dbus-libs
BuildRequires:  atk
BuildRequires:  at-spi2-atk
BuildRequires:  cups-libs
BuildRequires:  cairo
BuildRequires:  gtk3
BuildRequires:  mesa-libgbm
BuildRequires:  alsa-lib
BuildRequires:  rpm-build
%dnl BuildRequires:	anda-srpm-macros
BuildRequires:  terra-appstream-helper

Requires:       electron

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%{go_task} init

%build
%{go_task} package || /bin/true
ls -la make/linux-unpacked/

%dnl --completion string

%dnl %ifarch aarch64
%dnl USE_SYSTEM_FPM=1 go-task start
%dnl %endif

%install
mkdir -p %{buildroot}%{_optdir}
install -Dm 0755 make/linux-unpacked/waveterm                   %{buildroot}%{_optdir}/waveterm
install -Dm 0644 make/linux-unpacked/libvk_swiftshader.so       %{buildroot}%{_optdir}/libvk_swiftshader.so
install -Dm 0755 make/linux-unpacked/chrome_crashpad_handler    %{buildroot}%{_optdir}/chrome_crashpad_handler
install -Dm 0755 make/linux-unpacked/chrome-sandbox             %{buildroot}%{_optdir}/chrome-sandbox
install -Dm 0644 make/linux-unpacked/libvulkan.so.1             %{buildroot}%{_optdir}/libvulkan.so.1
install -Dm 0755 make/linux-unpacked/chrome_100_percent.pak     %{buildroot}%{_optdir}/chrome_100_percent.pak
install -Dm 0755 make/linux-unpacked/chrome_200_percent.pak     %{buildroot}%{_optdir}/chrome_200_percent.pak
install -Dm 0755 make/linux-unpacked/waveterm %{buildroot}%{_optdir}/waveterm
install -Dm 0755 make/linux-unpacked/waveterm %{buildroot}%{_optdir}/waveterm
install -Dm 0755 make/linux-unpacked/waveterm %{buildroot}%{_optdir}/waveterm

%terra_appstream -o %{SOURCE1}

%files
%license LICENSE
%doc README.md ACKNOWLEDGEMENTS.md BUILD.md CODE_OF_CONDUCT.md CONTRIBUTING.md RELEASES.md ROADMAP.md SECURITY.md
%{_bindir}/waveterm
%{_datadir}/%{name}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_optdir}/LICENSE.electron.txt
%{_optdir}/LICENSES.chromium.html
%{_optdir}/chrome-sandbox
%{_optdir}/*.pak
%{_optdir}/chrome_crashpad_handler
%{_optdir}/icudtl.dat
%{_optdir}/*.so
%{_optdir}/libvulkan.so.1
%{_optdir}/locales/*.pak
%{_optdir}/resources.pak
%{_optdir}/resources/app-update.yml
%{_optdir}/resources/app.asar
%{_optdir}/resources/app.asar.unpacked/dist/bin/wavesrv.x64
%{_optdir}/resources/app.asar.unpacked/dist/bin/wsh-0.12.5-darwin.arm64
%{_optdir}/resources/app.asar.unpacked/dist/bin/wsh-0.12.5-darwin.x64
%{_optdir}/resources/app.asar.unpacked/dist/bin/wsh-0.12.5-linux.arm64
%{_optdir}/resources/app.asar.unpacked/dist/bin/wsh-0.12.5-linux.mips
%{_optdir}/resources/app.asar.unpacked/dist/bin/wsh-0.12.5-linux.mips64
%{_optdir}/resources/app.asar.unpacked/dist/bin/wsh-0.12.5-linux.x64
%dnl %{_optdir}/resources/app.asar.unpacked/dist/bin/wsh-0.12.5-windows.arm64.exe
%dnl %{_optdir}/resources/app.asar.unpacked/dist/bin/wsh-0.12.5-windows.x64.exe
%{_optdir}/resources/app.asar.unpacked/dist/schema/*.json
%{_optdir}/resources/apparmor-profile
%{_optdir}/resources/package-type
%{_optdir}/resources/tsunamiscaffold/.gitignore
%{_optdir}/resources/tsunamiscaffold/*.tmpl
%{_optdir}/resources/tsunamiscaffold/dist/assets/index--f3-IlxP.css
%{_optdir}/resources/tsunamiscaffold/dist/assets/index-BtzCONjg.js
%{_optdir}/resources/tsunamiscaffold/dist/assets/wave-logo-256-C_-lEXjS.png
%{_optdir}/resources/tsunamiscaffold/dist/fonts/*.woff2
%{_optdir}/resources/tsunamiscaffold/dist/index.html
%{_optdir}/resources/tsunamiscaffold/dist/tw/errcomponent.go
%{_optdir}/resources/tsunamiscaffold/dist/tw/*.tsx
%{_optdir}/resources/tsunamiscaffold/dist/tw/table.go
%{_optdir}/resources/tsunamiscaffold/dist/wave-logo-256.png
%{_optdir}/resources/tsunamiscaffold/nm/.bin/detect-libc
%{_optdir}/resources/tsunamiscaffold/nm/.bin/jiti
%{_optdir}/resources/tsunamiscaffold/nm/.bin/tailwindcss
%{_optdir}/resources/tsunamiscaffold/nm/.package-lock.json
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/README.md
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/dist/gen-mapping.mjs
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/dist/gen-mapping.mjs.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/dist/gen-mapping.umd.js
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/dist/gen-mapping.umd.js.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/dist/types/*.ts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/package.json
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/src/*.ts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/types/*.cts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/types/*.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/types/*.mts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/gen-mapping/types/*.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/remapping/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/remapping/README.md
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/remapping/dist/remapping.mjs
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/remapping/dist/*.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/remapping/dist/remapping.umd.js
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/remapping/package.json
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/remapping/src/*.ts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/remapping/types/*.cts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/remapping/types/*.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/remapping/types/*.mts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/resolve-uri/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/resolve-uri/README.md
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/resolve-uri/dist/resolve-uri.mjs
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/resolve-uri/dist/*.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/resolve-uri/dist/resolve-uri.umd.js
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/resolve-uri/dist/types/resolve-uri.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/resolve-uri/package.json
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/README.md
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/dist/sourcemap-codec.mjs
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/dist/*.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/dist/sourcemap-codec.umd.js
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/package.json
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/src/*.ts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/src/vlq.ts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/types/*.cts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/types/*.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/sourcemap-codec/types/*.mts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/trace-mapping/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/trace-mapping/README.md
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/trace-mapping/dist/trace-mapping.mjs
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/trace-mapping/dist/*.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/trace-mapping/dist/trace-mapping.umd.js
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/trace-mapping/package.json
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/trace-mapping/src/*.ts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/trace-mapping/types/*.cts
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/trace-mapping/types/*.cts.map
%{_optdir}/resources/tsunamiscaffold/nm/@jridgewell/trace-mapping/types/*.mts
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher-linux-x64-glibc/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher-linux-x64-glibc/README.md
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher-linux-x64-glibc/package.json
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher-linux-x64-glibc/watcher.node
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/README.md
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/binding.gyp
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/*.ts
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/index.js.flow
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/package.json
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/scripts/build-from-source.js
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/Backend.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/Backend.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/Debounce.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/Debounce.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/DirTree.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/DirTree.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/Event.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/Glob.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/Glob.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/PromiseRunner.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/Signal.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/Watcher.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/Watcher.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/binding.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/kqueue/KqueueBackend.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/kqueue/KqueueBackend.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/linux/InotifyBackend.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/linux/InotifyBackend.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/macos/FSEventsBackend.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/macos/FSEventsBackend.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/shared/BruteForceBackend.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/shared/BruteForceBackend.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/unix/fts.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/unix/legacy.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/wasm/WasmBackend.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/wasm/WasmBackend.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/wasm/include.h
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/watchman/BSER.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/watchman/BSER.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/watchman/IPC.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/watchman/WatchmanBackend.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/watchman/WatchmanBackend.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/windows/WindowsBackend.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/windows/WindowsBackend.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/windows/win_utils.cc
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/src/windows/win_utils.hh
%{_optdir}/resources/tsunamiscaffold/nm/@parcel/watcher/wrapper.js
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/cli/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/cli/README.md
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/cli/dist/index.mjs
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/cli/package.json
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/README.md
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/dist/esm-cache.loader.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/dist/esm-cache.loader.mjs
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/dist/index.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/dist/index.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/dist/index.js
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/dist/index.mjs
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/dist/require-cache.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/dist/require-cache.js
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/node/package.json
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/oxide-linux-x64-gnu/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/oxide-linux-x64-gnu/README.md
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/oxide-linux-x64-gnu/package.json
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/oxide-linux-x64-gnu/tailwindcss-oxide.linux-x64-gnu.node
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/oxide/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/oxide/index.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/oxide/index.js
%{_optdir}/resources/tsunamiscaffold/nm/@tailwindcss/oxide/package.json
%{_optdir}/resources/tsunamiscaffold/nm/braces/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/braces/README.md
%{_optdir}/resources/tsunamiscaffold/nm/braces/index.js
%{_optdir}/resources/tsunamiscaffold/nm/braces/lib/compile.js
%{_optdir}/resources/tsunamiscaffold/nm/braces/lib/constants.js
%{_optdir}/resources/tsunamiscaffold/nm/braces/lib/expand.js
%{_optdir}/resources/tsunamiscaffold/nm/braces/lib/parse.js
%{_optdir}/resources/tsunamiscaffold/nm/braces/lib/stringify.js
%{_optdir}/resources/tsunamiscaffold/nm/braces/lib/utils.js
%{_optdir}/resources/tsunamiscaffold/nm/braces/package.json
%{_optdir}/resources/tsunamiscaffold/nm/detect-libc/.npmignore
%{_optdir}/resources/tsunamiscaffold/nm/detect-libc/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/detect-libc/README.md
%{_optdir}/resources/tsunamiscaffold/nm/detect-libc/bin/detect-libc.js
%{_optdir}/resources/tsunamiscaffold/nm/detect-libc/lib/detect-libc.js
%{_optdir}/resources/tsunamiscaffold/nm/detect-libc/package.json
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/README.md
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/AliasFieldPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/AliasPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/AppendPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/CachedInputFileSystem.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/CloneBasenamePlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/ConditionalPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/DescriptionFilePlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/DescriptionFileUtils.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/DirectoryExistsPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/ExportsFieldPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/ExtensionAliasPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/FileExistsPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/ImportsFieldPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/JoinRequestPartPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/JoinRequestPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/LogInfoPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/MainFieldPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/ModulesInHierachicDirectoriesPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/ModulesInHierarchicalDirectoriesPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/ModulesInRootPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/NextPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/ParsePlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/PnpPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/Resolver.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/ResolverFactory.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/RestrictionsPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/ResultPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/RootsPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/SelfReferencePlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/SymlinkPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/SyncAsyncFileSystemDecorator.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/TryNextPlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/UnsafeCachePlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/UseFilePlugin.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/createInnerContext.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/forEachBail.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/getInnerRequest.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/getPaths.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/index.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/util/entrypoints.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/util/identifier.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/util/memoize.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/util/module-browser.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/util/path.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/lib/util/process-browser.js
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/package.json
%{_optdir}/resources/tsunamiscaffold/nm/enhanced-resolve/types.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/fill-range/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/fill-range/README.md
%{_optdir}/resources/tsunamiscaffold/nm/fill-range/index.js
%{_optdir}/resources/tsunamiscaffold/nm/fill-range/package.json
%{_optdir}/resources/tsunamiscaffold/nm/graceful-fs/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/graceful-fs/README.md
%{_optdir}/resources/tsunamiscaffold/nm/graceful-fs/clone.js
%{_optdir}/resources/tsunamiscaffold/nm/graceful-fs/graceful-fs.js
%{_optdir}/resources/tsunamiscaffold/nm/graceful-fs/legacy-streams.js
%{_optdir}/resources/tsunamiscaffold/nm/graceful-fs/package.json
%{_optdir}/resources/tsunamiscaffold/nm/graceful-fs/polyfills.js
%{_optdir}/resources/tsunamiscaffold/nm/is-extglob/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/is-extglob/README.md
%{_optdir}/resources/tsunamiscaffold/nm/is-extglob/index.js
%{_optdir}/resources/tsunamiscaffold/nm/is-extglob/package.json
%{_optdir}/resources/tsunamiscaffold/nm/is-glob/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/is-glob/README.md
%{_optdir}/resources/tsunamiscaffold/nm/is-glob/index.js
%{_optdir}/resources/tsunamiscaffold/nm/is-glob/package.json
%{_optdir}/resources/tsunamiscaffold/nm/is-number/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/is-number/README.md
%{_optdir}/resources/tsunamiscaffold/nm/is-number/index.js
%{_optdir}/resources/tsunamiscaffold/nm/is-number/package.json
%{_optdir}/resources/tsunamiscaffold/nm/jiti/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/jiti/README.md
%{_optdir}/resources/tsunamiscaffold/nm/jiti/dist/babel.cjs
%{_optdir}/resources/tsunamiscaffold/nm/jiti/dist/jiti.cjs
%{_optdir}/resources/tsunamiscaffold/nm/jiti/lib/jiti-cli.mjs
%{_optdir}/resources/tsunamiscaffold/nm/jiti/lib/jiti-hooks.mjs
%{_optdir}/resources/tsunamiscaffold/nm/jiti/lib/jiti-native.mjs
%{_optdir}/resources/tsunamiscaffold/nm/jiti/lib/jiti-register.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/jiti/lib/jiti-register.mjs
%{_optdir}/resources/tsunamiscaffold/nm/jiti/lib/jiti.cjs
%{_optdir}/resources/tsunamiscaffold/nm/jiti/lib/jiti.d.cts
%{_optdir}/resources/tsunamiscaffold/nm/jiti/lib/jiti.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/jiti/lib/jiti.mjs
%{_optdir}/resources/tsunamiscaffold/nm/jiti/lib/types.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/jiti/package.json
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss-linux-x64-gnu/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss-linux-x64-gnu/README.md
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss-linux-x64-gnu/lightningcss.linux-x64-gnu.node
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss-linux-x64-gnu/package.json
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/README.md
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/ast.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/ast.js.flow
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/browserslistToTargets.js
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/composeVisitors.js
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/flags.js
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/index.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/index.js
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/index.js.flow
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/index.mjs
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/targets.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node/targets.js.flow
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node_modules/detect-libc/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node_modules/detect-libc/README.md
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node_modules/detect-libc/index.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node_modules/detect-libc/lib/detect-libc.js
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node_modules/detect-libc/lib/elf.js
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node_modules/detect-libc/lib/filesystem.js
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node_modules/detect-libc/lib/process.js
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/node_modules/detect-libc/package.json
%{_optdir}/resources/tsunamiscaffold/nm/lightningcss/package.json
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/README.md
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/dist/magic-string.cjs.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/dist/magic-string.cjs.js
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/dist/magic-string.cjs.js.map
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/dist/magic-string.es.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/dist/magic-string.es.mjs
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/dist/magic-string.es.mjs.map
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/dist/magic-string.umd.js
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/dist/magic-string.umd.js.map
%{_optdir}/resources/tsunamiscaffold/nm/magic-string/package.json
%{_optdir}/resources/tsunamiscaffold/nm/micromatch/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/micromatch/README.md
%{_optdir}/resources/tsunamiscaffold/nm/micromatch/index.js
%{_optdir}/resources/tsunamiscaffold/nm/micromatch/package.json
%{_optdir}/resources/tsunamiscaffold/nm/mri/index.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/mri/lib/index.js
%{_optdir}/resources/tsunamiscaffold/nm/mri/lib/index.mjs
%{_optdir}/resources/tsunamiscaffold/nm/mri/license.md
%{_optdir}/resources/tsunamiscaffold/nm/mri/package.json
%{_optdir}/resources/tsunamiscaffold/nm/mri/readme.md
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/LICENSE.md
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/README.md
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/common.gypi
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/except.gypi
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/index.js
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/napi-inl.deprecated.h
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/napi-inl.h
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/napi.h
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/node_addon_api.gyp
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/node_api.gyp
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/noexcept.gypi
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/nothing.c
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/package-support.json
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/package.json
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/tools/README.md
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/tools/check-napi.js
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/tools/clang-format.js
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/tools/conversion.js
%{_optdir}/resources/tsunamiscaffold/nm/node-addon-api/tools/eslint-format.js
%{_optdir}/resources/tsunamiscaffold/nm/picocolors/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/picocolors/README.md
%{_optdir}/resources/tsunamiscaffold/nm/picocolors/package.json
%{_optdir}/resources/tsunamiscaffold/nm/picocolors/picocolors.browser.js
%{_optdir}/resources/tsunamiscaffold/nm/picocolors/picocolors.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/picocolors/picocolors.js
%{_optdir}/resources/tsunamiscaffold/nm/picocolors/types.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/picomatch/CHANGELOG.md
%{_optdir}/resources/tsunamiscaffold/nm/picomatch/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/picomatch/README.md
%{_optdir}/resources/tsunamiscaffold/nm/picomatch/index.js
%{_optdir}/resources/tsunamiscaffold/nm/picomatch/lib/constants.js
%{_optdir}/resources/tsunamiscaffold/nm/picomatch/lib/parse.js
%{_optdir}/resources/tsunamiscaffold/nm/picomatch/lib/picomatch.js
%{_optdir}/resources/tsunamiscaffold/nm/picomatch/lib/scan.js
%{_optdir}/resources/tsunamiscaffold/nm/picomatch/lib/utils.js
%{_optdir}/resources/tsunamiscaffold/nm/picomatch/package.json
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/README.md
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/array-set.js
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/base64-vlq.js
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/base64.js
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/binary-search.js
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/mapping-list.js
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/quick-sort.js
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/source-map-consumer.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/source-map-consumer.js
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/source-map-generator.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/source-map-generator.js
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/source-node.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/source-node.js
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/lib/util.js
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/package.json
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/source-map.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/source-map-js/source-map.js
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/README.md
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/chunk-GFBUASX3.mjs
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/chunk-HTB5LLOP.mjs
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/chunk-MEY3PWYT.mjs
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/colors-b_6i0Oi7.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/colors.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/colors.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/colors.js
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/colors.mjs
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/default-theme.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/default-theme.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/default-theme.js
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/default-theme.mjs
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/flatten-color-palette.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/flatten-color-palette.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/flatten-color-palette.js
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/flatten-color-palette.mjs
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/lib.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/lib.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/lib.js
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/lib.mjs
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/plugin.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/plugin.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/plugin.js
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/plugin.mjs
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/resolve-config-BIFUA2FY.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/resolve-config-QUZ9b-Gn.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/dist/types-WlZgYgM8.d.mts
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/index.css
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/package.json
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/preflight.css
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/theme.css
%{_optdir}/resources/tsunamiscaffold/nm/tailwindcss/utilities.css
%{_optdir}/resources/tsunamiscaffold/nm/tapable/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/tapable/README.md
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/AsyncParallelBailHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/AsyncParallelHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/AsyncSeriesBailHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/AsyncSeriesHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/AsyncSeriesLoopHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/AsyncSeriesWaterfallHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/Hook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/HookCodeFactory.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/HookMap.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/MultiHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/SyncBailHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/SyncHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/SyncLoopHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/SyncWaterfallHook.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/index.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/lib/util-browser.js
%{_optdir}/resources/tsunamiscaffold/nm/tapable/package.json
%{_optdir}/resources/tsunamiscaffold/nm/tapable/tapable.d.ts
%{_optdir}/resources/tsunamiscaffold/nm/to-regex-range/LICENSE
%{_optdir}/resources/tsunamiscaffold/nm/to-regex-range/README.md
%{_optdir}/resources/tsunamiscaffold/nm/to-regex-range/index.js
%{_optdir}/resources/tsunamiscaffold/nm/to-regex-range/package.json
%{_optdir}/resources/tsunamiscaffold/package-lock.json
%{_optdir}/resources/tsunamiscaffold/package.json
%{_optdir}/resources/tsunamiscaffold/tailwind.css
%{_optdir}/snapshot_blob.bin
%{_optdir}/v8_context_snapshot.bin
%{_optdir}/vk_swiftshader_icd.json
%{_optdir}/waveterm
/usr/share/applications/waveterm.desktop
/usr/share/icons/hicolor/128x128/apps/waveterm.png
/usr/share/icons/hicolor/16x16/apps/waveterm.png
/usr/share/icons/hicolor/256x256/apps/waveterm.png
/usr/share/icons/hicolor/32x32/apps/waveterm.png
/usr/share/icons/hicolor/48x48/apps/waveterm.png
/usr/share/icons/hicolor/512x512/apps/waveterm.png
/usr/share/icons/hicolor/64x64/apps/waveterm.png

%changelog
* Wed Nov 26 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
