%define debug_package %{nil}

Name:           bat-extras
Version:        2022.07.27
Release:        1%{?dist}
Summary:        Bash scripts that integrate bat with various command line tools

License:        MIT
URL:            https://github.com/eth-p/bat-extras
Source0:        https://github.com/eth-p/bat-extras/archive/refs/tags/v2022.07.27.tar.gz

BuildRequires:  bash
Requires:       bash

%description
%{summary}.

%prep
%autosetup -n bat-extras-%{version}


%build
# ./build.sh --no-verify


%install
./build.sh --install --prefix=%{buildroot}%{_prefix}

mkdir -p %{buildroot}%{_mandir}/man1/
cp -v man/* %{buildroot}%{_mandir}/man1/


%files
%license LICENSE.md
%doc doc/
%{_bindir}/bat*
%{_bindir}/prettybat
%{_mandir}/man1/*

%changelog
* Mon Oct 03 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial release
