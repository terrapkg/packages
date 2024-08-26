# This is a simplified version of the containerd.spec file from Fedora
# designed to build from upstream containerd, not Fedora

# Created due to https://bugzilla.redhat.com/show_bug.cgi?id=2237396

%global debug_package %{nil}

# https://github.com/containerd/containerd
%global goipath         github.com/containerd/containerd
Version:                1.7.21

%gometa

%global goname          containerd
%global godevelname     containerd-devel

%global common_description %{expand:
Containerd is an industry-standard container runtime with an emphasis on
simplicity, robustness and portability. It is available as a daemon for Linux
and Windows, which can manage the complete container lifecycle of its host
system: image transfer and storage, container execution and supervision,
low-level storage and network attachments, etc.}

%global golicenses      LICENSE NOTICE
%global godocs          docs ROADMAP.md SCOPE.md code-of-conduct.md\\\
                        BUILDING.md README.md RELEASES.md

Name:           %{goname}
Release:        1%?dist
Summary:        Open and reliable container runtime

License:        Apache-2.0
URL:            https://github.com/containerd/containerd
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/containerd-%{version}.tar.gz
Source2:        containerd.toml
# Carve out code requiring github.com/Microsoft/hcsshim
#Patch0:         0001-Revert-commit-for-Windows-metrics.patch
#Patch1:         0002-Remove-windows-only-dep.patch
# Backport for github.com/containerd/typeurl update
#Patch2:         0001-Use-typeurl.Any-instead-of-github.com-gogo-protobuf-.patch
# To use with latest go-runc
#Patch3:         0001-Add-reaper-StartLocked.patch
# To use with latest opencontainers/image-spec
#Patch4:         0001-opencontainers-image-spec-v1.1.0-rc3.patch

BuildRequires:  btrfs-progs-devel
BuildRequires:  go-md2man
BuildRequires:  systemd-rpm-macros
BuildRequires:  git-core

Requires:       runc

%description
%{common_description}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goname} prefix.

%prep
%autosetup -p1 -n %{goname}-%{version}
# Used only for generation:
#rm -rf cmd/protoc-gen-gogoctrd
# Replace default bin directory
sed -i "s|/usr/local/bin/containerd|/usr/bin/containerd|" containerd.service

%build
#pushd containerd
export GOFLAGS="-buildmode=pie -v -x"
%make_build
mkdir _man
go-md2man -in docs/man/containerd-config.8.md -out _man/containerd-config.8
go-md2man -in docs/man/containerd-config.toml.5.md -out _man/containerd-config.toml.5
go run cmd/gen-manpages/main.go containerd.8 _man
go run cmd/gen-manpages/main.go ctr.8 _man

%install
export GOFLAGS="-buildmode=pie -v -x"
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}

	
	
install -D -p -m 0644 _man/containerd.8 %{buildroot}%{_mandir}/man8/containerd.8	
install -D -p -m 0644 _man/containerd-config.8 %{buildroot}%{_mandir}/man8/containerd-config.8
install -D -p -m 0644 _man/ctr.8 %{buildroot}%{_mandir}/man8/ctr.8
install -D -p -m 0644 _man/containerd-config.toml.5 %{buildroot}%{_mandir}/man5/containerd-config.toml.5
install -D -p -m 0644 containerd.service %{buildroot}%{_unitdir}/containerd.service
install -D -p -m 0644 %{S:2} %{buildroot}%{_sysconfdir}/containerd/config.toml
mkdir -p %{buildroot}%{_sharedstatedir}/containerd/opt

%post
%systemd_post containerd.service

%preun
%systemd_preun containerd.service

%postun
%systemd_postun_with_restart containerd.service



%files
%license LICENSE NOTICE
%doc docs ROADMAP.md SCOPE.md code-of-conduct.md BUILDING.md
%doc README.md RELEASES.md
%{_bindir}/*
%{_mandir}/man8/containerd.8*
%{_mandir}/man8/containerd-config.8*
%{_mandir}/man8/ctr.8*
%{_mandir}/man5/containerd-config.toml.5*
%{_unitdir}/containerd.service
%dir %{_sysconfdir}/containerd
%config(noreplace) %{_sysconfdir}/containerd/config.toml
%dir %{_sharedstatedir}/containerd
%dir %{_sharedstatedir}/containerd/opt


%changelog
%autochangelog
