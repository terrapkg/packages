Name:			mini-wakuwaku-fonts
Version:		1.0
Release:		%autorelease
URL:			http://mini-design.jp/font/mini-wakuwaku.html
Source0:		http://mini-design.jp/font/img/mini-wakuwaku.zip
License:		custom
Summary:		A fat looking, rounded and cute Japanese font
BuildRequires:	unzip
BuildArch:		noarch


%description
%{summary}.


%prep
%setup -q -n mini-wakuwaku

%build

%install
install -D -m644 mini-wakuwaku-maru.otf %{buildroot}/%{_datadir}/fonts/mini-wakuwaku/mini-wakuwaku-maru.otf
install -D -m644 mini-wakuwaku.otf %{buildroot}/%{_datadir}/fonts/mini-wakuwaku/mini-wakuwaku.otf


%files
%doc readme.html
%defattr(-,root,root,0755)
/%{_datadir}/fonts/mini-wakuwaku/

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.004
- Initial package
