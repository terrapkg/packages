%global         debug_package %{nil}

Name:		minecraft-launcher
Version:	1121
Release:	2%{?dist}
Summary:	Official launcher for Minecraft

License:	Proprietary
URL:		https://minecraft.net
Source0:	https://launcher.mojang.com/download/linux/x86_64/minecraft-launcher_%{version}.tar.gz
Source1:	minecraft-launcher.desktop
Source2:	https://launcher.mojang.com/download/minecraft-launcher.svg

ExclusiveArch:	x86_64

Requires:	java >= 1.8.0

%description
The official Linux release of the launcher for Minecraft, a game about placing blocks and going on adventures.

%prep
%autosetup -n minecraft-launcher

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/symbolic/apps/
mkdir -p %{buildroot}/%{_datadir}/applications/

mv %{_builddir}/minecraft-launcher/minecraft-launcher %{buildroot}/%{_bindir}/minecraft-launcher
chmod 755 %{buildroot}/%{_bindir}/minecraft-launcher

install -Dm644 %{_sourcedir}/minecraft-launcher.desktop %{buildroot}/%{_datadir}/applications/minecraft-launcher.desktop
install -Dm644 %{_sourcedir}/minecraft-launcher.svg %{buildroot}/%{_datadir}/icons/hicolor/symbolic/apps/minecraft-launcher.svg

%files
%{_bindir}/minecraft-launcher
%{_datadir}/applications/minecraft-launcher.desktop
%{_datadir}/icons/hicolor/symbolic/apps/minecraft-launcher.svg

%changelog
* Tue Mar 08 2022 Thomas Batten stenstorpmc@gmail.com> - 1121-2
- Moved minecraft-launcher into bindir

* Mon Mar 07 2022 Thomas Batten <stenstorpmc@gmail.com> - 1121-1
- Updated to version 1121

* Sat Nov 27 2021 Thomas Batten <stenstorpmc@gmail.com> - 928-1
- Updated to version 928

* Tue Mar 02 2021 Thomas Batten <stenstorpmc@gmail.com> - 887-1
- Updated to version 887
- Adjust install procedure for new packaging method

* Tue Feb 23 2021 Thomas Batten <stenstorpmc@gmail.com> - 2.2.1867-1
- Updated to version 2.2.1867

* Wed Feb 03 2021 Thomas Batten <stenstorpmc@gmail.com> - 2.2.1441-1
- Updated to version 2.2.1441

* Tue Jan 26 2021 Thomas Batten <stenstorpmc@gmail.com> - 2.2.1262-1
- Updated to version 2.2.1262

* Thu Dec 10 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.2.909-1
- Updated to version 2.2.909

* Tue Dec 01 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.2.741-1
- Updated to version 2.2.741

* Wed Oct 21 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.17785-1
- Updated to version 2.1.17785

* Wed Sep 23 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.17627-1
- Updated to version 2.1.17627

* Wed Sep 02 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.17417-1
- Updated to version 2.1.17417

* Wed Jul 22 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.16102-1
- Updated to version 2.1.16102

* Sat Jul 04 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.15852-1
- Updated to version 2.1.15852

* Mon Jun 08 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.15166-1
- Updated to version 2.1.15166

* Thu May 28 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.14947-1
- Updated to version 2.1.14947

* Tue May 26 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.14930-1
- Updated to version 2.1.14930

* Thu May 21 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.14403-1
- Updated to version 2.1.14403

* Sat Apr 18 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.13829-1
- Updated to version 2.1.13829

* Thu Apr 02 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.13509-1
- Updated to version 2.1.13509

* Fri Mar 20 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.13086-1
- Updated to version 2.1.13086

* Tue Mar 17 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.12872-1
- Updated to version 2.1.12872

* Tue Mar 03 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.12464-1
- Updated to version 2.1.12464

* Mon Feb 24 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.12308-1
- Updated to version 2.1.12308

* Sat Jan 25 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.11314-1
- Updated to version 2.1.11314
- use install instead of cp for desktop and icon files

* Fri Jan 24 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.11290-1
- Updated to version 2.1.11290

* Fri Jan 17 2020 Thomas Batten <stenstorpmc@gmail.com> - 2.1.10835-1
- Updated to version 2.1.10835

* Thu Nov 14 2019 Thomas Batten <stenstorpmc@gmail.com> - 2.1.9618-1
- Updated to version 2.1.9618
- Use official minecraft-launcher.svg

* Wed Jun 26 2019 Thomas Batten <stenstorpmc@gmail.com> - 2.1.5320-1
- Updated to version 2.1.5320

* Thu Apr 25 2019 Thomas Batten <stenstorpmc@gmail.com> - 2.1.3676-1
- Updated to version 2.1.3676

* Tue Feb 26 2019 Thomas Batten <stenstorpmc@gmail.com> - 2.1.2482-1
- Updated to version 2.1.2482
- Re-jig install section

* Mon Feb 25 2019 Thomas Batten <stenstorpmc@gmail.com> - 2.1.2472-1
- Updated to version 2.1.2472

* Sun Nov 25 2018 Thomas Batten <stenstorpmc@gmail.com> - 2.1.1431-1
- Initial build using version 2.1.1431