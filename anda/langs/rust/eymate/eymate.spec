Name:           eymate
Version:        0.0.1
Release:        1%?dist
Summary:        An Linux alternative to Windows facial IR login, simular to Howdy
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND CC0-1.0 AND GPL-3.0 AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
SourceLicense:  MIT OR Apache-2.0
URL:            https://github.com/LDprg/eyMate
Source0:        %url/archive/refs/tags/v%version.tar.gz
Source1:        https://github.com/timesler/facenet-pytorch/archive/refs/tags/v2.5.3.tar.gz
BuildRequires:  rpm_macro(cargo_install)
BuildRequires:  python
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(torchvision)
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(opencv)
BuildRequires:  git-core
BuildRequires:  gcc-c++ gcc
Requires:       python3dist(torch)

%description
%summary.

%prep
%autosetup -n eyMate-%version
%cargo_prep_online
cargo rm tch
cargo add tch@0.18.0
mkdir facenet_pytorch
cd facenet_pytorch
tar xf %{S:1} --strip-components=1

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies
python build_model.py

%install
export LIBTORCH_USE_PYTORCH=1
export LIBTORCH_BYPASS_VERSION_CHECK=1
%cargo_install
install -Dm644 target/rpm/libpam_eymate.so -t %buildroot%_usr/lib/security/
install -Dm755 vggface2.pt -t %buildroot%_datadir/eymate/

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%_bindir/eymate
%_datadir/eymate/
%_usr/lib/security/libpam_eymate.so
