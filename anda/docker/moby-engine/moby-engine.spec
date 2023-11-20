# This specfile is licensed under:
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: Fedora Project Authors
# SPDX-FileCopyrightText: 2022 Maxwell G <gotmax@e.email>
# See %%{name}.spec.license for the full license text.

# disable debuginfo for now
%global debug_package %{nil}

# moby
%global goipath_moby github.com/docker/docker
%global git_moby https://%%{goipath_moby}
#%%global commit_moby 9fdeb9c3de2f2d9f5799be373f27b2f9df44609d
#%%global shortcommit_moby %%(c=%%{commit_moby}; echo ${c:0:7})

# cli
%global goipath_cli github.com/docker/cli
%global git_cli https://%%{goipath_cli}
#%%global commit_cli baeda1f82a10204ec5708d5fbba130ad76cfee49
#%%global shortcommit_cli %%(c=%%{commit_cli}; echo ${c:0:7})

# tini
%global git_tini https://github.com/krallin/tini
%global commit_tini 0b44d3665869e46ccbac7414241b8256d6234dc4
%global shortcommit_tini %(c=%{commit_tini}; echo ${c:0:7})

%global anda_go_build go build -buildmode=pie -tags 'osusergo,netgo' -v -x

Name:           moby-engine
Version:        24.0.5
Release:        1%{?dist}
Summary:        The open-source application container engine
License:        Apache-2.0
Source0:        %{git_moby}/archive/v%{version}/moby-%{version}.tar.gz
Source1:        %{git_cli}/archive/v%{version}/cli-%{version}.tar.gz
Source2:        %{git_tini}/archive/%{commit_tini}/tini-%{shortcommit_tini}.tar.gz
Source3:        docker.service
Source4:        docker.sysconfig
Source5:        moby-engine-systemd-sysusers.conf
Source6:        generate-docs.sh

# Seperate file containing virtual provides for bundled deps that's %%include'd in the specfile.
#Source100:      provides.spec.inc
# Specfile license
Source200:      moby-engine.spec.license

URL:            https://www.docker.com

ExclusiveArch:  %{golang_arches}

BuildRequires:  pkgconfig(libbtrfsutil)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  golang
BuildRequires:  go-rpm-macros
BuildRequires:  go-md2man
BuildRequires:  pkgconfig(libseccomp) >= 2.3.0
BuildRequires:  make
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  firewalld-filesystem

# Build dependencies for tini
BuildRequires:  cmake
BuildRequires:  glibc-static

# required packages on install
Requires:       container-selinux
Requires:       containerd
Requires:       iptables
Requires:       pigz
Requires:       runc
Requires:       systemd
Requires:       tar
Requires:       xz

# Resolves: rhbz#1165615
Requires:       device-mapper-libs >= 1.02.90-1

# Replace the old Docker packages
Provides:       docker = %{version}-%{release}
Provides:       docker-latest = %{version}-%{release}

# conflicting packages
Conflicts:      docker-ce
Conflicts:      docker-ce-cli
Conflicts:      docker-common
Conflicts:      docker-ee
Conflicts:      docker-engine-cs
Conflicts:      docker-io
Conflicts:      podman-docker

%description
Docker is an open source project to build, ship and run any application as a
lightweight container.

Docker containers are both hardware-agnostic and platform-agnostic. This means
they can run anywhere, from your laptop to the largest EC2 compute instance and
everything in between - and they don't require you to use a particular
language, framework or packaging system. That makes them great building blocks
for deploying and scaling web apps, databases, and backend services without
depending on a particular stack or provider.

%package fish-completion
Summary:        Fish completion files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       fish
Provides:       docker-fish-completion = %{version}-%{release}

%description fish-completion
This package installs %{summary}.

%package zsh-completion
Summary:        Zsh completion files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Provides:       docker-zsh-completion = %{version}-%{release}

%description zsh-completion
This package installs %{summary}.

%package nano
Summary:        GNU nano syntax highlighting files for Moby
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       nano

%description nano
This package installs %{summary}.

%prep
%setup -q -a 1 -a 2 -n moby-%{version}
ln -s vendor.mod go.mod
#export GOPATH="$PWD"
#go get -x
#go mod vendor
# correct rpmlint errors for bash completion
sed -i '/env bash/d' cli-%{version}/contrib/completion/bash/docker
cp %{SOURCE6} cli-%{version}/scripts/docs/generate-man.sh
%build
mkdir -p _build/bin
export CGO_ENABLED=1

