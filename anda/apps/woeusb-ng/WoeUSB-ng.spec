Name:           WoeUSB-ng
Version:        0.2.12
Release:        2%?dist
Summary:        Simple tool that enable you to create your own usb stick with Windows installer
License:        GPL-3.0-only
Requires:       parted dosfstools ntfsprogs p7zip p7zip-plugins xdg-utils grub2-tools
URL:            https://github.com/WoeUSB/WoeUSB-ng
Source:         https://github.com/WoeUSB/WoeUSB-ng/archive/refs/tags/v%version.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/WoeUSB/WoeUSB-ng/pull/79.patch
BuildArch:      noarch
Requires:       python3-%{name} = %{evr}
BuildRequires:  anda-srpm-macros python3-devel python3-installer pyproject-rpm-macros python3dist(pip) python3dist(setuptools) python3dist(termcolor) python3dist(wxpython) python3dist(wheel)

%global _description %{expand:
WoeUSB-ng is a simple tool that enable you to create your own usb stick windows installer from an iso image or a real DVD. This is a rewrite of original WoeUSB.}

%description %_description

%package -n     python3-%{name}
Summary:        Python files for %{name}
Requires:       %{name} = %{evr}
BuildArch:      noarch

%description -n python3-%{name}
Python files needed for %{name}.

%prep
%autosetup -p1

%if 0%{?fedora} > 41
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?fedora} <= 41
%py3_build
%else
%pyproject_wheel
%endif

%install
%if 0%{?fedora} <= 41
%py3_install
%else
%pyproject_install
%pyproject_save_files WoeUSB
%endif
install -Dpm644 miscellaneous/WoeUSB-ng.desktop %buildroot%_datadir/applications/WoeUSB-ng.desktop
install -Dpm644 miscellaneous/com.github.woeusb.woeusb-ng.policy %buildroot%_datadir/polkit-1/actions/com.github.woeusb.woeusb-ng.policy


%check
#pyproject_check_import

%files
%_bindir/woeusb
%_bindir/woeusbgui
%_datadir/applications/WoeUSB-ng.desktop
%_iconsdir/hicolor/scalable/apps/woeusb-logo.png
%_datadir/polkit-1/actions/com.github.woeusb.woeusb-ng.policy

%if 0%{?fedora} <= 41
%files -n python3-%{name}
%{python3_sitelib}/WoeUSB/
%{python3_sitelib}/woeusb_ng-%{version}-py%{python3_version}.egg-info/
%else
%files -n python3-%{name} -f %{pyproject_files}
%endif


%changelog
%autochangelog
