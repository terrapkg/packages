Name:               xdg-terminal-exec-nautilus
Version:            0.1.0
Release:            2%?dist
Summary:            xdg-terminal-exec extension for nautilus-python
License:            Apache-2.0
Group:              System
URL:                https://github.com/zirconium-dev/xdg-terminal-exec-nautilus
Source0:            %{url}/archive/refs/tags/%{version}.tar.gz

Requires:           nautilus-python
Packager:           Tulip Blossom (tulilirockz@outlook.com)

%description
xdg-terminal-exec extension for nautilus-python

%prep
%autosetup -n xdg-terminal-exec-nautilus-%{version}

%build

%install
install -Dpm0644 -t %{buildroot}%{_datadir}/nautilus-python/extensions/ ./xdg-terminal-exec-nautilus.py
install -Dpm0644 -t %{buildroot}%{_datadir}/licenses/xdg-terminal-exec-nautilus/ ./LICENSE
install -Dpm0644 -t %{buildroot}%{_datadir}/doc/xdg-terminal-exec-nautilus/ ./README.md

%files
%license LICENSE
%doc README.md
%{_datadir}/nautilus-python/extensions/xdg-terminal-exec-nautilus.py

%changelog
* Thu Mar 12 2026 Tulip Blossom <tulilirockz@outlook.com>
- Initial commit
