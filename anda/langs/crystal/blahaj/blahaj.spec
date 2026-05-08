Name:           blahaj
Version:        2.2.0
Release:        2%{?dist}
Summary:        Gay sharks at your local terminal - lolcat-like CLI tool
License:        BSD-2-Clause
URL:            https://blahaj.geopjr.dev/
Source0:        https://codeberg.org/GeopJr/BLAHAJ/archive/v%{version}.tar.gz
BuildRequires:  crystal shards make gcc libyaml-devel pcre-devel libgc-devel libevent-devel bash
ExclusiveArch:  x86_64

%description
Apart from a cute cuddly shark plushie from IKEA, BLÅHAJ is a lolcat-like CLI
tool that colorizes your input, shows flags and prints colorful sharks!
It has a wide variety of flags/colors to choose from and many options from flag
size to whether to colorize by line, word or character.

%prep
%autosetup -n %{name}

%build
shards build --production --release

%install
%make_install

%files
%doc README.md
%license LICENSE
%_bindir/blahaj

%changelog
* Sat Dec 06 2025 june-fish <june@fyralabs.com> - 2.2.0-2
- Update URLs and build steps (fix missing debug_package)
* Sat Apr 15 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.0.1-1
- Initial package.
