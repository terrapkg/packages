# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/alexeiva/Raleway
%global commit      98add575720aa077b7d253477e26c463a55e71da
%forgemeta

Version: 4.101
Release: 10%{?dist}
URL:     %{forgeurl}

%global foundry           Impallari
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Raleway
%global fontsummary       Raleway, an elegant sans-serif font family
%global fonts             fonts/TTF/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Raleway is an elegant sans-serif font family intended for headings and other
large size usage.

It features both old style and lining numerals, standard and discretionary
ligatures, a pretty complete set of diacritics, as well as a stylistic
alternate inspired by more geometric sans-serif typefaces than its
neo-grotesque inspired default character set.}

Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{fontpkgname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{fontpkgname}.

%prep
%forgesetup
%linuxtext %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles
%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc documents/*

%changelog
* Thu Nov 17 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.101
- Bump

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.025
- Repackaged for Terra

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.025-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 02 2022 Parag Nemade <pnemade@fedoraproject.org> - 4.025-9.20200310git98add57
- Fix packaging issues

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.025-8.20200310git98add57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.025-7.20200310git98add57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.025-6.20200310git98add57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.025-5.20200310git98add57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.025-4.20200310git98add57
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.025-3.20200310git98add57
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.025-2.20200310git98add57
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Tue Mar 10 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 4.025-1.20200310git98add57.fc33
✅ Convert to fonts-rpm-macros use

* Sun Mar 12 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0-1.git20161116.6c67ab1
- Initial package.
