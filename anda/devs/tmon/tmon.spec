%global commit e8cae0d88dc8d51cb0e34e3fd3553bcbdaf04ca5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20241215
%global debug_package %{nil}

Name:           tmon
Version:        %{commit_date}.git~%{shortcommit}
Release:        1%{?dist}
Summary:        A tiny system monitor for Linux

License:        GPL-3.0-only
URL:            https://github.com/pondda/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

Requires:       lm_sensors
Conflicts:      kernel-tools

Recommends:     google-noto-color-emoji-fonts

BuildRequires:  make gcc-c++ ncurses-devel

Packager:       sadlerm <sad_lerm@hotmail.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit}

%build
%make_build

%install
install -m 0755 -vd              %{buildroot}%{_bindir}
install -m 0755 -vp %{name}      %{buildroot}%{_bindir}/%{name}
install -m 0755 -vd              %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -vp default.conf %{buildroot}%{_sysconfdir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_sysconfdir}/%{name}/default.conf

%changelog
* Tue Dec 17 2024 sadlerm <sad_lerm@hotmail.com>
- Initial package

