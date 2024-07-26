Name:		google-black-cursor-theme
Version:	2.0.0
Release:	1%{?dist}
URL:		https://github.com/ful1e5/Google_Cursor
Source0:	%{url}/releases/download/v%{version}/GoogleDot-Black.tar.gz
Source1:	https://raw.githubusercontent.com/ful1e5/Google_Cursor/v%{version}/README.md
Source2:	https://raw.githubusercontent.com/ful1e5/Google_Cursor/v%{version}/LICENSE
License:	GPL-3.0
Summary:	An opensource cursor theme inspired by Google. 
BuildArch:	noarch

%description
An opensource cursor theme inspired by Google.

%prep
tar xf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/icons/
mv Google* %{buildroot}/%{_datadir}/icons/
mkdir -p %{buildroot}/%{_datadir}/{doc,licenses}/%{name}/
cp %{SOURCE1} %{buildroot}/%{_datadir}/doc/%{name}/README.md
cp %{SOURCE2} %{buildroot}/%{_datadir}/licenses/%{name}/LICENSE

%files
%doc README.md
%license LICENSE
%{_datadir}/icons/Google*

%changelog
* Tue May 21 2024 matteodev8 <me@matteodev.xyz> - 2.0.0
- Initial package (mostly copied from bibata-cursor-theme)
