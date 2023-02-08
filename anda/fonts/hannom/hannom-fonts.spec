Name:       hannom-fonts
Version:    2005
Release:    2%{?dist}
URL:        https://vietunicode.sourceforge.net/fonts/fonts_hannom.html
Source0:    https://downloads.sourceforge.net/project/vietunicode/hannom/hannom%20v%{version}/hannomH.zip
Source1:    COPYING
License:    custom
Summary:    Chinese and Vietnamese TrueType fonts
BuildRequires: unzip
BuildArch: noarch

%description
%{summary}.

%prep
unzip %{SOURCE0}

%build

%install
install -Dm644 'HAN NOM A.ttf' "%{buildroot}/%{_datadir}/fonts/hannom/HAN NOM A.ttf"
install -Dm644 'HAN NOM B.ttf' "%{buildroot}/%{_datadir}/fonts/hannom/HAN NOM B.ttf"
install -Dm644 %{SOURCE1} "%{buildroot}/%{_datadir}/licenses/%{name}/COPYING"


%files
%license COPYING
%defattr(-,root,root,0755)
/%{_datadir}/fonts/hannom/

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.004
- Initial package
