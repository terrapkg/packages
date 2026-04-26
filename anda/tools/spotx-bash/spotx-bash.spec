%global commit c9b506c7749f853c827b6d4bd1d57818f953f68d
%global commit_date 20260425
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           spotx-bash
Version:        %commit_date.git~%shortcommit
Release:        1%{?dist}
Summary:        Adblock for the Spotify desktop client on Linux.
License:        MIT
URL:            https://github.com/SpotX-Official/SpotX-Bash
Source0:        %url/archive/%commit.tar.gz
Requires:       bash
BuildArch:      noarch
Provides:       spotx spotx-linux spot-x spotx.sh
Packager:       Its-J <jonah@fyralabs.com>

%description
%summary

%prep
%autosetup -n SpotX-Bash-%commit

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 spotx.sh %{buildroot}%{_bindir}/spotx
%{__ln_s} -f %{_bindir}/spotx %{buildroot}%{_bindir}/spotx.sh

%files
%doc README.md
%license LICENSE
%{_bindir}/spotx.sh
%{_bindir}/spotx

%changelog
* Tue Apr 14 2026 Its-J <jonah@fyralabs.com>
- Add email to my previous contributor attributions

* Sat Dec 14 2024 Its-J <jonah@fyralabs.com>
- Package SpotX-Bash
