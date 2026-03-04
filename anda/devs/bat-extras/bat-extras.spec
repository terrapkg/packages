%define debug_package %{nil}

Name:           bat-extras
Version:        2024.08.24
Release:        1%?dist
Summary:        Bash scripts that integrate bat with various command line tools

License:        MIT
URL:            https://github.com/eth-p/bat-extras
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  bash
Requires:       bash
BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup


%build


%install
./build.sh --install --prefix=%{buildroot}%{_prefix} --no-verify

mkdir -p %{buildroot}%{_mandir}/man1/
cp -v man/* %{buildroot}%{_mandir}/man1/

chmod -x %{buildroot}%{_mandir}/man1/*


%files
%license LICENSE.md
%{_bindir}/bat*
%{_bindir}/prettybat
%{_mandir}/man1/*

%changelog
* Mon Oct 03 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 2022.07.27-1
- Initial release
