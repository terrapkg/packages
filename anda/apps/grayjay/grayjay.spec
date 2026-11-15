%define __strip /bin/true
%define debug_package %nil

Name:           grayjay
Version:        18
Release:        1%?dist
Summary:        Watch content on your own terms, ensuring you retain full ownership and control over what you watch
License:        SFL-1.1
URL:            https://grayjay.app/desktop
BuildRequires:  npm dotnet-host dotnet-hostfxr-8.0 dotnet-sdk-8.0
BuildRequires:  anda-srpm-macros git-core
BuildRequires:  desktop-file-utils

%description
Grayjay is a multi-platform media application that allows you to watch content from multiple platforms in a single application. Using an extendable plugin system developers can make new integrations with additional platforms. Plugins are cross-compatible between Android and Desktop.

%prep
%git_clone https://gitlab.futo.org/videostreaming/syncserver

%build
pushd Grayjay.Desktop.Web
npm i
rm -rf dist
npm run build
popd

pushd Grayjay.Desktop.CEF
rm -rf bin
dotnet publish -c Release
popd

# Copy wwwroot
dir=$(ls Grayjay.Desktop.CEF/bin/Release/net8.0)
mkdir -p Grayjay.Desktop.CEF/bin/Release/net8.0/$dir/publish/wwwroot
cp -r Grayjay.Desktop.Web/dist Grayjay.Desktop.CEF/bin/Release/net8.0/$dir/publish/wwwroot/web

gendesk \
    --name=Grayjay          \
    --pkgname=%name         \
    --pkgdesc='%summary'    \
    --exec=%_bindir/grayjay \
    --icon=%_datadir/grayjay/logo.ico

%install
mkdir -p %buildroot%_datadir/grayjay %buildroot%_bindir
cp -r Grayjay.Desktop.CEF/bin/Release/net8.0/*/publish/* %buildroot%_datadir/grayjay/
ln -s %_datadir/Grayjay %buildroot%_bindir/grayjay
install -Dm644 %buildroot%_datadir/grayjay/logo.ico %buildroot%_datadir/pixmaps/grayjay.ico
install -Dm644 grayjay.desktop -t %buildroot%_datadir/applications

%files
%doc README.md
%license LICENSE.md
%_bindir/grayjay
%_datadir/applications/grayjay.desktop
%_datadir/grayjay/
%_iconsdir/hicolor/256x256/apps/grayjay.ico

%changelog
* Sat Jun 27 2026 madonuko <madonuko@outlook.com> - 18-1
- Initial package.
