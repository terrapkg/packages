# BPF-based auto-tuning SPEC file

%define pcpdir	    %{_sharedstatedir}/pcp/pmdas

%global ver 0.4-2
%global releaseS %(echo '%ver' | sed -E 's/^[^-]+-//')
%define upstream_name bpftune

%undefine __brp_add_determinism

%bcond_with openrc

%global commit f562f776aac16478a2eeae1bf4871a66dd0070c3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260819

Name:           bpftune-gaming
Version:        %(echo '%ver' | sed 's/-/~/g')^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        BPF/tracing tools for auto-tuning Linux, with a gaming tuner
License:        GPL-2.0-only WITH Linux-syscall-note
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
URL:            https://github.com/KyleGospo/bpftune
Conflicts:      bpftune
Conflicts:      bpftune-nightly

Source0:        %{url}/archive/%{commit}/%{upstream_name}-%{commit}.tar.gz

Group:          Development/Tools
Requires:       libbpf >= 0.6
Requires:       libnl3
Requires:       libcap
BuildRequires:  libbpf-devel >= 0.6
BuildRequires:  libcap-devel
BuildRequires:	bpftool >= 4.18
BuildRequires:  libnl3-devel
BuildRequires:  clang >= 11
BuildRequires:  clang-libs >= 11
BuildRequires:  llvm >= 11
BuildRequires:  llvm-libs >= 11
BuildRequires:	python3-docutils

%description
Service consisting of daemon (bpftune) and plugins which
support auto-tuning of Linux via BPF observability.

This build includes work by Shane Fagan to enable
automatic tuning for gaming related networking.

%package devel
Requires:   %{name} = %{evr}
Requires:   libbpf-devel >= 0.6
Requires:   libcap-devel
Requires:   bpftool
Requires:   libnl3-devel

%pkg_devel_files

%package pcp-pmda
Summary:	Performance Co-Pilot PMDA for bpftune
Requires:   %{name} = %{evr}
Requires:	pcp
Requires:   python3-pcp 

%description pcp-pmda
The %{name}-pcp-pmda exports tunables and metrics from bpftune
to Performance Co-Pilot (PCP)

%prep
%autosetup -n %{upstream_name}-%{commit}

%build
%make_build

%install
%make_install SBINPATH=%{_bindir}
# Upstream hardcodes /usr/sbin in the unit file
sed -i 's|/usr/sbin/bpftune|%{_bindir}/bpftune|' %{buildroot}%{_unitdir}/bpftune.service

%post
%systemd_post bpftune.service

%preun
%systemd_preun bpftune.service

%postun
%systemd_postun_with_restart bpftune.service

%files
%doc README.md TROUBLESHOOTING.md SECURITY.md docs/bpftune-gaming.rst
%license LICENSE.txt
%defattr(-,root,root)
%config %{_sysconfdir}/ld.so.conf.d/libbpftune.conf
%{_bindir}/bpftune
%{_unitdir}/bpftune.service
%{_libdir}/libbpftune.so.%(echo '%ver' | sed 's/-/./g')
%{_libdir}/bpftune/*
%{_mandir}/*/*
%if %{with openrc}
%{_sysconfdir}/conf.d/bpftune
%{_sysconfdir}/init.d/bpftune
%else
%exclude %{_sysconfdir}/conf.d/bpftune
%exclude %{_sysconfdir}/init.d/bpftune
%endif

%files pcp-pmda
%{pcpdir}/%{upstream_name}/*

%changelog
* Wed Aug 19 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.4-2
- Initial package release
