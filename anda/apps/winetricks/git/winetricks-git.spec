# Fedora sometimes sources the snapshots under stable versions and just bumps release
# For user clarity I have separated these into different packages
%global commit  5eed63521781ffc2f0c4bbee7ec9e215b13a1243
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 20250102
%global commit_date 20250711

Name:           winetricks-git
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Work around common problems in Wine; Winetricks Git builds
License:        LGPL-2.1-or-later
URL:            https://github.com/Winetricks/winetricks
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
Requires:       cabextract
Requires:       gzip
Requires:       unzip
Requires:       wget
Requires:       which
Requires:       hicolor-icon-theme
Requires:       (kdialog or zenity)
Requires:       (wine-stable or wine-staging or wine-dev or wine-common)
Conflicts:      winetricks
Conflicts:      terra-winetricks
BuildArch:      noarch
# need arch-specific wine, not available everywhere:
# - adopted from wine.spec
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
ExcludeArch:    ppc64 ppc64le

%description
Winetricks is an easy way to work around common problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also lets you install missing DLLs
or tweak various Wine settings individually.

This version of Winetricks is built from the latest Git.

It is also compatible with Terra WINE builds.

%prep
%setup -qn winetricks-%{commit}

sed -i -e s:steam:: -e s:flash:: tests/*

%build
# Empty build section because RPM

%install
%make_install
# some tarballs do not install appdata
install -Dm0644 -t %{buildroot}%{_datadir}/metainfo src/io.github.winetricks.Winetricks.metainfo.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/winetricks.desktop


%files
%license COPYING
%license debian/copyright
%doc README.md
%{_bindir}/winetricks
%{_mandir}/man1/winetricks.1*
%{_datadir}/applications/winetricks.desktop
%{_datadir}/bash-completion/completions/winetricks
%{_datadir}/icons/hicolor/scalable/apps/winetricks.svg
%{_datadir}/metainfo/io.github.winetricks.Winetricks.metainfo.xml


%changelog
%autochangelog
