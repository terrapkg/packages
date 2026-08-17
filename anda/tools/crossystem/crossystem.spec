%global commit_date 20221215
%global commit 	c4102fe4eef8c0539c03d60c7256fd4bc599bf4a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           crossystem
Summary:        Manage ChromeOS firmware
License:        BSD-3-Clause
URL:            https://chromium.googlesource.com/chromiumos/platform/vboot_reference

Version:        %shortcommit
Release:        1%?dist
Source0:        %url/+archive/refs/heads/release-R110-15278.B.tar.gz
Patch0:         use-flashrom-cros.patch
Patch1:         disable-werror.patch

Requires:       flashrom-cros
BuildRequires:  make gcc openssl-devel flashrom-devel libuuid-devel

Packager:       WeirdTreeThing <bradyn127@protonmail.com>

%description
A tool to manage ChromeOS bootloader flags and get various
info from a ChromeOS system

%prep
%setup -C
%patch -P0 -p1
%patch -P1 -p1

%build
%make_build

%install
install -Dm755 build/utility/crossystem %{buildroot}%{_bindir}/crossystem

%files
%license LICENSE
%{_bindir}/crossystem

%changelog
* Fri Oct 25 2024 WeirdTreeThing <bradyn127@protonmail.com>
- initial release
