%global commit ffa0fdf363527c9993b8836cce48cd12bd2b81ba

Summary:        A modernist sans serif font
Name:           manrope-fonts
Version:        4.505
Release:        1%{?dist}
License:        OFL-1.1
URL:            https://github.com/sharanda/manrope

Source0:        %url/archive/%commit.tar.gz
BuildArch:      noarch

%description
Manrope – modern geometric sans-serif

%prep
%autosetup -n manrope-%commit

%build

%install
install -d %{buildroot}%{_datadir}/fonts/manrope
install -pm 644 fonts/otf/*.otf %{buildroot}%{_datadir}/fonts/manrope
install -pm 644 fonts/ttf/*.ttf %{buildroot}%{_datadir}/fonts/manrope
install -pm 644 fonts/variable/Manrope* %{buildroot}%{_datadir}/fonts/manrope

%files
%doc README.md
%doc documentation.html
%license OFL.txt
%{_datadir}/fonts/manrope/*

 
%changelog
* Thu Jun 22 2023 windowsboy111 <windowsboy111@fyralabs.com> - 4.505-1
- Bump version and fix sources

* Tue Jan 10 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 1-3
- Ported from tauOS

* Sat May 14 2022 Jamie Murphy <jamie@fyralabs.com> - 1-1
- Fix specfile

* Sat May 14 2022 Lains <lainsce@airmail.cc> - 1-1
- Initial release
