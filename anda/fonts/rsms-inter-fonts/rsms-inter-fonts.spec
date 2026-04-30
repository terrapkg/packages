Version:        4.1
Release:        3%{?dist}
URL:            https://rsms.me/inter/

%global common_description %{expand:Inter is a typeface specially designed for user interfaces with focus on high
legibility of small-to-medium sized text on computer screens.

The family features a tall x-height to aid in readability of mixed-case and
lower-case text. Several OpenType features are provided as well, like contextual
alternates that adjusts punctuation depending on the shape of surrounding
glyphs, slashed zero for when you need to disambiguate "0" from "o", tabular
numbers, etc.}

%global foundry rsms
%global fontlicense OFL-1.1
%global fontlicenses LICENSE.txt
%global fontdocsex %{fontlicenses}

%global fontfamily0 Inter
%global fontsummary0 The Inter font family
%global fonts0 extras/ttf/*.ttf
%global fontconfs0 %{SOURCE10}
%global fontdescription0 %{expand:%{common_description}

This package contains the non-variable font version of the Inter font.}

%global fontfamily1 Inter-VF
%global fontsummary1 The Inter font family (variable)
%global fonts1 Inter*.ttf
%global fontconfs1 %{SOURCE11}
%global fontdescription1 %{expand:%{common_description}

This package contains the variable font version of the Inter font.}

Source0:        https://github.com/rsms/inter/releases/download/v%{version}/inter-%{version}.zip
Source10:       63-rsms-inter.conf
Source11:       63-rsms-inter-vf.conf

Packager:       Owen Zimmerman <owen@fyralabs.com>

%fontpkg -a


%prep
%autosetup -c


%build
%fontbuild -a


%install
%fontinstall -a


%check
%fontcheck -a


%fontfiles -a


%changelog
* Thu Apr 30 2026 Owen Zimmerman <owen@fyralabs.com>
- Port to Terra from Fedora

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 25 2025 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.1-1
- Update to 4.1

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 23 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0-1
- Update to 4.0
- Add subpackage for variable fonts

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 04 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.19-5
- Package hinted TrueType fonts instead of Type 1 OTF fonts (RHBZ #2122246)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.19-1
- Update to 3.19

* Thu Apr 01 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.18-1
- Update to 3.18

* Tue Mar 30 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.17-1
- Update to 3.17

* Mon Mar 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.16-1
- Update to 3.16

* Thu Dec 24 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.15-1
- Initial RPM release
