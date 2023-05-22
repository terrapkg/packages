Name:		open-hunnin-fonts
Version:	2.0
Release:	1%?dist
URL:		https://github.com/justfont/open-huninn-font
Source0:	%url/releases/download/v%version/jf-openhuninn-%version.ttf
License:	OFL-1.1
Summary:	Chinese (Taiwan) font based on Kosugi Maru
BuildArch:	noarch

%description
Open-hunnin (jf open 粉圓) is an open source Chinese font family
derived from Kosugi Maru for daily use in Taiwan.

%prep

%build

%install
mkdir -p %buildroot/%_datadir/fonts/open-hunnin
install -Dm644 %SOURCE0 %buildroot/%_datadir/fonts/open-hunnin/


%files
%doc README.md
%license LICENSE
%defattr(-,root,root,0755)
/%{_datadir}/fonts/open-hunnin/


%changelog
* Mon May 22 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.1
- Initial package
