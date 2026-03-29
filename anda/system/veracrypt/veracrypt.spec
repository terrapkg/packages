%define debug_package %{nil}
%define _unpackaged_files_terminate_build 0
%define appid jp.veracrypt.veracrypt
%global ver VeraCrypt_1.26.24
%global sanitized_ver %(echo %{ver} | sed 's/^VeraCrypt_//')

Name:           veracrypt
Version:        %{sanitized_ver}
Release:        2%?dist
Summary:        Disk encryption with strong security based on TrueCrypt
URL:            https://veracrypt.jp/en/Home.html
Source0:        https://github.com/veracrypt/VeraCrypt/archive/refs/tags/VeraCrypt_%version.tar.gz
Source1:        %{appid}.metainfo.xml
License:        Apache-2.0 AND TrueCrypt-License-version-3.0 AND LGPL-3.0-only AND BSD-2-Clause AND Zlib AND BSD-3-Clause AND Public Domain
BuildRequires:  make
BuildRequires:  yasm
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  clang
BuildRequires:  pkgconf-pkg-config
BuildRequires:  wxGTK-devel
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pcsc-lite-devel
Requires:       wxGTK-devel

Provides:       VeraCrypt

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package        lang
Summary:        Translations for package %{name}
Requires:       %{name} = %{evr}
Supplements:    %{name}
Provides:       %{name}-lang-all = %{evr}
BuildArch:      noarch

%description    lang
%{summary}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{evr}
Supplements:    %{name}
BuildArch:      noarch

%description    doc
%{summary}.

%prep
%autosetup -n VeraCrypt-VeraCrypt_%{version}

%build
%make_build -C src

%install
%make_install -C src
cp -r doc/ %{buildroot}%{_pkgdocdir}/
%terra_appstream -o %{SOURCE1}

%files
%doc README.md
%license License.txt
%{_bindir}/veracrypt
%{_bindir}/veracrypt-uninstall.sh
%{_appsdir}/veracrypt.desktop
%{_datadir}/mime/packages/veracrypt.xml
%{_datadir}/pixmaps/veracrypt.xpm
%{_metainfodir}/%{appid}.metainfo.xml

%files lang
%{_datadir}/veracrypt/languages/*

%files doc
%{_pkgdocdir}/

%changelog
* Sat Feb 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
