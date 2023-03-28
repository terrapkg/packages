%global forgeurl https://gitlab.com/ubports/development/core/ubuntu-touch-meta
%global commit d1dc3b7f6c508cc2e803db3b72fcf1dc0a019afa
%forgemeta

Name:    ubuntu-sdk
Summary: Assets and icons for Unity
Version: 20.04
Release: %autorelease

License:   GPL-3.0-or-later
URL:       https://gitlab.com/ubports/development/core/ubuntu-touch-meta
Source0:   %{url}/-/archive/%commit/ubuntu-touch-meta-%commit.tar.gz
BuildArch: noarch

BuildRequires: binutils
Recommends:    python3-lomiri-click

%description
Theme and icons for Unity.

%prep
%autosetup -n ubuntu-touch-meta-%commit

%build
true

%install
mkdir -m 0755 -p %{buildroot}%{_datadir}/ubports/changelogs %{buildroot}%{_datadir}/click/frameworks

install -Dm644 changelogs/* %{buildroot}%{_datadir}/ubports/changelogs
install -Dm644 frameworks/* %{buildroot}%{_datadir}/click/frameworks

ln -s %{buildroot}%{_datadir}/click/frameworks/ubuntu-sdk-%{version}.framework %{buildroot}%{_datadir}/click/frameworks/current
ln -s %{buildroot}%{_datadir}/ubports/changelogs/%{version} %{buildroot}%{_datadir}/ubports/changelogs/current

%files
%license COPYING
%{_datadir}/ubports/changelogs/
%{_datadir}/click/frameworks/

%changelog
%autochangelog
