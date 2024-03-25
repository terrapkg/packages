# vim: sw=4:ts=4:et
# Rustdesk will be added later, but for now this supplements the
# external rustdesk package

%define relabel_files() \
restorecon -R /usr/lib/rustdesk/rustdesk; \

%define selinux_policyver 38.28-1

Name:   rustdesk-selinux
Version:	1.0
Release:	1%{?dist}
Summary:	SELinux policy module for rustdesk

Group:	System Environment/Base		
License:	GPLv2+	
URL:		http://rustdesk.com
Source0:	rustdesk.te

Requires: policycoreutils, libselinux-utils
BuildRequires: policycoreutils, libselinux-utils, checkpolicy
Supplements: rustdesk
Enhances: rustdesk
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for rustdesk.

%build
checkmodule -M -m -o rustdesk.mod %{SOURCE0}
semodule_package -o rustdesk.pp -m rustdesk.mod


%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 rustdesk.pp %{buildroot}%{_datadir}/selinux/packages



%post
semodule -n -i %{_datadir}/selinux/packages/rustdesk.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files

fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r rustdesk
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files

    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/rustdesk.pp


%changelog
* Sun Oct  1 2023 Cappy Ishihara <cappy@fyralabs.com> 1.0-1
- Initial version

