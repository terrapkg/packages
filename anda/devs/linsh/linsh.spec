Name:          linsh
Version:       0.02
Release:       1%{?dist}
Summary:       Linux shell
License:       GPL-2.0-or-later
URL:           https://github.com/maxskiier/linsh
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:      Owen Zimmerman <owen@fyralabs.com>

BuildRequires: make
BuildRequires: gcc

%description
%{summary}.

%prep
%autosetup

%build
%make_build CC="%__cc %build_cflags %build_ldflags"

%install
install -Dm755 linsh %{buildroot}%{_bindir}/linsh

%files
%license LICENSE
%doc README.txt
%{_bindir}/linsh

%changelog
* Mon Jun 15 2026 Owen Zimmerman <owen@fyralabs.com> - 0.02-1
- Initial package
