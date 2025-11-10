Name:           shitpost
Version:        1
Release:        1%?dist
Summary:        A tool to create memes using CLI
License:        WTFPL
URL:            https://redd.it/5ezk1f
Source0:        https://raw.githubusercontent.com/magnus-ISU/aur-scripts/master/shitpost
Requires:       bash
BuildRequires:  wget
BuildArch:      noarch

%description
%{summary}.

%prep
%dnl wget %{SOURCE0}

%install
ls -la
install -Dm 755 %{SOURCE0} %{buildroot}%{_bindir}/shitpost

%files
%{_bindir}/shitpost

%changelog
* Sun Nov 09 2025 Its-J
- Package shitpost
