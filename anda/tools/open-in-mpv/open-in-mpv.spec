#%global debug_package %{nil}

Name:           open-in-mpv
Version:        2.2.2
Release:        1%?dist
Summary:        CLI component of open-in-mpv browser extension

License:        MIT
URL:            https://github.com/Baldomo/open-in-mpv
Source0:        https://github.com/Baldomo/open-in-mpv/archive/refs/tags/v%{version}.tar.gz

ExclusiveArch:  %{golang_arches}

BuildRequires:  go-rpm-macros
BuildRequires:  git
BuildRequires:  elfutils

%description
This is a simple web extension (for Chrome and Firefox) which helps open any video in the currently open tab in the mpv player.

The extension itself shares a lot of code with the one from the awesome iina, while the (bare) native binary is written in Go (this is a rewrite from C++).

%prep
%autosetup -p1

%build
make build/linux/open-in-mpv

%install
install -Dm755 build/linux/open-in-mpv %{buildroot}%{_bindir}/open-in-mpv
install -Dm644 scripts/open-in-mpv.desktop %{buildroot}%{_datarootdir}/applications/open-in-mpv.desktop

%post
update-desktop-database %{_datarootdir}/applications
xdg-mime default open-in-mpv.desktop x-scheme-handler/mpv

%files
%license LICENSE
%doc README.md
%{_bindir}/open-in-mpv
%{_datarootdir}/applications/open-in-mpv.desktop

%changelog
%autochangelog
