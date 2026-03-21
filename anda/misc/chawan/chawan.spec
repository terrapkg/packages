%global commit 2723e63772e83595c22ac0691aa5b018f2305a05
%global commit_date 20251210
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define debug_package %nil

Name:           chawan
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        TUI web (and (S)FTP, Gopher, Gemini, ...) browser with CSS, inline image and JavaScript support
URL:            https://github.com/kachick/chawan
Source0:        %url/archive/%commit/chawan-%commit.tar.gz
License:        Unlicense
BuildRequires: nim
BuildRequires: gcc
BuildRequires: libssh2-devel
BuildRequires: openssl-devel
BuildRequires: brotli-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: make
Packager: apolunar <ijholm@tuta.io>

%description
TUI web (and (S)FTP, Gopher, Gemini, ...) browser with CSS, inline image and JavaScript support.

It uses its own small browser engine developed from scratch,
which can nevertheless display many websites in a manner similar to major graphical browsers.

It can also be used as a terminal pager.

%prep
%autosetup -n chawan-%commit

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
%{_mandir}/man5/cha-localcgi.5.*
%{_mandir}/man5/cha-mailcap.5.*
%{_mandir}/man5/cha-mime.types.5.*
%{_mandir}/man5/cha-urimethodmap.5.*
%{_mandir}/man7/cha-api.7.*
%{_mandir}/man7/cha-css.7.*
%{_mandir}/man7/cha-image.7.*
%{_mandir}/man7/cha-protocols.7.*
%{_mandir}/man7/cha-terminal.7.*
%{_mandir}/man7/cha-troubleshooting.7.*
%license UNLICENSE
%doc README.md

%changelog
* Fri Mar 20 2026 apolunar <ijholm@tuta.io>
- Initial commit
