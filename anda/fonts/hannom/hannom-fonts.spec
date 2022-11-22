Name:       hannom-fonts
Version:    2005
Release:    %autorelease
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


%install
install -D -m644 'HAN NOM A.ttf' "%{buildroot}/%{_datadir}/fonts/hannom/HAN NOM A.ttf"
install -D -m644 'HAN NOM B.ttf' "%{buildroot}/%{_datadir}/fonts/hannom/HAN NOM B.ttf"


%files
# %license %{SOURCE1}
%defattr(-,root,root,0755)
/%{_datadir}/fonts/hannom/

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.004
- Initial package
