%global debug_package %{nil}

Name:           fasm
Release:        1%?dist
Version:        1.73.35
Summary:        Fast assembler for the x86 and x86-64 architectures
License:        BSD-2-Clause
URL:            https://flatassembler.net
Source:         %{url}/%{name}-%{version}.tgz
Packager:       metcya <metcya@gmail.com>
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
* Sun Nov 23 2025 metcya <metcya@gmail.com>
- Package fasm
