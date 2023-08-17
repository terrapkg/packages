Name:			seto-fonts
Version:		6.20
Release:		2%?dist
URL:			https://setofont.osdn.jp/
Source0:		http://osdn.net/frs/redir.php?m=nchc&f=setofont%2F61995%2Fsetofont_v_6_20.zip
License:		OFL-1.1
Summary:		A handwritten font that contains kanji up to JIS 4th level and difficult kanji
BuildRequires:	unzip
BuildArch:		noarch


%description
%summary.


%prep
%setup -q -n setofont

%build

%install
mkdir -p %buildroot/%_datadir/fonts/%name
install -Dm644 *.ttf %buildroot/%_datadir/fonts/%name/


%files
%doc readme.txt
%_datadir/fonts/%name/

%changelog
* Sun Jun 18 2023 windowsboy111 <windowsboy111@fyralabs.com> - 6.20-2
- Fix install dir.

* Tue Nov 22 2022 windowsboy111 <windowsboy111@fyralabs.com> - 6.20-1
- Initial package
