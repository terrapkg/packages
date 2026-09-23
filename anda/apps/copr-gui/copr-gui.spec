Name:           copr-gui
%define pypi_name copr_gui
Version:        0.1.5
Release:        1%{?dist}
Summary:        GUI for managing COPR instances

License:        GPL-3.0-or-later
URL:            https://github.com/qr243vbi/%{pypi_name}
Source0:        %{url}/archive/refs/tags/%{version}/%{pypi_name}-%{version}.tar.gz
Source1:        https://github.com/fedora-copr/copr/raw/refs/heads/main/frontend/coprs_frontend/coprs/static/favicon.ico
Source2:        copr-gui.desktop

BuildArch:      noarch
Packager:       moordjin

BuildRequires:  python3-devel

Requires:       qt6-qtdeclarative
Requires:       python3-pyqt6
Requires:       python3-copr

%description
A Qt-based graphical user interface for managing COPR instances.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
install -Dm644 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/copr.png
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/copr-gui.desktop
%pyproject_install
%pyproject_save_files copr_gui copr_gui_source_types

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/copr-gui
%{_iconsdir}/hicolor/32x32/apps/copr.png
%{_datadir}/applications/copr-gui.desktop

%changelog
* Wed Sep 23 2026 moordjin - 0.1.5-1
- Initial package
