Name:           youki
Version:        0.4.1
Release:        1%?dist
Summary:        A container runtime written in Rust

License:        Apache-2.0
URL:            https://github.com/containers/youki
Source0:        https://github.com/containers/youki/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  pkg-config
BuildRequires:  rust-packaging
BuildRequires:  anda-srpm-macros
BuildRequires:  systemd-devel
BuildRequires:  git-core
BuildRequires:  dbus-devel
BuildRequires:  libseccomp-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  binutils
BuildRequires:  fdupes
BuildRequires:  mold

%description
youki is an implementation of the OCI runtime-spec in Rust, similar to runc.

%prep
%setup -q -n youki-%{version}

git init .
git remote add origin https://github.com/containers/youki
git fetch origin
git config user.name "username"
git config user.email "dunno@idk.com"
git add * .*
git commit -a -m "idk"
git checkout v%{version}

# add host key for github
# mkdir -p ~/.ssh
# ssh-keyscan github.com >> ~/.ssh/known_hosts

#git submodule set-url integration_tests/oci-runtime-tests https://github.com/opencontainers/runtime-tools
#git submodule sync

# download git submodules
git submodule update --init --recursive

%cargo_prep_online


%build
%cargo_build


%install
ls target/*
install -D -m 0755 target/rpm/youki %{buildroot}%{_bindir}/youki
%fdupes docs/

%files
%license LICENSE
%doc docs
%{_bindir}/youki


%changelog
* Wed Oct 05 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.0.5-1
- Initial Release
