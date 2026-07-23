%global commit 1d20bd9b058f425a0e3e8ac03fe2f501b0457d7c
%global commit_date 20260704
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           yabs
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Simple bash script to estimate Linux server performance using fio, iperf3, & Geekbench
URL:            https://github.com/masonr/yet-another-bench-script
Source0:        %{url}/archive/%{commit}/yet-another-bench-script-%commit.tar.gz
License:        WTFPL
Provides:       yet-another-bench-script
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n yet-another-bench-script-%{commit}

%build

%install
install -Dm755 yabs.sh %{buildroot}%{_bindir}/yabs

%files
%doc README.md
%license LICENSE
%{_bindir}/yabs

%changelog
* Fri Apr 03 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
