# apparmor.d - Full set of apparmor profiles
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 Christian Boltz
# Copyright (C) 2023-2024 Alexandre Pujol <alexandre@pujol.io>
# Copyright (c) 2026 CatPieLeaf <catpieleaf@proton.me>
# SPDX-License-Identifier: GPL-2.0-only

# Warning: for development only, use https://copr.fedorainfracloud.org/coprs/catpieleaf/apparmor.d for production use.

%define _complain 0

%define _disable_source_fetch 0

# Numeric release for the Source0 tag name (v<VERSION>-<tag_release>); must match the git tag
%global tag_release 5

Name:           apparmor.d-fedora
Version:        0.4910.0
Release:        %{tag_release}%{?dist}
Summary:        Full set of AppArmor policies
License:        GPL-2.0-only
URL:            https://github.com/CatPieLeaf/apparmor.d-fedora
Source0:        %{url}/archive/refs/tags/v%{version}-%{tag_release}.tar.gz

Requires:       apparmor-profiles
Requires:       apparmor-parser
Requires:       apparmor-utils
Provides:       apparmor.d
Packager:       CatPieLeaf <catpieleaf@proton.me>
BuildRequires:  just
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
BuildRequires:  curl
BuildRequires:  jq

%description
AppArmor.d is a set of over 1500 AppArmor profiles whose aim is to
confine most Linux based applications and processes.

%if %{_complain}
Built in COMPLAIN mode: violations are logged but not blocked.
Use this mode with aa-logprof for fixing profiles.
%else
Built in ENFORCE mode: violations are actively blocked. Make sure
you have already validated this profile set in complain mode.
%endif

%prep
%autosetup -n apparmor.d-fedora-%{version}-%{tag_release}

%build
%if %{_complain} == 1
just complain
%else
just enforce
%endif

%install
just destdir="%{buildroot}" install-prebuilt
just destdir="%{buildroot}" install-base
just destdir="%{buildroot}" install-tools

%posttrans
apparmor_parser --purge-cache || :
systemctl daemon-reload || :
if systemctl is-active --quiet apparmor.service 2>/dev/null; then
    systemctl try-restart apparmor.service || :
fi

%postun
systemctl daemon-reload || :
if [ $1 -eq 0 ] ; then
    apparmor_parser --purge-cache || :
fi

%files
%license LICENSE
%doc README.md
%config /etc/apparmor.d/
%{_bindir}/aa-log
%{_bindir}/aa-mode

%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_aa-*.zsh
%{_datadir}/bash-completion/completions/aa-*
%doc %{_mandir}/man1/aa-*.1.gz
%doc %{_mandir}/man8/aa-*.8.gz

%dir %{_unitdir}/dbus.service.d
%{_unitdir}/dbus.service.d/apparmor.conf
%dir %{_unitdir}/dbus-broker.service.d
%{_unitdir}/dbus-broker.service.d/apparmor.conf
%dir %{_userunitdir}/dbus.service.d
%{_userunitdir}/dbus.service.d/apparmor.conf
%dir %{_userunitdir}/dbus-broker.service.d
%{_userunitdir}/dbus-broker.service.d/apparmor.conf

%changelog
%(
json=$(curl -fsSL https://api.github.com/repos/CatPieLeaf/apparmor.d-fedora/commits/main)
sha=$(echo "$json" | jq -r '.sha[0:7]')
msg=$(echo "$json" | jq -r '.commit.message | split("\n")[0]' | sed 's/%/%%/g')
echo "* $(date '+%a %b %d %Y') CatPieLeaf <catpieleaf@proton.me> - %{version}-%{release}"
echo "- ${sha}: ${msg}"
)
