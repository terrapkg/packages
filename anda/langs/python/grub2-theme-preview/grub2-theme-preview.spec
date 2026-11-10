%global pypi_name grub2-theme-preview
%global _desc Preview a GRUB 2.x theme using KVM/QEMU.

Name:			python-%{pypi_name}
Version:		2.10.1
Release:		2%{?dist}
Summary:		Preview a GRUB 2.x theme using KVM/QEMU
License:		GPL-2.0-or-later
URL:			https://pypi.org/project/grub2-theme-preview/
Source0:		%{pypi_source grub2_theme_preview}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       qemu-kvm
Requires:       grub2-tools-extra
Requires:       edk2-ovmf
Requires:       mtools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files grub2_theme_preview

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/grub2-theme-preview

%changelog
* Sat Nov 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
