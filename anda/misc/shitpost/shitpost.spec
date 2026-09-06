Name:           shitpost
Version:        1
Release:        2%?dist
Summary:        A tool to create memes using CLI
License:        WTFPL
URL:            https://redd.it/5ezk1f
Source0:        https://raw.githubusercontent.com/magnus-ISU/aur-scripts/master/shitpost
Requires:       bash
BuildArch:      noarch

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep

%build

%install
install -Dm 755 %{SOURCE0} %{buildroot}%{_bindir}/shitpost

%files
%{_bindir}/shitpost

%changelog
* Tue Apr 14 2026 Its-J <jonah@fyralabs.com>
- Add email to my previous contributor attributions

* Sun Nov 09 2025 Its-J <jonah@fyralabs.com>
- Package shitpost
