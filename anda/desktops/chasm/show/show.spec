%global debug_package %{nil}

Name:           show
Release:        1%{?dist}
Version:        0.1.0
Summary:        Pure assembly file viewer with syntax highlighting
License:        Unlicense
URL:            https://github.com/isene/show
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  nasm
BuildRequires:  make
Packager:       Owen Zimmerman <owen@fyralabs.com>
ExclusiveArch:  x86_64
Conflicts:      nmh

%description
Pure assembly file viewer with syntax highlighting. Part of CHasm.

%prep
%autosetup -C

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.0-1
- Initial commit
