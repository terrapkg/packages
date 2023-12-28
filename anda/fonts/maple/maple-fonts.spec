%define debug_package %nil
%define _ttfontsdir %{_datadir}/fonts/maple

Name:           maple-fonts
Version:        6.4
Release:        %autorelease
Summary:        Open source monospace & nerd font with round corner and ligatures.
License:        OFL-1.1
URL:            https://github.com/subframe7536/Maple-font
Source0:        %{url}/releases/download/v%{version}/MapleMono-SC-NF.zip
Source1:        %{url}/releases/download/v%{version}/MapleMono-ttf.zip
Source2:        %{url}/releases/download/v%{version}/MapleMono-NF.zip
Source3:        https://raw.githubusercontent.com/subframe7536/maple-font/main/OFL.txt
BuildArch:      noarch
BuildRequires:  unzip
 
%description
%summary

%prep
%setup -c -n %{name}-%{version}
unzip %{S:1}
unzip %{S:2}
cp %{S:3} .
 
%build
 
%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 *.ttf %{buildroot}%{_ttfontsdir}
 
%post
 
%postun
 
%files
%license OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf
 
%changelog
* Tue Dec 26 2023 madoka773 <valigarmanda55@gmail.com> - 6.4
- Initial package
