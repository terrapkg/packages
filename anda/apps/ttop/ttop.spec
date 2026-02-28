Name:           ttop
Version:        1.5.7
Release:        1%?dist
Summary:        System monitoring tool with historical data service, triggers and top-like TUI
License:        MIT
URL:            https://github.com/inv2004/ttop
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  nim

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n ttop-%version
%nim_prep

%build
%nim_c src/ttop

%install
install -Dm755 src/ttop.out %{buildroot}%{_bindir}/ttop

%files
%doc README.md
%license LICENSE
%{_bindir}/ttop

%changelog
* Sun Jan 04 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
