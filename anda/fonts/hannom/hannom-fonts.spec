Name:       hannom-fonts
Version:    2005
Release:    %autorelease
URL:        http://vietunicode.sourceforge.net/fonts/fonts_hannom.html
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
mkdir -p $RPM_BUILD_ROOT/%{prefix}/%{name}/
cp -r *.ttf $RPM_BUILD_ROOT/%{prefix}/%{name}/


%clean
rm -rf $RPM_BUILD_ROOT


%files
# %license %{SOURCE1}
%defattr(-,root,root,0755)
/%{prefix}/%{name}

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.004
- Initial package