export DISABLE_WARN_OUTSIDE_CONTAINER=1

#go mod download


# build docker-proxy / libnetwork
(

        # Link source and vendored deps into local GOPATH.
        #ln -fns ../../.. src/%{goipath_moby}
        #export GOPATH="${PWD}"
        %anda_go_build -o _build/bin/docker-proxy github.com/docker/docker/cmd/docker-proxy
)

# build tini (installed as docker-init)
(
        cd tini-%{commit_tini}
        %cmake
        make tini-static -C "%{__cmake_builddir}"
)

%global buildtime %(date --utc --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +"%Y-%m-%dT%H:%M:%SZ")
# build engine
(
        mkdir -p src/github.com/docker
        # Link source and vendored deps into local GOPATH.
        ln -fns ../../.. src/%{goipath_moby}
        # Build using source and vendored deps in local GOPATH.
        export GOPATH="${PWD}"
        export GO111MODULE=off
        export LDFLAGS="-w"
        export LDFLAGS+=" -X github.com/docker/docker/dockerversion.Version=%{version}"
        export LDFLAGS+=" -X github.com/docker/docker/dockerversion.GitCommit=%{shortcommit_moby}"
        export LDFLAGS+=" -X github.com/docker/docker/dockerversion.IAmStatic=false"
        export LDFLAGS+=" -X 'github.com/docker/docker/dockerversion.BuildTime=%{buildtime}'"
        export DOCKER_BUILDTAGS="seccomp selinux journald"
        export BUILDTAGS="${DOCKER_BUILDTAGS}"
        export GOBUILDTAGS="${BUILDTAGS}"
        %anda_go_build -o _build/bin/dockerd %{goipath_moby}/cmd/dockerd
        # VERSION=%%{version} DOCKER_GITCOMMIT=%%{shortcommit_moby} bash sh dynbinary
        # mv bundles/dynbinary-daemon/dockerd-%%{version} _build/bin/dockerd
)

# build cli
(
        cd cli-%{version}
        mkdir -p src/github.com/docker
        # Link source and vendored deps into local GOPATH.
        ln -fns ../../.. src/%{goipath_cli}
        # export DISABLE_WARN_OUTSIDE_CONTAINER=1
        # Build using source and vendored deps in local GOPATH.
        export GOPATH="${PWD}"
        export GO111MODULE=off
        export LDFLAGS="\
            -w \
            -X \"github.com/docker/cli/cli/version.GitCommit=%{shortcommit_cli}\" \
            -X \"github.com/docker/cli/cli/version.BuildTime=%{buildtime}\" \
            -X \"github.com/docker/cli/cli/version.Version=%{version}\" \
    "
        export BUILDTAGS="pkcs11"
        export GOBUILDTAGS="${BUILDTAGS}"
        %anda_go_build -o ../_build/bin/docker %{goipath_cli}/cmd/docker
        # make VERSION=%%{version} GITCOMMIT=%%{shortcommit_cli} dynbinary

	scripts/docs/generate-man.sh
)

%install
# install binary
install -Dpm 755 _build/bin/docker _build/bin/dockerd -t %{buildroot}%{_bindir}/

# install proxy
install -Dpm 755 _build/bin/docker-proxy -t %{buildroot}%{_libexecdir}/docker/

# install tini
install -Dpm 755 tini-%{commit_tini}/%{__cmake_builddir}/tini-static %{buildroot}%{_libexecdir}/docker/docker-init

# install udev rules
install -Dpm 644 contrib/udev/80-docker.rules -t %{buildroot}%{_usr}/lib/udev/rules.d/

# add init scripts
install -Dpm 644 %{SOURCE3} contrib/init/systemd/docker.socket -t %{buildroot}%{_unitdir}/

# for additional args
install -Dpm 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/docker

# Install sysusers configuration
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/moby-engine.conf

# add bash, zsh, and fish completions
install -Dpm 644 cli-%{version}/contrib/completion/bash/docker -t %{buildroot}%{_datadir}/bash-completion/completions/
install -Dpm 644 cli-%{version}/contrib/completion/zsh/_docker -t %{buildroot}%{_datadir}/zsh/site-functions/
install -Dpm 644 cli-%{version}/contrib/completion/fish/docker.fish -t %{buildroot}%{_datadir}/fish/vendor_completions.d/

