%global __brp_mangle_shebangs %{nil}
%global appid com.github.neohtop

Name:           neohtop
Version:        1.2.0
Release:        2%?dist
Summary:        System monitoring on steroids
License:        MIT
URL:            https://github.com/Abdenasser/neohtop
Source0:        %url/archive/refs/tags/v%version.tar.gz
Source1:        NeoHtop.desktop
Source2:        com.github.neohtop.metainfo.xml
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildRequires:  rust
BuildRequires:  %tauri_buildrequires
BuildRequires:  libsoup3-devel
BuildRequires:  gtk3-devel
BuildRequires:  rust-gdk-pixbuf-sys-devel
BuildRequires:  glib2-devel
BuildRequires:  openssl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  anda-srpm-macros
BuildRequires:  terra-appstream-helper

Provides:       NeoHtop

%description
%summary.

%prep
%autosetup -n neohtop-%version
%tauri_prep

%build
%npm_build -B

%install
install -Dpm755 src-tauri/target/release/NeoHtop %{buildroot}%{_bindir}/NeoHtop
install -Dpm644 %{SOURCE1}                       %{buildroot}%{_appsdir}/NeoHtop.desktop
# don't mind the numbers not matching, this is how the offical rpm installs these files
install -Dpm644 src-tauri/icons/128x128@2x.png   %{buildroot}%{_hicolordir}/256x256@2/apps/NeoHtop.png
install -Dpm644 src-tauri/icons/32x32.png        %{buildroot}%{_hicolordir}/32x32/apps/NeoHtop.png
install -Dpm644 src-tauri/icons/128x128.png      %{buildroot}%{_hicolordir}/128x128/apps/NeoHtop.png

%terra_appstream -o %{SOURCE2}

%check
%__desktop_file_validate %{buildroot}%{_appsdir}/NeoHtop.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/NeoHtop
%{_appsdir}/NeoHtop.desktop
%{_hicolordir}/256x256@2/apps/NeoHtop.png
%{_hicolordir}/32x32/apps/NeoHtop.png
%{_hicolordir}/128x128/apps/NeoHtop.png
%{_metainfodir}/com.github.neohtop.metainfo.xml

%changelog
* Wed Dec 24 2025 Owen Zimmerman <owen@fyralabs.com>
- Clean up build, add %check 
* Wed Nov 19 2025 Owen Zimmerman <owen@fyralabs.com>
- Add metainfo
* Sat Feb 15 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial package
