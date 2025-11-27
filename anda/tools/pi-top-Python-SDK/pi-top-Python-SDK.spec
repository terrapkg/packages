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
%pyproject_save_files pitop

%dnl %pyproject_save_files battery
%dnl %pyproject_save_files camera
%dnl %pyproject_save_files cli
%dnl %pyproject_save_files common
%dnl %pyproject_save_files core
%dnl %pyproject_save_files display
%dnl %pyproject_save_files keyboard
%dnl %pyproject_save_files miniscreen
%dnl %pyproject_save_files pitop
%dnl %pyproject_save_files pma
%dnl %pyproject_save_files processing
%dnl %pyproject_save_files robotics
%dnl %pyproject_save_files simulation
%dnl %pyproject_save_files system

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc

%files battery -f %{pyproject_files}

%files camera -f %{pyproject_files}

%files cli -f %{pyproject_files}

%files common -f %{pyproject_files}

%files core -f %{pyproject_files}

%files display -f %{pyproject_files}

%files keyboard -f %{pyproject_files}

%files miniscreen -f %{pyproject_files}

%files pitop -f %{pyproject_files}

%files pma -f %{pyproject_files}

%files processing -f %{pyproject_files}

%files robotics -f %{pyproject_files}

%files simulation -f %{pyproject_files}

%files system -f %{pyproject_files}

%changelog
* Wed Oct 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
