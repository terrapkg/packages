%global commit 6b8a3e4faaabc462f90ffcb0cf0f91991ee58077
%global commit_date 20240428
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       vala-extra-vapis
Version:    0~%{commit_date}git.%{shortcommit}
Release:    1%?dist
License:    LGPL-2.1-or-later
Summary:    Vala bindings to various libraries which do not provide their own bindings, and for which valac does not provide bindings
URL:        https://gitlab.gnome.org/GNOME/vala-extra-vapis
Source0:    %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:    https://gitlab.gnome.org/GNOME/vala/-/raw/main/COPYING
BuildArch:  noarch
Packager:   Owen Zimmerman <owen@fyralabs.com

%description
%{summary}.

%prep
%autosetup -C

%build

%install
mkdir -p %{buildroot}%{_datadir}/vala/vapi/
cp -a *.vapi %{buildroot}%{_datadir}/vala/vapi/
cp -a *.deps %{buildroot}%{_datadir}/vala/vapi/
mv %{S:1} LICENSE

%files
%doc README.md
%license LICENSE
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/vala/vapi/*.deps

%changelog
* Mon Oct 12 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
