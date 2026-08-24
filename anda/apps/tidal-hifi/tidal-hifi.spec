Name:           tidal-hifi
Version:        8.1.2
Release:        1%?dist
Summary:        The web version of Tidal running in electron with hifi support thanks to widevine
%electronmeta
License:        MIT AND %electron_license
URL:            https://github.com/Mastermindzh/tidal-hifi
Source0:        %url/archive/refs/tags/%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  nodejs-packaging

%description
The web version of TIDAL running in electron with Hi-Fi (High & Max) support thanks to widevine.

%prep
%autosetup

%build
%npm_build -BC ./build/electron-builder.base.yml

%install
%electron_install

%files
%doc README.md
%license LICENSE
%_bindir/%name

%changelog
* Mon Aug 17 2026 madonuko <mado@fyralabs.com>
- Initial package
