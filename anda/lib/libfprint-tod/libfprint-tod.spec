%global debug_package       %{nil}
%define relabel_files()     restorecon -R /usr/libexec/fprintd;
%define selinux_policyver   41.31-1
%define major_version       1.0
%define release_version     3

Name:       fprintd_tod_selinux
Version:	%{major_version}
Release:	%{release_version}%{?dist}
Summary:	SELinux policy module for fprintd_tod

Group:	    System Environment/Base
License:	GPLv2+
URL:		https://github.com/ferdiu/fprintd_tod_selinux
Source0:	https://github.com/ferdiu/fprintd_tod_selinux/archive/refs/tags/v%{major_version}-%{release_version}.tar.gz


Requires: policycoreutils-python-utils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils-python-utils
Requires(postun): policycoreutils-python-utils
BuildRequires: make, selinux-policy-devel
BuildArch: noarch

%description
This package installs and sets up the SELinux
policy security module for fprintd_tod.

%prep
%setup -q -n fprintd_tod_selinux-%{major_version}-%{release_version}

%build
make -f /usr/share/selinux/devel/Makefile fprintd_tod.pp

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 fprintd_tod.pp %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}/etc/selinux/targeted/contexts/users/

%post
semodule -n -i %{_datadir}/selinux/packages/fprintd_tod.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files
fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r fprintd_tod
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files
    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/fprintd_tod.pp


%changelog
* Fri Feb 7 2025 Federico Manzella <ferdiu.manzella@gmail.com> 1.0-1
- Initial version
