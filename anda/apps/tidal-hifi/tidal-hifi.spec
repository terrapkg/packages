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
%npm_build -B

%install
%electron_install

%files
%doc README.md
%license LICENSE
%_bindir/%name
