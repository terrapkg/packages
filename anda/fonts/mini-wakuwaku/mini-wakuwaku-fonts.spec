Name:       mini-wakuwaku-fonts
Version:    1.0
Release:    %autorelease
URL:        http://mini-design.jp/font/mini-wakuwaku.html
Source0:	http://mini-design.jp/font/img/mini-wakuwaku.zip
License:    custom
Summary:    A fat looking, rounded and cute Japanese font
BuildRequires: unzip
BuildArch: noarch


%description
%{summary}.


%prep
%setup -n mini-wakuwaku


%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}/%{name}/
cp -r *.otf $RPM_BUILD_ROOT/%{prefix}/%{name}/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc readme.html
%defattr(-,root,root,0755)
/%{prefix}/%{name}

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.004
- Initial package
