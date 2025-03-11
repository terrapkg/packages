%bcond check 0
%global __brp_mangle_shebangs %{nil}

# https://github.com/loft-sh/devpod
%global goipath         github.com/loft-sh/devpod
Version:                0.6.15

%gometa -f

%global common_description %{expand:
Codespaces but open-source, client-only and unopinionated: Works with any IDE
and lets you use any cloud, kubernetes or just localhost docker.}

%global golicenses      LICENSE
%global godocs          docs examples COMMUNITY.md CONTRIBUTING.md README.md\\\
                        SECURITY.md desktop/README.md e2e/README.md\\\
                        loadtest/README.md

Name:           devpod
Release:        1%?dist
Summary:        Codespaces but open-source, client-only and unopinionated: Works with any IDE and lets you use any cloud, kubernetes or just localhost docker
Provides:       golang-github-loft-sh-devpod
BuildRequires:  anda-srpm-macros mold
BuildRequires:  yarnpkg rust-packaging
Recommends:     devpod-desktop

License:        MPL-2.0
URL:            https://devpod.sh
Source:         %{gosource}
# gendesk --pkgname=DevPod --name=DevPod --exec=/usr/bin/DevPod --icon=devpod.png --categories='Utility;TextEditor;Development;IDE' --mimetypes='text/plain;application/x-zerosize' -n
Source1:        DevPod.desktop

%description %{common_description}

%package desktop
Summary: %summary
License: ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSL-1.0 AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND ISC AND MIT AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR NCSA) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(javascriptcoregtk-4.1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)

%description desktop %{common_description}

%prep
#yarn set version 1.22.1
%autosetup -n %name-%version
rm go.sum
cd desktop/src-tauri
%cargo_prep_online
sed -i '/"targets"/s@"all"@[]@' tauri.conf.json

sed -i '/Comment=/s@DevPod@%summary@' %{S:1}

%build
%define gomodulesmode GO111MODULE=on
# just remove -v -x for godsake
%define gobuild_baseflags %{gocompilerflags} -tags="rpm_crashtraceback ${GO_BUILDTAGS-${BUILDTAGS-}}" -a
%define gobuild_ldflags -s -w -X github.com/loft-sh/devpod/pkg/version.version="v%version" ${GO_LDFLAGS-${LDFLAGS-}} %{?currentgoldflags} -B 0x$(echo "%{name}-%{version}-%{release}-${SOURCE_DATE_EPOCH:-}" | sha1sum | cut -d ' ' -f1) -compressdwarf=false -linkmode=external -extldflags '%{build_ldflags} %{?__golang_extldflags}'
%define gobuilddir %_builddir/%buildsubdir
# build cli
(%{gobuild -o %{gobuilddir}/bin/devpod .}) &

pushd desktop
yarn version --new-version %version --no-git-tag-version &
yarn install &
pushd src-tauri
# cargo licenses
%{cargo_license_summary_online} &
%{cargo_license_online} > %_builddir/%buildsubdir/LICENSE.dependencies &
wait
cp %{gobuilddir}/bin/devpod bin/devpod-cli-%_arch-unknown-linux-gnu
popd # src-tauri
# ≈ %%cargo_build
/usr/bin/env CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 RUSTFLAGS='%{build_rustflags}' \
	yarn run desktop:build -- -- %{__cargo_common_opts} --profile rpm
popd # desktop


%install
# go
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp bin/devpod          %{buildroot}%{_bindir}/
# tauri
install -Dm755 "desktop/src-tauri/target/rpm/DevPod Desktop" %buildroot%_bindir/DevPod-Desktop
install -Dm644 %{S:1} -t %buildroot%_datadir/applications/
install -Dm644 desktop/devpod.png -t %buildroot%_datadir/pixmaps/

%files
%license LICENSE
%doc README.md SECURITY.md
%{_bindir}/devpod

%files desktop
%_bindir/DevPod-Desktop
%_datadir/applications/DevPod.desktop
%_datadir/pixmaps/devpod.png
