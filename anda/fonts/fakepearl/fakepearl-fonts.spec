Name:		fakepearl-fonts
Version:	1.1
Release:	1%?dist
URL:		https://github.com/max32002/FakePearl
Source0:	%url/archive/refs/tags/%version.tar.gz
License:	OFL-1.1
Summary:	A free font family derived from open-huninn-font
BuildArch:	noarch

%description
FakePeal (假粉圓體) is an open source Chinese font family
derived from justfont/open-hunnin-font.

%prep
%autosetup -n FakePearl-%version

%build

%install
mkdir -p %buildroot/%_datadir/fonts/fakepearl
install -Dm644 tw/*.ttf %buildroot/%_datadir/fonts/fakepearl/


%files
%doc README.md
%license SIL_Open_Font_License_1.1.txt
%defattr(-,root,root,0755)
/%{_datadir}/fonts/fakepearl/


%changelog
* Mon May 22 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.1
- Initial package
