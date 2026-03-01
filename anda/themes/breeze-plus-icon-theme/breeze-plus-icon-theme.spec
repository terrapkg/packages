Name:           breeze-plus-icon-theme
Version:        6.19.0
Release:        1%{?dist}
Summary:        Breeze icon theme with additional icons
Packager:       Amy King <amy@amyrom.tech>

License:        LGPL-2.1-only
URL:            https://github.com/mjkim0727/breeze-plus
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
%description
%summary.

%prep
%autosetup -n breeze-plus-%{version}
%build

%install
mkdir -p %{buildroot}%{_datadir}/icons/
cp -r src/* %{buildroot}%{_datadir}/icons/


%files
%license LICENSE
%doc README.md
%{_datadir}/icons/*

%changelog
* Wed Feb 25 2026 Amy King <amy@amyrom.tech> - 6.19.0
- Initial package
