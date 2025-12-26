%global appid com.github.snow

Name:           snow
Version:        1.2.0
Release:        2%?dist
Summary:        Classic Macintosh emulator
URL:            https://github.com/twvd/snow
Source0:        %url/archive/refs/tags/v%version.tar.gz
Source1:        snow.desktop
Source2:        %appid.metainfo.xml
License:        MIT

BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  mold
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  terra-appstream-helper
BuildRequires:  SDL2-devel
Provides:       snowemu

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Snow emulates classic (Motorola 68k-based) Macintosh computers.
It features a graphical user interface to operate and debug the emulated machine.
The aim of this project is to emulate the Macintosh on a hardware-level as much as possible,
as opposed to emulators that patch the ROM or intercept system calls.

%package doc
Summary:        Documentation files for %{name}

%description doc
Documentation files for %{name}

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
mkdir -p %{buildroot}%{_pkgdocdir}
install -Dm755 target/rpm/snow_frontend_egui %{buildroot}%{_bindir}/snowemu

install -Dm644 docs/images/snow_icon.png     %{buildroot}%{_hicolordir}/1024x1024/apps/snow_icon.png

install -Dm644 %{SOURCE1}                    %{buildroot}%{_appsdir}/snow.desktop

cp -a docs/*                                 %{buildroot}%{_pkgdocdir}/
rm %{buildroot}%{_pkgdocdir}/*.toml
rm %{buildroot}%{_pkgdocdir}/images/*.icns
rm %{buildroot}%{_pkgdocdir}/images/*.ico
rm -r %{buildroot}%{_pkgdocdir}/theme

%terra_appstream -o %{SOURCE2}

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%check
desktop-file-validate %{buildroot}%{_appsdir}/snow.desktop

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/snowemu
%{_hicolordir}/1024x1024/apps/snow_icon.png
%{_appsdir}/snow.desktop
%{_metainfodir}/%appid.metainfo.xml

%files doc
%license LICENSE
%doc %{_pkgdocdir}/*

%changelog
* Tue Dec 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
