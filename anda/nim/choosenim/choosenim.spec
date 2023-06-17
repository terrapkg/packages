Name:			choosenim
Version:		0.8.4
Release:		3%{?dist}
Summary:		Easily install and manage multiple versions of the Nim programming language
License:		BSD-3-Clause
URL:			https://github.com/dom96/choosenim
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildRequires:	nim mold

%description
choosenim installs the Nim programming language from official downloads and
sources, enabling you to easily switch between stable and development compilers.

%prep
%autosetup -n choosenim-%version

%build

%install
mold -run nimble build -t:-fPIE -l:-pie


%files
%doc readme.md
%license LICENSE
%{_bindir}/choosenim

%changelog
* Sat Jun 17 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.8.4-3
- Use nim to compile instead of prebuilt binaries.

* Mon Jan 9 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.8.4-1
- Initial Package.
