Name:           rEFInd_GUI
Version:        3.4.1
Release:        1%{?dist}
Summary:        Small GUI for customizing and installing rEFInd bootloader

License:        MIT
URL:            https://github.com/jlobue10/rEFInd_GUI
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  systemd-rpm-macros
Requires:       mokutil
Requires:       sbsigntools
Requires:       xterm
Requires:       zenity
Provides:       refind_gui
Conflicts:      refind-gui

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C

%conf
pushd GUI/src
%cmake
popd

%build
pushd GUI/src
%cmake_build
popd

%install
install -Dm755 GUI/src/redhat-linux-build/rEFInd_GUI            %{buildroot}%{_bindir}/rEFInd_GUI
install -Dm755 GUI/src/redhat-linux-build/rEFInd_GUI_helper     %{buildroot}%{_bindir}/rEFInd_GUI_helper
install -Dm644 rEFInd_bg_randomizer.service                     %{buildroot}%{_unitdir}/rEFInd_bg_randomizer.service
install -Dm644 rEFInd_theme_randomizer.service                  %{buildroot}%{_unitdir}/rEFInd_theme_randomizer.service

%post
%systemd_post rEFInd_bg_randomizer.service rEFInd_theme_randomizer.service

%preun
%systemd_preun rEFInd_bg_randomizer.service rEFInd_theme_randomizer.service

%postun
%systemd_postun_with_restart rEFInd_bg_randomizer.service rEFInd_theme_randomizer.service

%files
%doc README.md
%license LICENSE
%{_unitdir}/rEFInd_bg_randomizer.service
%{_unitdir}/rEFInd_theme_randomizer.service
%{_bindir}/rEFInd_GUI
%{_bindir}/rEFInd_GUI_helper

%changelog
* Sun Aug 23 2026 Owen Zimmerman <owen@fyralabs.com> - 3.4.1-1
- Initial commit
