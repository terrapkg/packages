%global commit 2daa195bfb519b33dd292701965bd1f6ea6ad6bb
%global commit_date 20230812
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           git-dude
Version:        %{commit_date}.git~%{shortcommit}
Release:        1%{?dist}
Summary:        Git commit notifier
License:        GPL-3.0-or-later
URL:            https://github.com/ku1ik/git-dude
Source0:        %{url}/archive/%{commit}.tar.gz
BuildArch:      noarch

Requires:       bash
Requires:       git-core
Requires:       libnotify

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit}

%build

%install
install -Dm 755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Wed Sep 30 2026 Its-J <jonah@fyralabs.com>
- Initial commit
