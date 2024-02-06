Name:			terra-wl-clipboard
Version:		2.2.1
Release:		1%?dist
Summary:		Command-line copy/paste utilities for Wayland
License:		GPL-3.0
URL:			https://github.com/bugaevc/wl-clipboard
Source0:		%url/archive/refs/tags/v%version.tar.gz
Requires:		xdg-utils mailcap
#? Requires: wayland
BuildRequires:	git-core meson wayland-protocols-devel gcc pkgconfig(wayland-client) redhat-rpm-config
Provides:		wl-clipboard = %version

%description
This project implements two command-line Wayland clipboard utilities, wl-copy and wl-paste,
that let you easily copy data between the clipboard and Unix pipes, sockets, files and so on.

%prep
%autosetup -n wl-clipboard-%version

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/wl-{copy,paste)
%bash_completions_dir/wl-{copy,paste}
%fish_completions_dir/wl-{copy,paste}
%zsh_completions_dir/_wl-{copy,paste}
%_mandir/man1/wl-{clipboard,copy,paste}.1.gz

%changelog
%autochangelog
