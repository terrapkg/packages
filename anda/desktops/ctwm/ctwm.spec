Summary: Lightweight window manager with virtual workspaces
Name: ctwm
Version: 4.1.0
Release: 1
URL: https://ctwm.org
BuildRequires: libx11-devel libjpg-devel libxt-devel libxext-devel libxmu-devel libxpm-devel cmake
Source0: https://www.ctwm.org/dist/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
License: MIT
Requires: m4
# Derived from RPMSphere's packaging

%description
CTWM is a window manager based on TWM (with virtual workspaces added.)

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
%{__install} -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%files
%doc README.md CHANGES.md
%doc README.md CHANGES.md
%license COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/ctwm
%{_datadir}/doc/ctwm/ctwm.1.html
%{_datadir}/examples/ctwm/system.ctwmrc

%changelog
* Thu June 27 2024 Jaiden Riordan <jade@fyralabs.com> - 4.1.0
- Rewrite for Terra, Thanks RPMSphere
* Tue Dec 24 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.3
- Rebuilt for Fedora
* Sat Apr  9 2011 Agnelo de la Crotche <agnelo@unixversal.com>
- package for openSUSE 11.3/11.4
* Thu Feb 16 2006 Richard Levitte <richard@levitte.org>
- Release ctwm 3.8a.
* Wed May  4 2005 Rudolph T Maceyko <rm55@pobox.com>
- Tweaks.  Added all .ctwmrc files as well as sound and VMS docs.
* Wed May  4 2005 Richard Levitte <richard@levitte.org>
- Changed some directory specifications to RedHat-ish standards.
* Tue May  3 2005 Richard Levitte <richard@levitte.org>
- Received the original from Johan Vromans. Adjusted it to become
  an official .spec file.
  