# install manpages
install -Dpm 644 cli-%{version}/man/man1/*.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 644 cli-%{version}/man/man5/*.5 -t %{buildroot}%{_mandir}/man5/
install -Dpm 644 cli-%{version}/man/man8/*.8 -t %{buildroot}%{_mandir}/man8/

# add nano files
install -Dpm 644 contrib/syntax/nano/Dockerfile.nanorc -t %{buildroot}%{_datadir}/nano/

for cli_file in LICENSE MAINTAINERS NOTICE README.md; do
    cp "cli-%{version}/$cli_file" "cli-$cli_file"
done

%pre
%sysusers_create_compat %{SOURCE5}

%post
%systemd_post docker.service docker.socket
%firewalld_reload

%preun
%systemd_preun docker.service docker.socket

%postun
%systemd_postun_with_restart docker.service

%files
%license LICENSE cli-LICENSE
%doc AUTHORS CONTRIBUTING.md MAINTAINERS NOTICE README.md
%doc cli-MAINTAINERS cli-NOTICE cli-README.md
%config(noreplace) %{_sysconfdir}/sysconfig/docker
%{_bindir}/docker
%{_bindir}/dockerd
%dir %{_libexecdir}/docker/
%{_libexecdir}/docker/docker-proxy
%{_libexecdir}/docker/docker-init
%{_usr}/lib/udev/rules.d/80-docker.rules
%{_unitdir}/docker.service
%{_unitdir}/docker.socket
%{_sysusersdir}/moby-engine.conf
%{_datadir}/bash-completion/completions/docker
%{_mandir}/man1/docker*.1*
%{_mandir}/man5/{Dockerfile,docker-config-json}.5*
%{_mandir}/man8/dockerd.8*

%files zsh-completion
%{_datadir}/zsh/site-functions/_docker

%files fish-completion
%{_datadir}/fish/vendor_completions.d/docker.fish

%files nano
%dir %{_datadir}/nano
%{_datadir}/nano/Dockerfile.nanorc

%changelog
* Wed Aug 23 2023 LuK1337 <priv.luk@gmail.com> - 24.0.5-1
- Update moby-engine to 24.0.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 John Ghatas <john@johnghatas.com>
- Update moby-engine to 23.0.4

* Sun Jan 29 2023 Sérgio Basto <sergio@serjux.com>
- Update moby-engine to 20.10.23

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 01 2023 Sérgio Basto <sergio@serjux.com>
- Update moby-engine to 20.10.22

* Wed Dec 14 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 20.10.21-1
- Update to 20.10.21
- Fix build, use libnetwork from golang-github-docker-0:22.06.0~beta

* Thu Oct 20 2022 Jan Kuparinen <copperi@fedoraproject.org> - 20.10.20-1
- Update to 20.10.20.
- Mitigates CVE-2022-39253

* Tue Oct 18 2022 Jan Kuparinen <copperi@fedoraproject.org> - 20.10.19-1
- Update to 20.10.19.

* Sat Sep 10 2022 Maxwell G <gotmax@e.email> - 20.10.18-1
- Update to 20.10.18.
- Mitigates CVE-2022-36109 / GHSA-rc4r-wh2q-q6c4

* Tue Aug 30 2022 Luca BRUNO <lucab@lucabruno.net> - 20.10.17-8
- Move 'docker' group creation logic to a sysusers.d fragment
  Resolves: rhbz#1745936

* Fri Aug 05 2022 Maxwell G <gotmax@e.email> - 20.10.17-7
- Migrate to SPDX license identifiers
- Generate debuginfo
- Specfile improvements

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 20.10.17-5
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Mon Jul 04 2022 Maxwell G <gotmax@e.email> - 20.10.17-4
- Only build on %%golang_arches (i.e. where golang is available).

* Sun Jun 19 2022 Maxwell G <gotmax@e.email> - 20.10.17-3
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629.

* Sat Jun 11 2022 Maxwell G <gotmax@e.email> - 20.10.17-2
- Rebuild for new golang-github-docker-libnetwork

* Fri Jun 10 2022 Maxwell G <gotmax@e.email> - 20.10.17-1
- Update to 20.10.17. Fixes rhbz#2095714.

* Fri May 13 2022 Maxwell G <gotmax@e.email> - 20.10.16-1
- Update to 20.10.16.

* Sat May 07 2022 Maxwell G <gotmax@e.email> - 20.10.15-1
- Update to 20.10.15 (rhbz#2082501).
- Fix BUILDTAGS (rhbz#2082924).
- Make non-binary subpackages noarch.

* Mon Apr 11 2022 Maxwell G <gotmax@e.email> - 20.10.14-1
- Update to 20.10.14. Fixes rhbz#2063052.
- Mitigate CVE-2022-24769.

* Mon Jan 31 2022 Maxwell G <gotmax@e.email> - 20.10.12-3
- Fixes FTBFS. Closes rhbz#2046748.
- Use %%anda_go_build instead of Makefile to build binaries
- Add explanatory comments.
- Normalize install commands
- Make compliant with SourceURL Guidelines
- Remove no longer necessary `ExcludeArch: ppc64`.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Maxwell G <gotmax@e.email> - 20.10.12-1
- Update to 20.10.12. Fixes rhbz#2032534.
- Install zsh completions to the correct directory. Fixes rhbz#2038888.

* Mon Nov 22 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10-11-1
- Update to upstream 20.10.11 (fixes rhbz#2024384)
- Mitigates CVE-2021-41190 (fixes rhbz#2024940)

* Fri Oct 29 2021 Maxwell G <gotmax@e.email> - 20.10.10-1
- Update to 20.10.10 (fixes rhbz#2015385)
- Update virtual provides

* Fri Oct 08 2021 Maxwell G <gotmax@e.email> - 20.10.9-1
- Update to 20.10.9 (fixes rhbz#2010508)
- Patch seccomp policy to fix clone3() issue (fixes rhbz#2011523 and rhbz#1988199)

* Sun Aug 15 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.8-1
- Update to upstream 20.10.8 (fixes rhbz#1990148)
- Fix seccomp support (fixes rhbz#1986092)

* Sun Aug 15 2021 Dusty Mabe <dusty@dustymabe.com> - 20.10.7-3
- Remove `Requires(post)` on firewalld-filesystem.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.7-1
- Update to upstream 20.10.7 (fixes rhbz#1967390)

* Tue May 04 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.6-2
- Add conflict with podman-docker

* Tue Apr 20 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.6-1
- Update to upstream 20.10.6 (#1948605)
- Re-bundle moby dependencies to fix gRPC issues with Swarm
  (https://github.com/coreos/fedora-coreos-tracker/issues/793)

* Sun Mar 14 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.5-1
- Update to latest upstream 20.10.5 - fixes #1903426
- Upstream brings compatibility with cgroups v2 - fixes #1746355
- Remove package moby-engine-vim (dockerfile.vim has been merged in upstream vim)
- Remove firewalld docker zone, since dockerd can now communicate with firewalld - fixes #1852680
- Build dockerd and docker-proxy from unbundled source packages
- Remove fixed storage-driver (cf. https://src.fedoraproject.org/rpms/moby-engine/pull-request/6)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 19.03.13-3.ce.git4484c46
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.13-2.ce.git4484c46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 02 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.13-1.ce.git4484c46
- Update to upstream 19.03.13 (#1837641)

* Fri Oct 02 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.11-4.ce.git42e35e6
- Fix FTBFS: adapt to change to CMake builds (#1864160)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.11-3.ce.git42e35e6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.11-2.ce.git42e35e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.11-1.ce.git42e35e6
- Update to upstream 19.03.11 to prevent CVE-2020-13401

* Thu May 07 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.8-2.ce.gitafacb8b
- Configure storage-driver explicitely (fixes #1832301)
- Add firewalld zone: trust interface docker0, as firewalld now uses nftables
  by default and docker communicates with iptables (fixes #1817022)

* Mon Mar 16 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.8-1.ce.gitafacb8b
- Update to latest upstream release - Docker CE 19.03.8
- Prune unused BuildRequires

* Sun Mar 8 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.7-2.ce.git7141c19
- Add Conflicts with docker-ce-cli and Obsoletes docker-common

* Sat Mar 7 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.7-1.ce.git7141c19
- Update to latest upstream release - Docker CE 19.03.7
- Add Epoch: 2 to Obsoletes for docker and docker-latest

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.09.8-3.ce.git0dd43dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.09.8-2.ce.git0dd43dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.8-1.ce.git0dd43dd
- Update to latest upstream release - Docker CE 18.09.8

* Sat Jul 13 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-5.ce.git2d0083d
- Move docker-init and docker-proxy to /usr/libexec/docker
- Update moby-engine-nano summary to follow guidelines

* Sat Jul 13 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-4.ce.git2d0083d
- Add nofile ulimit to default docker daemon options (#1715254, #1708115)

* Fri Jul 12 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-3.ce.git2d0083d
- rebuilt

* Fri Jul 12 2019 Olivier Lemasle <o.lemasle@gmail.com> - 18.09.7-2.ce.git2d0083d
- Depend on packaged versions "runc" and "containerd" instead of building them.

* Thu Jun 27 2019 David Michael <dm0@redhat.com> - 18.09.7-1.ce.git2d0083d
- Update docker-ce to commit 2d0083d (version 18.09.7).
- Update runc to commit 425e105.
- Update containerd to commit 894b81a (1.2.6).
- Update docker-proxy to commit e7933d4.

* Tue May 14 2019 David Michael <dm0@redhat.com> - 18.09.6-1.ce.git481bc77
- Update docker-ce to commit 481bc77 (version 18.09.6).
- Update docker-proxy to commit 872f0a8.
- Obsolete and provide the docker and docker-latest packages. (#1700006)

* Thu Apr 11 2019 David Michael <dm0@redhat.com> - 18.09.5-1.ce.gite8ff056
- Update docker-ce to commit e8ff056 (version 18.09.5).
- Update docker-runc to commit 2b18fe1.
- Update docker-containerd to commit bb71b10 (version 1.2.5).
- Update docker-proxy to commit 4725f21.
- Report the correct engine version.
- Install symlinks to unprefixed runc/containerd program names.

* Thu Mar 28 2019 David Michael <dm0@redhat.com> - 18.06.3-2.ce.gitd7080c1
- Conflict with docker-common. (#1693397)

* Thu Feb 21 2019 David Michael <dm0@redhat.com> - 18.06.3-1.ce.gitd7080c1
- Update docker-ce to commit d7080c1 (version 18.06.3).

* Tue Feb 12 2019 David Michael <dm0@redhat.com> - 18.06.2-1.ce.git6d37f41
- Update docker-ce to commit 6d37f41 (version 18.06.2).
- Update docker-runc to commit a592beb.

* Mon Feb 11 2019 David Michael <dm0@redhat.com> - 18.06.1-3.ce.gite68fc7a
- Apply a runc patch for CVE-2019-5736.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.06.1-2.ce.gite68fc7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 David Michael <dm0@redhat.com> - 18.06.1-1.ce.gite68fc7a
- Update docker-ce to commit e68fc7a (version 18.06.1).
- Update docker-runc to commit 69663f0.
- Update docker-containerd to commit 468a545 (version 1.1.2).
- Update docker-proxy to commit 3ac297b.
- Backport a fix for mounting named volumes.
- Create a "docker" group for non-root Docker access.
- Support systemd socket-activation.
- Make runc and containerd commit IDs match their expected values.
- Preserve containerd debuginfo.

* Mon Nov 12 2018 Marcin Skarbek <rpm@skarbek.name> - 18.06.0-2.ce.git0ffa825
- add configuration file
- update service file

* Sat Aug 18 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 18.06.0-1.ce.git0ffa825
- Resolves: #1539161 - first upload to Fedora
- built docker-ce commit 0ffa825
- built docker-runc commit ad0f5255
- built docker-containerd commit a88b631
- built docker-proxy commit a79d368
- built docker-init commit fec3683

* Tue Mar 20 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-4.ce.gitf5ec1e2
- correct some rpmlint errors

* Wed Feb 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-3.ce
- docker-* symlinks to moby-* (RE: gh PR 34226)

* Wed Feb 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-2.ce
- rename binaries as per upstream gh PR 34226

* Fri Jan 26 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 17.03.2-1
- initial build
- built moby commit f5ec1e2
- built cli commit 4b61f56
- built docker-runc commit 2d41c047
- built docker-containerd commit 3addd84
- built docker-proxy commit 7b2b1fe
