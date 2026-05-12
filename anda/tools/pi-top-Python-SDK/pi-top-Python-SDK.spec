%global pypi_name pitop
%global _desc A simple, modular interface for interacting with a pi-top and its related accessories and components.
%global ver 0.35.0-4
%global sanitized_ver %(echo %{ver} | sed 's/-/^/g')

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

%package -n python3-pitop-battery
Summary:    Battery support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-battery
Battery support for the pi-top sdk.

%package    -n python3-pitop-camera
Summary:    Camera support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-camera
Camera support for the pi-top sdk.

%package    -n python3-pitopcli
Summary:    cli support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitopcli
cli support for the pi-top sdk.

%package    -n python3-pitop-core
Summary:    core for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-core
core for the pi-top sdk.

%package    -n python3-pitop-common
Summary:    Support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-common
Support for the pi-top sdk.

%package    -n python3-pitop-display
Summary:    Display support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-display
Display support for the pi-top sdk.

%package    -n python3-pitop-keyboard
Summary:    Keyboard support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-keyboard
Keyboard support for the pi-top sdk.

%package    -n python3-pitop-miniscreen
Summary:    Miniscreen support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-miniscreen
Miniscreen support for the pi-top sdk.

%package    -n python3-pitop-pma
Summary:    pma support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-pma
pma support for the pi-top sdk.

%package    -n python3-pitop-processing
Summary:    Processing support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-processing
Processing support for the pi-top sdk.

%package    -n python3-pitop-robotics
Summary:    Robotics support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-robotics
Robotics support for the pi-top sdk.

%package    -n python3-pitop-simulation
Summary:    Simulation support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-simulation
Simulation support for the pi-top sdk.

%package    -n python3-pitop-system
Summary:    System support for the pi-top sdk
Requires:   python3-pitop

%description -n python3-pitop-system
System support for the pi-top sdk.

%prep
%autosetup -n pi-top-Python-SDK-%{ver}

%pyproject_patch_dependency flask:drop_constraints
%pyproject_patch_dependency flask-cors:drop_constraints
%pyproject_patch_dependency gevent:drop_constraints
%pyproject_patch_dependency gpiozero:drop_constraints

%build
pushd packages/battery
%pyproject_wheel
popd
pushd packages/camera
%pyproject_wheel
popd
pushd packages/cli
%pyproject_wheel
popd
pushd packages/common
%pyproject_wheel
popd
pushd packages/core
%pyproject_wheel
popd
pushd packages/display
%pyproject_wheel
popd
pushd packages/keyboard
%pyproject_wheel
popd
pushd packages/miniscreen
%pyproject_wheel
popd
pushd packages/pitop
%pyproject_wheel
popd
pushd packages/pma
%pyproject_wheel
popd
pushd packages/processing
%pyproject_wheel
popd
pushd packages/robotics
%pyproject_wheel
popd
pushd packages/simulation
%pyproject_wheel
popd
pushd packages/system
%pyproject_wheel
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

rm -rf %{buildroot}/usr/lib/python3.14/site-packages/pitop/protoplus/

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pitop-*.dist-info/
%{python3_sitelib}/pitop/__pycache__/
%{python3_sitelib}/pitop/__init__.py
%{python3_sitelib}/pitop/*.py
%{python3_sitelib}/pitop/labs/
%{python3_sitelib}/pitop/pulse/

%files -n python3-pitop-battery
%{python3_sitelib}/pitop_battery-*.dist-info/
%{python3_sitelib}/pitop/battery/

%files -n python3-pitop-camera
%{python3_sitelib}/pitop_camera-*.dist-info/
%{python3_sitelib}/pitop/camera/

%files -n python3-pitopcli
%{python3_sitelib}/pitopcli-*.dev1.dist-info/
%{_bindir}/pi-top
%{_bindir}/pt
%{python3_sitelib}/pitopcli/

%files -n python3-pitop-common
%{python3_sitelib}/pitop_common-*.dist-info/
%{python3_sitelib}/pitop/common/

%files -n python3-pitop-core
%{python3_sitelib}/pitop_core-*.dist-info/
%{python3_sitelib}/pitop/core/

%files -n python3-pitop-display
%{python3_sitelib}/pitop_display-*.dist-info/
%{python3_sitelib}/pitop/display/

%files -n python3-pitop-keyboard
%{python3_sitelib}/pitop_keyboard-*.dist-info/
%{python3_sitelib}/pitop/keyboard/

%files -n python3-pitop-miniscreen
%{python3_sitelib}/pitop_miniscreen-*.dist-info/
%{python3_sitelib}/pitop/miniscreen/

%files -n python3-pitop-pma
%{python3_sitelib}/pitop_pma-*.dist-info/
%{python3_sitelib}/pitop/pma/

%files -n python3-pitop-processing
%{python3_sitelib}/pitop_processing-*.dist-info/
%{python3_sitelib}/pitop/processing/

%files -n python3-pitop-robotics
%{python3_sitelib}/pitop_robotics-*.dist-info/
%{python3_sitelib}/pitop/robotics/

%files -n python3-pitop-simulation
%{python3_sitelib}/pitop_simulation-*.dist-info/
%{python3_sitelib}/pitop/simulation/

%files -n python3-pitop-system
%{python3_sitelib}/pitop_system-*.dist-info/
%{python3_sitelib}/pitop/system/

%changelog
* Wed May 06 2026 Owen Zimmerman <owen@fyralabs.com>
- Update files and build/prep steps

* Wed Oct 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
