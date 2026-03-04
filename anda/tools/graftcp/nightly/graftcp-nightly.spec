%global commit 340910b3aad0141009ce9f8187ac385e590dae4f
%global commit_date 20260209
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:			graftcp-nightly
Version:		0~%{commit_date}git.%{shortcommit}
Release:		1%?dist
Summary:		A flexible tool for redirecting a given program's TCP traffic to SOCKS5 or HTTP proxy
URL:			https://github.com/hmgle/graftcp
License:		GPL-3.0
Source0:        %url/archive/%commit/graftcp-%commit.tar.gz
BuildRequires:	gcc mold make golang systemd-rpm-macros
Packager:       Owen Zimmerman <owen@fyralabs.com>
Conflicts:      graftcp

%description
graftcp can redirect the TCP connection made by the given program [application, script, shell, etc.] to SOCKS5 or HTTP proxy.

Compared with tsocks, proxychains or proxychains-ng, graftcp is not using the LD_PRELOAD trick which only work for dynamically
linked programs, e.g., applications built by Go can not be hook by proxychains-ng. graftcp can trace or modify any given program's
connect by ptrace(2), so it is workable for any program. The principle will be explained in this paragraph of how does it work.

%prep
%autosetup -n graftcp-%{commit}

%build
%make_build

%install
install -Dm755 graftcp                                      %{buildroot}%{_bindir}/graftcp
install -Dm755 local/graftcp-local                          %{buildroot}%{_bindir}/graftcp-local
install -Dm755 local/mgraftcp                               %{buildroot}%{_bindir}/mgraftcp
install -Dm644 local/contrib/systemd/graftcp-local.service  %{buildroot}%{_unitdir}/graftcp-local.service
install -Dm644 local/example-graftcp-local.conf             %{buildroot}%{_sysconfdir}/graftcp-local/example-graftcp-local.conf

%post
%systemd_post graftcp-local.service

%preun
%systemd_preun graftcp-local.service

%postun
%systemd_postun_with_restart graftcp-local.service

%files
%doc README.md README.zh-CN.md
%license COPYING
%{_bindir}/graftcp
%{_bindir}/graftcp-local
%{_bindir}/mgraftcp
%{_unitdir}/graftcp-local.service
%{_sysconfdir}/graftcp-local/example-graftcp-local.conf

%changelog
* Fri Oct 24 2025 Owen Zimmerman <owen@fyralabs.com>
- initial commit
