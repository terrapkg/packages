Name:           netto
Version:        0.1.0
Release:        1%?dist
Summary:        📡 GUI Network Applet
License:        GPL-3.0-or-later
URL:            https://github.com/madonuko/netto
Source0:        %url/archive/refs/tags/v%version.tar.gz
BuildRequires:  anda-srpm-macros nim
BuildRequires:  pkgconfig(libhelium-1)
BuildRequires:  pkgconfig(libnm)

%description
ネット (codename 🫘 納豆) is the new solution for setting up a new network.
Written proudly in libhelium and Nim, using libnm.

%prep
%autosetup -Sgit

%build
atlas init
atlas rep atlas.lock
%nim_c src/netto

%install
install -Dm755 src/netto -t %buildroot%_bindir

%files
%doc README.md
%license LICENSE.md
%_bindir/netto
