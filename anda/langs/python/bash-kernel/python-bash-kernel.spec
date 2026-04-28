# Mostly taken from Fedora, but updated because despite Fedora marking this project as abandoned it is not

%global pypi_name bash_kernel
%global real_name bash-kernel

Name:           python-%{real_name}
Version:        0.10.0
Release:        2%{?dist}
Summary:        Bash kernel for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/takluyver/bash_kernel
Source:         %{pypi_source}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(filetype)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(pip)
BuildRequires:  %{py3_dist docutils}
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
This package contains a Jupyter kernel for bash.

%package -n python3-%{real_name}
Summary:        %{summary}
Requires:       bash
Requires:       python-jupyter-filesystem

%description -n python3-%{real_name}
This package contains a Jupyter kernel for bash.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

# Work around an install error
sed -i 's/from \.resources/from %{pypi_name}.resources/' %{pypi_name}/install.py

%build
%pyproject_wheel
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
export PYTHONPATH=$PWD
cd %{pypi_name}
%{python3} install.py --prefix %{buildroot}%{_prefix}
cd -

%check
%pyproject_check_import

%files -n python3-%{real_name} -f %{pyproject_files}
%doc README.html
%license LICENSE
%{_datadir}/jupyter/kernels/bash/

%changelog
* Mon May 26 2025 Gilver E. <rockgrub@disroot.org> - 0.10.0-1
- Initial port from Fedora
