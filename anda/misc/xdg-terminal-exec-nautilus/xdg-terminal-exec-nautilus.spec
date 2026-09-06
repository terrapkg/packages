Name:               xdg-terminal-exec-nautilus
Version:            0.1.0
Release:            1%?dist
Summary:            xdg-terminal-exec extension for nautilus-python
License:            Apache-2.0
Group:              System
URL:                https://github.com/zirconium-dev/xdg-terminal-exec-nautilus
Source0:            %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:          noarch
Requires:           nautilus-python
Packager:           Tulip Blossom (tulilirockz@outlook.com)

%description
%{summary}.

%prep
%autosetup -n xdg-terminal-exec-nautilus-%{version}

%build

%install
install -Dpm0644 -t %{buildroot}%{_datadir}/nautilus-python/extensions/ ./xdg-terminal-exec-nautilus.py

%files
%license LICENSE
%doc README.md
%{_datadir}/nautilus-python/extensions/xdg-terminal-exec-nautilus.py

%changelog
* Fri Mar 13 2026 Tulip Blossom <tulilirockz@outlook.com>
- Initial commit
