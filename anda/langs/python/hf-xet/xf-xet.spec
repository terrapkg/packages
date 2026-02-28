%global pypi_name hf-xet
%global _desc xet client tech, used in huggingface_hub.

Name:			python-%{pypi_name}
Version:		1.2.0
Release:		1%?dist
Summary:		xet client tech, used in huggingface_hub
License:		Apache-2.0
URL:			https://github.com/huggingface/xet-core
Source0:		%url/archive/refs/tags/v%version.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

BuildRequires: python
BuildRequires: gdb
BuildRequires: cargo
BuildRequires: rust-src
BuildRequires: pkgconfig(libssh2)
BuildRequires: lmdb-devel
BuildRequires: maturin

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%package -n     python3-%{pypi_name}-doc
Summary:        documentation for python3-%{pypi_name}

%description -n python3-%{pypi_name}-doc
documentation for python3-%{pypi_name}.

%prep
%autosetup -n xet-core-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hf_xet

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc *.md
%license LICENSE

%changelog
* Fri Jan 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
