%global appid org.equibop.Equibop

Name:           Equibop
Version:        3.2.1
Release:        1%?dist
Summary:        Equibop is a custom Discord App aiming to give you better performance and improve linux support
%electronmeta
License:        GPL-3.0-only AND %electron_license
URL:            https://equibop.org
Source0:        https://github.com/Equicord/Equibop/archive/refs/tags/v%version.tar.gz
BuildRequires:  bun-bin

%description
Equibop is a custom Discord App aiming to give you better performance and improve linux support.

%prep
%autosetup

%build
%bun_build -c -r buildLibVesktop,build

%install
%electron_install

%terra_appstream

%files
%license LICENSE
%doc README.md
%_bindir/Equibop
