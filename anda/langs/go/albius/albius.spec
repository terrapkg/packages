%define debug_package %nil
%global commit f7a1c8106dbc70020aa9e9df27efef81ed394139
%global commit_date 20240811
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           albius
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        A Linux installer backend with support for SquashFS and OCI installations
License:        GPL-3.0
URL:            https://github.com/Vanilla-OS/Albius
Source0:        %url/archive/%commit/albius-%commit.tar.gz
BuildRequires:  go anda-srpm-macros btrfs-progs-devel pkgconfig(devmapper) pkgconfig(gpgme) lvm2 gcc

%description
Albius is a Linux installer backend originally designed for Vanilla OS,
but capable of handling any Linux distribution that uses either Squashfs
or OCI images for distributing the base system. Albius is written entirely
in Go and uses a recipe system (see "recipes" subsection) for describing
operations, mountpoints and options.

%prep
%autosetup -n Albius-%commit
go mod download

%build
mkdir -p build/bin
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n') -s -w" -buildmode=pie -o build/bin/albius .

%install
mkdir -p %{buildroot}%{_bindir}/
install -pm755 build/bin/albius %{buildroot}%{_bindir}/

%files
%_bindir/albius

%changelog
%autochangelog
