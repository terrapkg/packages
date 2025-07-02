%define _debugsource_template %{nil}

%define commit cd7d8fac1be33c2bdf06494f174b2ecb0e2f4f8e
%global shortcommit %{sub %{commit} 1 12}
%global commit_date 250419

Name:           bmpblk_utility
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        A utility to create/modify the bmpfv in the GBB of chromebooks running old stock firmware

License:        BSD-3-Clause
URL:            https://git.tree123.org/WeirdTreeThing/bmpblk_utility
Source0:        https://git.tree123.org/WeirdTreeThing/bmpblk_utility/archive/main.tar.gz
Source1:        https://chromium.googlesource.com/chromium/src/+/HEAD/LICENSE

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-g++
BuildRequires:  xz-libs
BuildRequires:  xz-devel
BuildRequires:  libyaml
BuildRequires:  libyaml-devel

packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n bmpblk_utility

%build
./build.sh

%install
install -Dm 644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE

install -Dm 755 build/bmpblk_utility %{buildroot}%{_bindir}/bmpblk_utility
install -Dm 755 build/bmpblk_font %{buildroot}%{_bindir}/bmpblk_font

%files
%license %{_licensedir}/%{name}/LICENSE
%doc README.md
%{_bindir}/bmpblk_utility
%{_bindir}/bmpblk_font

%changelog
* Tue Jul 01 2025 Owen Zimmerman <owen@fyralabs.com>
- initial package
