%global commit      50fad9429ff03e759f8a9405c383339683dbe7f4
%global commitdate  20260805
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global pkgname     nohang
%global ver         0.3.0

Name:           nohang-nightly
Version:        %{ver}^%{commit_date}.git%{shortcommit}
Release:        5%{?dist}
License:        MIT
Summary:        Sophisticated low memory handler for Linux
URL:            https://github.com/hakavlad/nohang
Source0:        %{url}/archive/%{commit}/nohang-%{commit}.tar.gz
Patch0:         10-fix-root-security.patch
Patch1:         11-ignore-zfs-on-lxc.patch
Conflicts:      nohang

Packager:       Mizuki Nguyen <acertaindrizzle@proton.me>

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gettext
%if 0%{?rhel} >= 7
BuildRequires:  systemd
%else
BuildRequires:  systemd-rpm-macros
%endif

Requires:       libnotify logrotate python >= 3.3

%{?systemd_requires}

%description
Nohang is a highly configurable daemon for Linux which is able to correctly
prevent out of memory (OOM) and keep system responsiveness in low memory
conditions.

%prep
%autosetup -p1 -n nohang-%{commit}

%build
# Not required

%install
%make_install \
    BINDIR=%{_bindir} \
    MANDIR=%{_mandir} \
    PREFIX=%{_prefix} \
    SYSCONFDIR=%{_sysconfdir} \
    SYSTEMDUNITDIR=%{_unitdir}

%posttrans
To enable and start for servers:
  systemctl enable --now %{pkgname}
Or for workstations (regular desktop):
  systemctl enable --now %{pkgname}-desktop

%post
%systemd_post %{pkgname}.service %{pkgname}-desktop.service

%preun
%systemd_preun %{pkgname}.service %{pkgname}-desktop.service

%postun
%systemd_postun_with_restart %{pkgname}.service %{pkgname}-desktop.service

%files
%license LICENSE
%{_bindir}/oom-sort
%{_bindir}/psi2log
%{_bindir}/psi-top
%{_sbindir}/%{pkgname}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{pkgname}
%config(noreplace) %{_sysconfdir}/%{pkgname}/%{pkgname}.conf
%config(noreplace) %{_sysconfdir}/%{pkgname}/%{pkgname}-desktop.conf
%{_datadir}/%{pkgname}/%{pkgname}.conf
%{_datadir}/%{pkgname}/%{pkgname}-desktop.conf
%{_datadir}/%{pkgname}/version
%{_datadir}/doc/%{pkgname}/README.md
%{_datadir}/doc/%{pkgname}/CHANGELOG.md
%{_mandir}/man1/*.1.*
%{_mandir}/man8/*.8.*
%{_unitdir}/%{pkgname}.service
%{_unitdir}/%{pkgname}-desktop.service


%changelog
* Sun Oct 25 2026 Mizuki Nguyen <acertaindrizzle@proton.me> - 0.3.0_20260805.git50fad94-5
- Packaging: fix .rhai version format

* Sat Oct 24 2026 Mizuki Nguyen <acertaindrizzle@proton.me> - 0.3.0_20260805.git50fad94-4
- Combine the -desktop files in, "nohang-nightly-desktop" is unintuitive and legacy

* Sat Oct 24 2026 Mizuki Nguyen <acertaindrizzle@proton.me> - 0.3.0_20260805.git50fad94-3
- * Apply PRs:
  * #158: fix: user-controlled process/service names can affect root command arguments
  * #160: implement ignore_zfs inside lxc

* Fri Oct 23 2026 Mizuki Nguyen <acertaindrizzle@proton.me> - 0.3.0_20260805.git50fad94-2
- Update maintainer contact info

* Wed Sep 02 2026 Mizuki Nguyen <acertaindrizzle@proton.me> - 0.3.0_20260805.git50fad94-1
- Update to HEAD
- * Makefile patch fixed upstream
  * Add support for doas instead of sudo
  * Protect phosh and phoc
  * Fix notification: https://github.com/hakavlad/nohang/issues/147
  * Fix ignore_positive_oom_score_adj option may not work properly on Linux 5.9+

* Thu Jan 01 2026 Mizuki Nguyen <acertaindrizzle@proton.me> - 0.3.0-1
- build(update): 0.3.0
- Patch Makefile to merge /sbin into /bin

* Sun May 02 2021 ElXreno <elxreno@gmail.com> - 0.2.0-5
- Don't install some docs via Makefile

* Sun May 02 2021 ElXreno <elxreno@gmail.com> - 0.2.0-4
- * Format spec
  * Replace git command via echo in Makefile
  * Don't exec chcon in Makefile
  * Don't exec systemctl in Makefile
  * Disable search of debuginfo
  * Drop not required build macros

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1
- build(update): 0.2.0

* Sun Sep 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-33.20200919gitfaf49b0
- Update to latest git snapshot

* Mon Aug 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-32.20200809git2500c6c
- Update to latest git snapshot

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-31.20200612git271c04d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-30.20200612git271c04d
- Update to latest git snapshot

* Wed May 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-29.20200506git4cf9810
- Update to latest git snapshot

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-28.20200504gita794396
- Update to latest git snapshot

* Sun Apr 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-27.20200426git45b15aa
- Update to latest git snapshot
- Update summary, sync with upstream

* Fri Apr 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-26.20200403git18f90d7
- Update to latest git snapshot

* Mon Mar 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-25.20200323gitdaca5cc
- Update to latest git snapshot

* Tue Mar 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-24.20200317gitc70b824
- Update to latest git snapshot

* Fri Feb 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-23.20200228git2928709
- Update to latest git snapshot

* Fri Feb 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-22.20200221git8cc7c63
- Update to latest git snapshot

* Tue Feb 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-21.20200218git4925df0
- Update to latest git snapshot

* Sun Feb 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-20.20200202gite6eace7
- Update to latest git snapshot

* Fri Jan 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-19.20200131git6fb0324
- Update to latest git snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18.20191203git6389a06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-17.20191203git6389a06
- Update to latest git snapshot

* Sun Nov 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-16.20191117gitaef8af6
- Update to latest git snapshot

* Mon Oct 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-15.20191005git2a3209c
- Update to latest git snapshot

* Sat Sep 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-15.20190919git286ed84
- Fix BR: systemd required for EPEL8

* Thu Sep 19 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-14.20190919git286ed84
- Update to latest git snapshot

* Tue Sep 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-10.20190910gite442e41
- Update to latest git snapshot
- Add 'desktop' package

* Thu Sep 05 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-8.20190905git6db1833
- Update to latest git snapshot

* Sun Sep 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-7.20190901git4c1b5ee
- Update to latest git snapshot

* Sat Aug 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-5.20190831gitf3baa58
- Initial package
