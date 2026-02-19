Name: nerdfetch
Version: 8.5.2
Release: 1%?dist
Summary: A POSIX *nix fetch script using Nerdfonts 

License: MIT
URL: https://github.com/ThatOneCalculator/NerdFetch
Source0: %url/archive/refs/tags/v%version.tar.gz

BuildArch: noarch
Requires: /usr/bin/sh
Requires: nerdfontssymbolsonly-nerd-fonts

%description
A POSIX *nix (Linux, macOS, Android, BSD, etc) fetch script using Nerdfonts (and others)

%prep
%autosetup -n NerdFetch-%version

%build


%install 
install -Dpm755 nerdfetch %buildroot%_bindir/nerdfetch

%files
%license LICENSE
%doc README.md
%_bindir/nerdfetch

%changelog
* Tue Jul 16 2025 dotdot0 - 8.4.0-1
- Initial Package 
