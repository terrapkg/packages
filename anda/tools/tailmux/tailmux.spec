%if 0%{?fedora} <= 44
%define debug_package %{nil}
%endif

%undefine __brp_mangle_shebangs

%global goipath github.com/GrowlyX/tailmux
Version:        1.2.0

%gometa -f

Name:           tailmux
Release:        1%{?dist}
Summary:        Be on all your tailnets at once

License:        BSD-3-Clause
URL:            https://github.com/GrowlyX/tailmux
Source0:        https://github.com/GrowlyX/tailmux/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
BuildRequires:  tauri
BuildRequires:  %{tauri_buildrequires}
BuildRequires:  pnpm

%description
%{summary}.

%gopkg

%package        desktop
Summary:        Desktop app for tailmux
Requires:       %{name} = %{evr}
SourceLicense:  BSD-3-Clause
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND (Apache-2.0 OR ISC OR MIT) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND CDLA-Permissive-2.0 AND Zlib AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND Unicode-3.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND Apache-2.0 AND ISC AND (BSD-3-Clause OR Apache-2.0) AND BSD-3-Clause AND MIT AND BSL-1.0 AND ISC AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

%description    desktop
Desktop app for tailmux.

%prep
%autosetup -C
pushd desktop
%tauri_prep
popd

%build
%define gomodulesmode GO111MODULE=on
%if 0%{?fedora} <= 44
export GOTOOLCHAIN=auto
%endif
%gobuild -o %{gobuilddir}/cmd/tailmux %{goipath}/cmd/tailmux

pushd desktop
%{tauri_cargo_license} > ../LICENSE.dependencies
%{pnpm_build}
popd

%install
install -Dm755 %{gobuilddir}/cmd/tailmux            %{buildroot}%{_bindir}/tailmux
install -Dm755 desktop/src-tauri/target/rpm/tailmux-desktop   %{buildroot}%{_bindir}/tailmux-desktop
install -Dm644 desktop/src-tauri/icons/icon.png     %{buildroot}%{_hicolordir}/512x512/apps/tailmux.png
%desktop_file_install packaging/linux/tailmux.desktop

%files
%license LICENSE LICENSE.dependencies
%doc README.md docs/*.md SECURITY.md
%{_bindir}/tailmux

%files desktop
%license LICENSE.dependencies
%{_bindir}/tailmux-desktop
%{_hicolordir}/512x512/apps/tailmux.png
%{_appsdir}/tailmux.desktop

%changelog
* Fri Dec 05 2025 Owen Zimmerman <owen@fyralabs.com> - 1.2.0-1
- Initial commit
