Name:		bibata-cursor-theme
Version:	2.0.7
Release:	2%?dist
URL:		https://github.com/ful1e5/Bibata_Cursor
Source0:	%{url}/releases/download/v%{version}/Bibata.tar.xz
License:	GPL-3.0-or-later
Summary:	Open source, compact, and material designed cursor set
BuildArch:	noarch
BuildRequires:	rpm_macro(fdupes)

%description
Bibata is an open source, compact, and material designed cursor set that
aims to improve the cursor experience for users. It is one of the most
popular cursor sets in the Linux community and is now available for free
on Windows as well, with multiple color and size options. Its goal is to
offer personalized cursors to users.

%prep
tar xf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/icons/
mv Bibata-* %{buildroot}/%{_datadir}/icons/
%fdupes %buildroot%_datadir/icons/

%files
%doc README.md
%license LICENSE
%{_datadir}/icons/Bibata-*

%changelog
* Wed Jan 4 2023 madonuko <mado@fyralabs.com> - 2.0.3-1
- Initial package
