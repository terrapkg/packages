%define debug_package %{nil}

Name:			graftcp
Version:		0.8.2
Release:		1%{?dist}
Summary:		A flexible tool for redirecting a given program's TCP traffic to SOCKS5 or HTTP proxy
URL:			https://github.com/hmgle/graftcp
License:		GPL-3.0-or-later
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	gcc make golang systemd-rpm-macros
Packager:       Owen Zimmerman <owen@fyralabs.com>
Conflicts:      graftcp-nightly

%description
graftcp can redirect the TCP connection made by the given program [application, script, shell, etc.] to SOCKS5 or HTTP proxy.

Compared with tsocks, proxychains or proxychains-ng, graftcp is not using the LD_PRELOAD trick which only work for dynamically
linked programs, e.g., applications built by Go can not be hook by proxychains-ng. graftcp can trace or modify any given program's
connect by ptrace(2), so it is workable for any program. The principle will be explained in this paragraph of how does it work.

%prep
%autosetup

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{_prefix}
install -Dm644 example-graftcp.conf             %{buildroot}%{_sysconfdir}/graftcp/example-graftcp.conf
install -Dm644 example-mgraftcp.conf            %{buildroot}%{_sysconfdir}/graftcp/example-mgraftcp.conf

%files
%doc README.md
%lang(zh_CN) %doc README.zh-CN.md
%license COPYING
%{_bindir}/graftcp
%{_bindir}/mgraftcp
%{_sysconfdir}/graftcp/example-graftcp.conf
%{_sysconfdir}/graftcp/example-mgraftcp.conf

%changelog
* Tue Jun 02 2026 Owen Zimmerman <owen@fyralabs.com> - 0.8.0-1
- Update for 0.8.0

* Fri Oct 24 2025 Owen Zimmerman <owen@fyralabs.com>
- initial commit
