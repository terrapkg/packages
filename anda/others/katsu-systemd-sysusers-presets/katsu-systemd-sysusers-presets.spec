%define debug_package %nil

Name:			katsu-systemd-sysusers-presets
Version:		1.0
Release:		%autorelease
Summary:		A set of systemd system user presets to supplement Fedora's defaults
License:		GPLv3+
Source0:		polkit.conf
Source1:		rpcbind.conf
BuildRequires:  systemd-rpm-macros
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd 


%description
A set of systemd system user presets to supplement Fedora's defaults,
Since for some packages, the system users are created using the package's
post-install script, this package is a no-op on its own. It is intended to be
used as a dependency for other packages that need to create system users.
For example, Polkit needs to create the polkitd system user, so this package
generates the polkitd system user for Polkit to use properly.

Katsu uses this package to fix Fedora's default system user presets, which
fails to add the system users for Polkit and rpcbind.

%package polkit
Summary:		Polkit system user
Requires:       rpcbind

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd 

Supplements:    polkit

%description polkit
Polkit system user preset

%package rpcbind
Summary:		RPC bind system user
Requires:       rpcbind

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Supplements:    rpcbind

%description rpcbind
RPC bind system user preset

%prep

%install
install -D %{SOURCE0} %{buildroot}%{_sysusersdir}/katsu-polkit.conf
install -D %{SOURCE1} %{buildroot}%{_sysusersdir}/katsu-rpcbind.conf

%post polkit
systemd-sysusers %{_sysusersdir}/katsu-polkit.conf

%post rpcbind
systemd-sysusers %{_sysusersdir}/katsu-rpcbind.conf


%files polkit
%{_sysusersdir}/katsu-polkit.conf
%files rpcbind
%{_sysusersdir}/katsu-rpcbind.conf

%changelog
%autochangelog