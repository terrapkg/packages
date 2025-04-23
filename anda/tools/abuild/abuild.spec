Name:           abuild
Version:        25.03
Release:        1%?dist
Summary:        coreboot autobuild script builds coreboot images for all available targets.
URL:            https://doc.coreboot.org/util/abuild/index.html
License:        GPLv2
BuildRequires:  anda-srpm-macros
BuildArch:      noarch
Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%summary 

%prep
%git_clone https://review.coreboot.org/coreboot.git %version

%install
install -Dm 777 util/abuild/abuild %buildroot%_bindir/abuild

%files
/usr/bin/abuild

%changelog
* Sat Feb 01 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial Package
