Name:			flutter
Version:		3.22.3
Release:		1%?dist
Summary:		SDK for crafting beautiful, fast user experiences from a single codebase
License:		BSD-3-Clause
URL:			https://flutter.dev
Group:			Development/Building
Source0:		https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_%version-stable.tar.xz
Requires:		bash curl git file which zip xz
Recommends:		mesa-libGLU

%description
Flutter transforms the app development process. Build, test, and deploy
beautiful mobile, web, desktop, and embedded apps from a single codebase.

%prep
tar xf %SOURCE0

%build

%install
mkdir -p %buildroot%_datadir %buildroot%_bindir
mv %name/ %buildroot%_datadir/
ln -s %_datadir/%name/bin/%name %buildroot%_bindir/%name

%files
%_bindir/%name
%_datadir/%name

%changelog
%autochangelog
