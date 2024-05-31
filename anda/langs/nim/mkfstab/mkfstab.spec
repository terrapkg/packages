Name:           mkfstab
Version:        0.1.1
Release:        1%?dist
Summary:        An alternative to genfstab: generate output suitable for addition to /etc/fstab
License:        MIT
URL:            https://github.com/Ultramarine-Linux/mkfstab
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildRequires:  nim anda-srpm-macros

%description
An alternative to genfstab from Arch Linux. This is a dead simple but faster implementation of genfstab.

%prep
%autosetup

%build
nimble setup -y
nim c %nim_c src/%name

%install
install -Dpm755 src/%name %buildroot%_bindir/%name

%files
%doc README.md
%license LICENSE
%_bindir/%name
