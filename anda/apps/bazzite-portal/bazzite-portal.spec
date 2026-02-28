Name:           bazzite-portal
Version:        0.1.6
Release:        3%?dist
Summary:        Bazzite Portal is a tabbed frontend for curated script execution, with a focus on distro specific QOL shortcuts
URL:            https://github.com/ublue-os/yafti-gtk
Source0:        https://github.com/ublue-os/yafti-gtk/archive/refs/tags/v%{version}.tar.gz
License:        GPL-3.0-only
Requires:       python3-gobject
Requires:       python3-PyYAML
Requires:       gtk3
Provides:       Bazzite-Portal
BuildArch:      noarch
Packager:       Zacharias Xenakis <xarishark@outlook.com>

%description
%{summary}.

%prep
%autosetup -n yafti-gtk-%{version}

%build

%install
install -Dm 755 yafti_gtk.py %{buildroot}%{_bindir}/yafti_gtk.py
install -Dm 644 io.github.ublue_os.yafti_gtk.desktop %{buildroot}%{_appsdir}/io.github.ublue_os.yafti_gtk.desktop
install -Dm 644 portal.svg %{buildroot}%{_scalableiconsdir}/io.github.ublue_os.yafti_gtk.svg
install -Dm 644 io.github.ublue_os.yafti_gtk.metainfo.xml %{buildroot}%{_metainfodir}/io.github.ublue_os.yafti_gtk.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/yafti_gtk.py
%{_appsdir}/io.github.ublue_os.yafti_gtk.desktop
%{_scalableiconsdir}/io.github.ublue_os.yafti_gtk.svg
%{_metainfodir}/io.github.ublue_os.yafti_gtk.metainfo.xml

%changelog
* Wed Jan 28 2026 Xarishark <xarishark@outlook.com>
- Initial commit