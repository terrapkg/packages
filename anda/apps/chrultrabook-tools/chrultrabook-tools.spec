Name:           chrultrabook-tools
Version:        3.1.2
Release:        1%?dist
Summary:        User-friendly configuration utility for Chromebooks running an alternate OS
URL:            https://github.com/death7654/Chrultrabook-Tools
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        GPLv3

BuildRequires:  cargo
BuildRequires:  glib2
BuildRequires:  glib2-devel
BuildRequires:  gtk3
BuildRequires:  gtk3-devel
BuildRequires:  javascriptcoregtk4.1
BuildRequires:  javascriptcoregtk4.1-devel
BuildRequires:  libsoup3
BuildRequires:  libsoup3-devel
BuildRequires:  libappindicator-gtk3
BuildRequires:  libappindicator-devel
BuildRequires:  gstreamer1
BuildRequires:  gstreamer1-devel
BuildRequires:  patchelf
BuildRequires:  libstdc++-static
BuildRequires:  libxdo-devel
BuildRequires:  anda-srpm-macros
BuildRequires:  rustc
BuildRequires:  %{tauri_buildrequires -a}

Requires:       chromium-ectool
Requires:       coreboot-utils-cbmem
Requires:       libayatana-appindicator-gtk3
Requires:       libayatana-ido-gtk3
Requires:       libayatana-indicator-gtk3

Packager:       Owen Zimmerman owen@fyralabs.com

%description
%summary.

%prep
%autosetup -n Chrultrabook-Tools-%version
%tauri_prep

%build
%npm_build -r build -B

%install
%tauri_install
%tauri_cargo_license > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%_bindir/chrultrabook-tools
%{_datadir}/applications/chrultrabook-tools.desktop
%{_hicolordir}/*x*/apps/Chrultrabook-Tools.png

%changelog
* Mon Jan 19 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
