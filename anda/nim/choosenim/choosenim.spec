Name:			choosenim
Version:		0.8.4
Release:		%autorelease
Summary:		Tool for easily installing and managing multiple versions of the Nim programming language
License:		BSD-3-Clause
URL:			https://github.com/dom96/choosenim
Source0:		%{url}/releases/download/v%{version}/choosenim-%{version}_linux_amd64
Source1:		https://raw.githubusercontent.com/dom96/choosenim/v%{version}/LICENSE
Source2:		https://raw.githubusercontent.com/dom96/choosenim/v%{version}/readme.md
ExclusiveArch:	x86_64
Conflicts:		nim

%description
choosenim installs the Nim programming language from official downloads and
sources, enabling you to easily switch between stable and development compilers.

%prep

%build

%install
mkdir -p %{buildroot}/%{_datadir}/licenses/%{name}/
mkdir -p %{buildroot}/%{_datadir}/doc/%{name}/
install -Dm 755 %{SOURCE0} -t "%{buildroot}/%{_bindir}/choosenim"
install -Dm 644 %{SOURCE1} -t "%{buildroot}/%{_datadir}/licenses/%{name}/LICENSE"
install -Dm 644 %{SOURCE2} -t "%{buildroot}/%{_datadir}/doc/%{name}/readme.md"

%files
%doc readme.md
%license LICENSE
%{_bindir}/choosenim

%changelog
* Mon Jan 9 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.8.4
- Initial Package.
