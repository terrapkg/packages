%global appid com.github.s-adi-dev.nmgui
%global org com.github.s-adi-dev

Name:           nmgui
Version:        1.0.0
Release:        1%?dist
Summary:        A simple and lightweight GTK4-based GUI for managing Wi-Fi using NetworkManager (nmcli) under the hood
License:        GPL-3.0-only
URL:            https://github.com/s-adi-dev/nmgui
Source0:        %url/archive/refs/tags/v%version.tar.gz
Source1:        https://raw.githubusercontent.com/s-adi-dev/nmgui/refs/heads/main/README.md
Source2:        https://raw.githubusercontent.com/s-adi-dev/nmgui/refs/heads/main/nmgui.desktop
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Packager:       madonuko <mado@fyralabs.com>

%description
%summary.

%prep
%autosetup
cp %{S:1} %{S:2} .
cat<<PYEOF > pyproject.toml
[build-system]
requires = ["setuptools>=64.0"]
build-backend = "setuptools.build_meta"
[project]
name = "%name"
version = "%version"
description = "%summary"
license = "GPL-3.0-only"
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
    "nmcli>=1.5.0",
    "PyGObject>=3.52.3",
    "pycairo>=1.28.0",
]
[project.urls]
Homepage = "https://github.com/s-adi-dev/nmgui"
[project.scripts]
nmgui = "nmgui.main:main"
[tool.setuptools.packages.find]
include = ["nmgui*"]
PYEOF
# Add main() entry point function
sed -i '/^if __name__ == "__main__":$/c\def main():' app/main.py
cat >> app/main.py << 'PYEOF'

if __name__ == "__main__":
    main()
PYEOF
mv app nmgui
touch nmgui/__init__.py
# Fix intra-package imports to use nmgui. prefix
sed -i 's/^from models import/from nmgui.models import/' nmgui/main.py nmgui/network_service.py nmgui/ui/*.py
sed -i 's/^from network_service import/from nmgui.network_service import/' nmgui/main.py nmgui/ui/*.py
sed -i 's/^from ui\./from nmgui.ui./' nmgui/main.py nmgui/ui/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %name

%desktop_file_install nmgui.desktop
%terra_appstream

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%_bindir/nmgui
%_appsdir/nmgui.desktop
%_metainfodir/%appid.metainfo.xml

%changelog
* Sun Jun 28 2026 madonuko <mado@fyralabs.com> - 1.0.0-1
- Initial package.
