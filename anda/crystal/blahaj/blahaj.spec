%define debug_package %nil

Name:			blahaj
Version:		2.0.2
Release:		1%{?dist}
Summary:		Gay sharks at your local terminal - lolcat-like CLI tool
License:		BSD-2-Clause
URL:			https://blahaj.queer.software
Source0:		https://github.com/GeopJr/BLAHAJ/archive/refs/tags/v%version.tar.gz
BuildRequires:	crystal make gcc libyaml-devel pcre-devel
ExclusiveArch:	x86_64

%description
Apart from a cute cuddly shark plushie from IKEA, BLÅHAJ is a lolcat-like CLI
tool that colorizes your input, shows flags and prints colorful sharks!
It has a wide variety of flags/colors to choose from and many options from flag
size to whether to colorize by line, word or character.

%prep
%autosetup -n BLAHAJ-%{version}

%build
%make_build -fpie

%install
%make_install

%check
make test_mt

%files
%doc README.md
%license LICENSE
/usr/bin/blahaj

%changelog
* Sat Apr 15 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.0.1-1
- Initial package.
