Name:		open-huninn-fonts
Version:	2.1
Release:	1%?dist
URL:		https://github.com/justfont/open-huninn-font
Source0:	%url/archive/refs/tags/v%version.tar.gz
License:	OFL-1.1
Summary:	Chinese (Taiwan) font based on Kosugi Maru
BuildArch:	noarch

%description
Open-huninn (jf open 粉圓) is an open source Chinese font family
derived from Kosugi Maru for daily use in Taiwan.

%prep
%autosetup -n open-huninn-font-%version

%build

%install
mkdir -p %buildroot/%_datadir/fonts/open-huninn
install -Dm644 font/jf-openhuninn-%version.ttf %buildroot/%_datadir/fonts/open-huninn/


%files
%doc README.md
%license license.txt
/%{_datadir}/fonts/open-huninn/


%changelog
* Mon May 22 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.1
- Initial package
