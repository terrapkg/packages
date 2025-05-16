# Fedora sometimes sources the snapshots under stable versions and just bumps release
# For user clarity I have separated these into different packages

Name:           winetricks
Version:        20250102
Release:        1%{?dist}

Summary:        Work around common problems in Wine

License:        LGPL-2.1-or-later
URL:            https://github.com/Winetricks/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

# need arch-specific wine, not available everywhere:
# - adopted from wine.spec
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
ExcludeArch:    ppc64 ppc64le

BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  gcc

Requires:       (wine-stable or wine-staging or wine-devel)
Requires:       cabextract gzip unzip wget which
Requires:       hicolor-icon-theme
Requires:       (kdialog or zenity)

%description
Winetricks is an easy way to work around common problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also lets you install missing DLLs
or tweak various Wine settings individually.


%prep
%setup -q

sed -i -e s:steam:: -e s:flash:: tests/*

%build
# not needed

%install
%make_install
# some tarballs do not install appdata
install -m0644 -D -t %{buildroot}%{_datadir}/metainfo src/io.github.winetricks.Winetricks.metainfo.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license COPYING debian/copyright
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/io.github.winetricks.Winetricks.metainfo.xml


%changelog
%autochangelog
