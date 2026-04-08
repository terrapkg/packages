Name:		google-black-cursor-theme
Version:	2.0.0
Release:	2%{?dist}
URL:		https://github.com/ful1e5/Google_Cursor
Source0:	%{url}/releases/download/v%{version}/GoogleDot-Black.tar.gz
License:	GPL-3.0-or-later
Summary:	An opensource cursor theme inspired by Google.
BuildArch:	noarch
BuildRequires:	rpm_macro(fdupes)

%description
An opensource cursor theme inspired by Google.

%prep
tar xf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/icons/
mv Google* %{buildroot}/%{_datadir}/icons/
%fdupes %buildroot%_datadir/icons/

%files
%doc README.md
%license LICENSE
%{_datadir}/icons/Google*

%changelog
* Tue May 21 2024 matteodev8 <me@matteodev.xyz> - 2.0.0
- Initial package (mostly copied from bibata-cursor-theme)
