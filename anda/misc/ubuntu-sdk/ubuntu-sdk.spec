%global forgeurl https://gitlab.com/ubports/development/core/ubuntu-touch-meta
%global commit 0d9120ed8ac9ec156a1d9dd00a6651613b6e6941
%forgemeta

Name:    ubuntu-sdk
Summary: Ubuntu Touch Metapackages for Click
Version: 20.04
Release: 2%?dist

License:   GPL-3.0-or-later
URL:       https://gitlab.com/ubports/development/core/ubuntu-touch-meta
Source0:   %{url}/-/archive/%commit/ubuntu-touch-meta-%commit.tar.gz
BuildArch: noarch

BuildRequires: binutils

Recommends:    python3-lomiri-click

%description
Ubuntu Touch Metapackages for Click.

%prep
%autosetup -n ubuntu-touch-meta-%commit

%build
true

%install
mkdir -m 0755 -p %{buildroot}%{_datadir}/ubports/changelogs %{buildroot}%{_datadir}/click/frameworks

install -Dm644 changelogs/* %{buildroot}%{_datadir}/ubports/changelogs
install -Dm644 frameworks/* %{buildroot}%{_datadir}/click/frameworks

ln -s %{_datadir}/click/frameworks/ubuntu-sdk-%{version}.framework %{buildroot}%{_datadir}/click/frameworks/current
ln -s %{_datadir}/ubports/changelogs/%{version} %{buildroot}%{_datadir}/ubports/changelogs/current

%files
%license COPYING
%{_datadir}/ubports/changelogs/
%{_datadir}/click/frameworks/

%changelog
%autochangelog
