Summary:        A modernist sans serif font
Name:           manrope-fonts
Version:        1
Release:        3%{?dist}
License:        OFL
URL:            https://manropefont.com/

Source0:        https://manropefont.com/manrope.zip
Source1:        README.md
BuildArch:      noarch

%description
Manrope – modern geometric sans-serif

%prep
yes A | %autosetup -c

%build

%install
install -d %{buildroot}%{_datadir}/fonts/manrope
install -pm 644 fonts/otf/*.otf %{buildroot}%{_datadir}/fonts/manrope
install -pm 644 fonts/ttf/*.ttf %{buildroot}%{_datadir}/fonts/manrope
install -pm 644 fonts/variable/Manrope* %{buildroot}%{_datadir}/fonts/manrope

install -pm 0644 %SOURCE1 README.md

# Install licenses
mkdir -p licenses
install -pm 0644 %SOURCE1 licenses/LICENSE

%files
%doc README.md
%doc documentation.html
%license licenses/LICENSE
%{_datadir}/fonts/manrope/*

 
%changelog
* Tue Jan 10 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 1-3
- Ported from tauOS


* Sat May 14 2022 Jamie Murphy <jamie@fyralabs.com> - 1-1
- Fix specfile

* Sat May 14 2022 Lains <lainsce@airmail.cc> - 1-1
- Initial release
