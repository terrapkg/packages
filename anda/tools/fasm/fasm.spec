%global debug_package %{nil}

Name:           fasm
Release:        2%?dist
Version:        1.73.35
Summary:        Fast assembler for the x86 and x86-64 architectures
License:        BSD-2-Clause
URL:            https://flatassembler.net
Source:         %{url}/%{name}-%{version}.tgz
Packager:       Olivia <git@olivia.sh>
ExclusiveArch:  x86_64 i686

%description
%summary.

%prep
%autosetup -n %{name}

%build
%ifarch i686
./fasm source/Linux/fasm.asm %{name}.out
%elifarch x86_64
./fasm.x64 source/Linux/x64/fasm.asm %{name}.out
%endif

%install
install -Dm 755 %{name}.out %{buildroot}%{_bindir}/%{name}

%files
%doc fasm.txt whatsnew.txt
%license license.txt
%{_bindir}/%{name}

%changelog
* Sun Jul 19 2026 Olivia <git@olivia.sh> - 1.73.35-2
- Update packager

* Sun Nov 23 2025 Olivia <git@olivia.sh>
- Package fasm
