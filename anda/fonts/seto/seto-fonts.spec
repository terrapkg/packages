Name:			seto-fonts
Version:		6.20
Release:		%autorelease
URL:			https://setofont.osdn.jp/
Source0:	https://osdn.net/frs/redir.php?m=nchc&f=setofont%2F61995%2Fsetofont_v_6_20.zip
License:		OFL-1.1
Summary:		A handwritten font that contains kanji up to JIS 4th level and difficult kanji
BuildRequires:	unzip
BuildArch:		noarch


%description
%{summary}.


%prep
%setup -q -n setofont

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}/%{name}/
cp -r *.ttf $RPM_BUILD_ROOT/%{prefix}/%{name}/


%files
%doc readme.txt
%defattr(-,root,root,0755)
/%{prefix}/%{name}

%changelog
* Tue Nov 22 2022 windowsboy111 <windowsboy111@fyralabs.com> - 6.20
- Initial package
