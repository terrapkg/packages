Name:           hollywood
Version:        1.25
Release:        1%?dist
Summary:        Fill your console with Hollywood melodrama technobabble
URL:            https://github.com/dustinkirkland/hollywood
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
License:        Apache-2.0
Recommends:     apg
Recommends:     bmon
Recommends:     byobu
Recommends:     util-linux
Recommends:     ccze
Recommends:     cmatrix
Recommends:     coreutils
Recommends:     htop
Recommends:     jp2a
Recommends:     mlocate
Requires:       moreutils
Recommends:     mplayer
Recommends:     openssh-client
Recommends:     speedometer
Recommends:     tree
Requires:       man
Requires:       python3-pygments
Requires:       tmux
Recommends:     byobu
Recommends:     caca-utils
Recommends:     newsbeuter
Requires:       perl-base
Recommends:     rsstail
Recommends:     ticker
Requires:       wget
Recommends:     w3m
Recommends:     jp2a
BuildArch: noarch
Packager: apolunar <ijholm@tuta.io>

%description
Fill your console with Hollywood melodrama technobabble.

This utility splits your terminal into multiple panes of genuine technobabble,
perfectly suitable for any Hollywood geek melodrama.
It is particularly suitable on any number of computer consoles in the
background of any excellent schlock technothriller.

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{_libdir}/hollywood
mkdir -p %{buildroot}%{_datadir}/wallstreet
mkdir -p %{buildroot}%{_datadir}/hollywood
mkdir -p %{buildroot}%{_mandir}/man1
install -Dm 755 bin/hollywood %{buildroot}%{_bindir}/hollywood
install -Dm 755 bin/wallstreet %{buildroot}%{_bindir}/wallstreet
install -Dm 755 lib/hollywood/* %{buildroot}%{_libdir}/hollywood/
install -Dm 644 share/man/man1/* %{buildroot}%{_mandir}/man1/
install -Dm 644 share/wallstreet/* %{buildroot}%{_datadir}/wallstreet/
install -Dm 644 share/hollywood/* %{buildroot}%{_datadir}/hollywood/

%files
%{_bindir}/hollywood
%{_bindir}/wallstreet
%{_libdir}/hollywood/
%{_mandir}/man1/hollywood.1.*
%{_mandir}/man1/wallstreet.1.*
%{_datadir}/wallstreet/
%{_datadir}/hollywood/
%license debian/copyright
%doc README.md

%changelog
* Fri Mar 20 2026 apolunar <ijholm@tuta.io>
- Initial commit
