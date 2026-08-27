%global commit ba38ca2880f497cc7ad8c83dd2e1c2911fd36ff6
%global commit_date 20260826
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define debug_package %nil

Name:           chawan-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        TUI web (and (S)FTP, Gopher, Gemini, ...) browser with CSS, inline image and JavaScript support
URL:            https://git.sr.ht/~bptato/chawan
Source0:        %{url}/archive/%{commit}.tar.gz
License:        Unlicense
BuildRequires: nim
BuildRequires: gcc
BuildRequires: libssh2-devel
BuildRequires: openssl-devel
BuildRequires: brotli-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: make
Conflicts:     chawan
Packager: apolunar <ijholm@tuta.io>

%description
TUI web (and (S)FTP, Gopher, Gemini, ...) browser with CSS, inline image and JavaScript support.

It uses its own small browser engine developed from scratch,
which can nevertheless display many websites in a manner similar to major graphical browsers.

It can also be used as a terminal pager.

%prep
%autosetup -n chawan-%{commit}

%build
%make_build

%install
%make_install PREFIX=/usr

%files
%{_bindir}/cha
%{_bindir}/mancha
%{_libexecdir}/chawan/
%{_mandir}/man1/cha.1.*
%{_mandir}/man1/mancha.1.*
%{_mandir}/man5/cha-config.5.*
%{_mandir}/man5/cha-mailcap.5.*
%{_mandir}/man5/cha-mime.types.5.*
%{_mandir}/man5/cha-urimethodmap.5.*
%{_mandir}/man5/cha-cgi.5.*
%{_mandir}/man7/cha-api.7.*
%{_mandir}/man7/cha-css.7.*
%{_mandir}/man7/cha-image.7.*
%{_mandir}/man7/cha-protocols.7.*
%{_mandir}/man7/cha-terminal.7.*
%{_mandir}/man7/cha-troubleshooting.7.*
%license UNLICENSE
%doc README.md

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com>
- Split into nightly and stable

* Fri Mar 20 2026 apolunar <ijholm@tuta.io>
- Initial commit
