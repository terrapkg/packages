%define debug_package %{nil}

Name:          linsh
Version:       0.02
Release:       1%{?dist}
Summary:       Linux shell
License:       GPL-2.0-or-later
URL:           https://github.com/maxskiier/linsh
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:      Owen Zimmerman <owen@fyralabs.com>

BuildRequires: make
BuildRequires: gcc

%description
%{summary}.

%prep
%autosetup

%build
%make_build

%install
install -Dm755 linsh %{buildroot}%{_bindir}/linsh

%files
%license LICENSE
%doc README.txt
%{_bindir}/linsh
