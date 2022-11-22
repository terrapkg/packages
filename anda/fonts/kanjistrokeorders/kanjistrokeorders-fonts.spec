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


%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}/%{name}/
cp -r *.ttf $RPM_BUILD_ROOT/%{prefix}/%{name}/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,0755)
/%{prefix}/%{name}

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.004
- Initial package
