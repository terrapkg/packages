%global appid   com.fyralabs.PackageKit-bootc
%global appstream_component addon
Name:           PackageKit-bootc
Version:        0.1.0
Release:        1%{?dist}
Summary:        bootc backend for PackageKit
Packager:       Cappy Ishihara <cappy@fyralabs.com>

License:        GPL-3.0-or-later
URL:            https://github.com/FyraLabs/PackageKit-bootc
Source0:        %{appid}.metainfo.xml

BuildRequires:  PackageKit-glib-devel
BuildRequires:  glib2-devel
BuildRequires:  PackageKit-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  anda-srpm-macros
Requires:       PackageKit
Requires:       bootc

%description
%{summary}.

%prep
%git_clone %{url}.git v%{version}


%build
%meson
%meson_build



%install
%meson_install
%terra_appstream -o %{SOURCE0}

%files
%license LICENSE
%doc README.md
%{_libdir}/packagekit-backend/libpk_backend_bootc.so
%{_datadir}/PackageKit/helpers/bootc/bootcBackend.py
%{_metainfodir}/%{appid}.metainfo.xml


%changelog
* Thu Dec 04 2025 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
