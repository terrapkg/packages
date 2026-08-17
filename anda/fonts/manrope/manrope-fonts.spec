Summary:        A modernist sans serif font
Name:           manrope-fonts
Version:        4.505
Release:        1%{?dist}
License:        OFL-1.1
#URL:            https://github.com/sharanda/manrope
URL:            https://github.com/terrapkg/pkg-manrope-fonts

Source0:        %url/archive/%version.tar.gz
BuildArch:      noarch

%description
Manrope – modern geometric sans-serif

%prep
%autosetup -n pkg-manrope-fonts-%version

%build

%install
install -d %{buildroot}%{_datadir}/fonts/manrope
install -pm 644 manrope-* %{buildroot}%{_datadir}/fonts/manrope
install -pm 644 Manrope* %{buildroot}%{_datadir}/fonts/manrope

%files
%doc README.md
%doc documentation.html
%license OFL.txt
%{_datadir}/fonts/manrope/*
