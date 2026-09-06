Name:           mount-manager
Version:        0.1.5
Release:        1%{?dist}
Summary:        SMB Mount Manager helps users mount SMB shares through a simple GTK interface. It checks the share, asks for credentials, tests the mount, and creates a startup mount managed by systemd.
URL:            https://github.com/Xarishark/mount-manager
Source0:        https://github.com/Xarishark/mount-manager/archive/refs/tags/v%{version}.tar.gz
License:        GPL-3.0-only
Requires:       cifs-utils
Requires:       gtk4
Requires:       polkit
Requires:       python3-gobject
Provides:       SMB-Mount-Manager
BuildArch:      noarch
Packager:       Zacharias Xenakis <xarishark@outlook.com>

%description
%{summary}.

%prep
%autosetup -n mount-manager-%{version}

%build

%install
install -Dm 755 mount_manager.py %{buildroot}%{_bindir}/mount-manager
install -Dm 644 data/applications/io.github.xarishark.mount-manager.desktop %{buildroot}%{_appsdir}/io.github.xarishark.mount-manager.desktop
install -Dm 644 data/icons/hicolor/scalable/apps/io.github.xarishark.mount-manager.svg %{buildroot}%{_scalableiconsdir}/io.github.xarishark.mount-manager.svg
install -Dm 644 data/metainfo/io.github.xarishark.mount-manager.metainfo.xml %{buildroot}%{_metainfodir}/io.github.xarishark.mount-manager.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/mount-manager
%{_appsdir}/io.github.xarishark.mount-manager.desktop
%{_scalableiconsdir}/io.github.xarishark.mount-manager.svg
%{_metainfodir}/io.github.xarishark.mount-manager.metainfo.xml

%changelog
* Fri May 15 2026 Zacharias Xenakis <xarishark@outlook.com>
- Initial package
* Fri May 15 2026 Zacharias Xenakis <xarishark@outlook.com>
- migrated to new source GIT
