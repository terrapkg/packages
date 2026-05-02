%global commit c9a5b3943e7fdab96e1cbbdbca1a7ebca371fc3c
%global commit_date 20251027
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:			system76-wallpapers
Version:		0~%{commit_date}git.%{shortcommit}
Release:		1%{?dist}
Summary:		System76 Wallpapers
License:		CC-BY-SA-4.0
URL:			https://github.com/pop-os/system76-wallpapers
Source0:		%{url}/archive/%{commit}/system76-wallpapers-%{commit}.tar.gz
BuildArch:      noarch

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package gnome-background-properties
Summary: GNOME background properties for System76 wallpapers
Requires: %{name} = %{evr}
BuildArch: noarch

%description gnome-background-properties
%{summary}.

%prep
%autosetup -n %{name}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/backgrounds
cp -r backgrounds/* %{buildroot}%{_datadir}/backgrounds/
mkdir -p %{buildroot}%{_datadir}/gnome-background-properties
install -Dm644 system76-wallpapers.xml %{buildroot}%{_datadir}/gnome-background-properties/system76-wallpapers.xml

%files
%license LICENSE
%{_datadir}/backgrounds/System76-*

%files gnome-background-properties
%{_datadir}/gnome-background-properties/system76-wallpapers.xml

%changelog
* Sat May 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
