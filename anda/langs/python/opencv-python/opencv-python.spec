%global pypi_name opencv-python
%global _desc Wrapper package for OpenCV python bindings.

Name:			python-%{pypi_name}
Version:		5.0.0.93
Release:		1%{?dist}
Summary:		Wrapper package for OpenCV python bindings
License:		MIT
URL:			https://pypi.org/project/opencv-python/
Source0:		%{pypi_source opencv_python}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-numpy
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-scikit-build-core
BuildRequires:  chrpath

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -C

%build
export SKBUILD_CMAKE_ARGS="-DCMAKE_SKIP_RPATH=ON;-DCMAKE_SKIP_BUILD_RPATH=ON;-DCMAKE_SKIP_INSTALL_RPATH=ON"
%pyproject_wheel

%install
%pyproject_install
find %{buildroot} -name '*.so*' -exec chrpath --delete {} \; 2>/dev/null || :
%pyproject_save_files cv2

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
* Wed Sep 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
