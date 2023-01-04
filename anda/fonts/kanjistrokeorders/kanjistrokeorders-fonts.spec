Name:       kanjistrokeorders-fonts
Version:    4.004
Release:    %autorelease
URL:        https://sites.google.com/site/nihilistorguk
License:    custom
Summary:    Kanji stroke order font
BuildRequires: unzip
BuildArch: noarch


%description
%{summary}.


%prep
curl -L --http1.1 http://www.dropbox.com/s/9jv2pnw4ohxzaml/KanjiStrokeOrders_v%{version}.zip > a.zip
unzip a.zip

%build

%install
install -D -m644 KanjiStrokeOrders_v%{version}.ttf %{buildroot}/%{_datadir}/fonts/TTF/KanjiStrokeOrders_v%{version}.ttf


%files
%defattr(-,root,root,0755)
/%{_datadir}/fonts/TTF/KanjiStrokeOrders_v%{version}.ttf

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.004
- Initial package
