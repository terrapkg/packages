%global pypi_name pitop
%global _desc A simple, modular interface for interacting with a pi-top and its related accessories and components.
%global ver 0.35.0-4
%global sanitized_ver %(echo %{ver} | sed 's/-//g')

Name:			python-%{pypi_name}
Version:		%{sanitized_ver}
Release:		1%?dist
Summary:		pi-top's Python SDK pitop package
License:		Apache-2.0
URL:			https://github.com/pi-top/pi-top-Python-SDK
Source0:		%{url}/archive/v%{ver}/%{name}-%{ver}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-devel
BuildRequires:  python3-installer
BuildRequires:  git

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       pitop
Provides:       pi-top-Python-SDK
Provides:       pi-top-python-sdk
Provides:       pi-top-sdk
Provides:       pitop-sdk
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%package    battery
Summary:    Battery support for the pi-top sdk
Requires:   python3-pitop

%description battery
Battery support for the pi-top sdk.

%package    camera
Summary:    Camera support for the pi-top sdk
Requires:   python3-pitop

%description camera
Camera support for the pi-top sdk.

%package    cli
Summary:    cli support for the pi-top sdk
Requires:   python3-pitop

%description cli
cli support for the pi-top sdk.

%package    core
Summary:    core for the pi-top sdk
Requires:   python3-pitop

%description core
core for the pi-top sdk.

%package    common
Summary:    Support for the pi-top sdk
Requires:   python3-pitop

%description common
Support for the pi-top sdk.

%package    display
Summary:    Display support for the pi-top sdk
Requires:   python3-pitop

%description display
Display support for the pi-top sdk.

%package    keyboard
Summary:    Keyboard support for the pi-top sdk
Requires:   python3-pitop

%description keyboard
Keyboard support for the pi-top sdk.

%package    miniscreen
Summary:    Miniscreen support for the pi-top sdk
Requires:   python3-pitop

%description miniscreen
Miniscreen support for the pi-top sdk.

%package    pitop
Summary:    pitop support for the pi-top sdk
Requires:   python3-pitop

%description pitop
pitop support for the pi-top sdk.

%package    pma
Summary:    pma support for the pi-top sdk
Requires:   python3-pitop

%description pma
pma support for the pi-top sdk.

%package    processing
Summary:    Processing support for the pi-top sdk
Requires:   python3-pitop

%description processing
Processing support for the pi-top sdk.

%package    robotics
Summary:    Robotics support for the pi-top sdk
Requires:   python3-pitop

%description robotics
Robotics support for the pi-top sdk.

%package    simulation
Summary:    Simulation support for the pi-top sdk
Requires:   python3-pitop

%description simulation
Simulation support for the pi-top sdk.

%package    system
Summary:    System support for the pi-top sdk
Requires:   python3-pitop

%description system
System support for the pi-top sdk.

%prep
%autosetup -n pi-top-Python-SDK-%{ver}

%build
%pyproject_wheel
pushd packages
pushd battery
%pyproject_wheel
popd
pushd cli
%pyproject_wheel
popd
pushd common
%pyproject_wheel
popd
pushd core
%pyproject_wheel
popd
pushd display
%pyproject_wheel
popd
pushd keyboard
%pyproject_wheel
popd
pushd miniscreen
%pyproject_wheel
popd
pushd pitop
%pyproject_wheel
popd
pushd pma
%pyproject_wheel
popd
pushd processing
%pyproject_wheel
popd
pushd robotics
%pyproject_wheel
popd
pushd simulation
%pyproject_wheel
popd
pushd system
%pyproject_wheel
popd
popd

%install
%pyproject_install

pushd packages/battery
%pyproject_install
popd

pushd packages/camera
%pyproject_install
popd

pushd packages/cli
%pyproject_install
popd

pushd packages/common
%pyproject_install
popd

pushd packages/core
%pyproject_install
popd

pushd packages/display
%pyproject_install
popd

pushd packages/keyboard
%pyproject_install
popd

pushd packages/miniscreen
%pyproject_install
popd

pushd packages/pitop
%pyproject_install
popd

pushd packages/pma
%pyproject_install
popd

pushd packages/processing
%pyproject_install
popd

pushd packages/robotics
%pyproject_install
popd

pushd packages/simulation
%pyproject_install
popd

pushd packages/system
%pyproject_install
popd

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pitop-%{version}.dist-info/

%files battery
%{python3_sitelib}/pitop_battery-%{version}.dist-info/
%{python3_sitelib}/pitop/battery/

%files camera
%{python3_sitelib}/pitop_camera-%{version}.dist-info/
%{python3_sitelib}/pitop/camera/

%files cli
%{python3_sitelib}/pitop_cli-%{version}.dist-info/
%{python3_sitelib}/pitop/cli/

%files common
%{python3_sitelib}/pitop_common-%{version}.dist-info/
%{python3_sitelib}/pitop/common/

%files core
%{python3_sitelib}/pitop_core-%{version}.dist-info/
%{python3_sitelib}/pitop/core/

%files display
%{python3_sitelib}/pitop_display-%{version}.dist-info/
%{python3_sitelib}/pitop/display/

%files keyboard
%{python3_sitelib}/pitop_keyboard-%{version}.dist-info/
%{python3_sitelib}/pitop/keyboard/

%files miniscreen
%{python3_sitelib}/pitop_miniscreen-%{version}.dist-info/
%{python3_sitelib}/pitop/miniscreen/

%files pitop
%{python3_sitelib}/pitop_pitop-%{version}.dist-info/
%{python3_sitelib}/pitop/pitop/

%files pma
%{python3_sitelib}/pitop_pma-%{version}.dist-info/
%{python3_sitelib}/pitop/pma/

%files processing
%{python3_sitelib}/pitop_processing-%{version}.dist-info/
%{python3_sitelib}/pitop/processing/

%files robotics
%{python3_sitelib}/pitop_robotics-%{version}.dist-info/
%{python3_sitelib}/pitop/robotics/

%files simulation
%{python3_sitelib}/pitop_simulation-%{version}.dist-info/
%{python3_sitelib}/pitop/simulation/

%files system
%{python3_sitelib}/pitop_system-%{version}.dist-info/
%{python3_sitelib}/pitop/system/

%changelog
* Wed Oct 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
