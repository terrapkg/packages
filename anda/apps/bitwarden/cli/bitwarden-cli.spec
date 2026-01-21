%define debug_package %nil
%global __strip /bin/true

%ifarch aarch64
%global armsuffix -arm64
%endif

Name:           bitwarden-cli
Version:        2025.12.1
Release:        1%?dist
Summary:        Bitwarden command-line client
License:        GPL-3.0-only
URL:            https://bitwarden.com
Source0:        https://github.com/bitwarden/clients/archive/refs/tags/cli-v%version.tar.gz

Packager:       madonuko <mado@fyralabs.com>
Provides:       bw

BuildRequires:  nodejs-npm
BuildRequires:  gcc-c++ gcc make

%description
%summary.

%prep
%autosetup -n clients-cli-v%version
npm i

%build
pushd apps/cli
npm i
npm run dist:oss:lin%?armsuffix

%install
install -Dm755 apps/cli/dist/oss/linux%?armsuffix/bw -t %buildroot%_bindir

%files
%doc README.md SECURITY.md CONTRIBUTING.md
%license LICENSE.txt LICENSE_GPL.txt LICENSE_BITWARDEN.txt
%_bindir/bw
