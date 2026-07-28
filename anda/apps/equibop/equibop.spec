%global debug_package %{nil}
%global appid org.equicord.equibop

Name:           equibop
Version:        3.2.2
Release:        1%{?dist}
Summary:        Custom Discord client focused on performance and Linux support
%electronmeta
License:        GPL-3.0-only AND %electron_license
URL:            https://equibop.org
Source0:        https://github.com/Equicord/Equibop/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  bun-bin
BuildRequires:  jq
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)

%description
Equibop is a custom Discord App aiming to give you better performance
and improve Linux support.

%prep
%autosetup -n Equibop-%{version}

# Set the repository to prevent git-related build errors, but avoid injecting invalid electron-builder schema properties
jq '.repository = "https://github.com/Equicord/Equibop.git"' package.json > package.json.tmp
mv package.json.tmp package.json

%build
%bun_build -c -r buildLibVesktop,package:dir

%install
%electron_install
%terra_appstream

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_metainfodir}/%{appid}.metainfo.xml
