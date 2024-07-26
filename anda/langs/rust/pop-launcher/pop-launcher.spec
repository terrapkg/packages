%global debug_package %{nil}
%define _disable_source_fetch 0
%bcond_without check
%global debug_package %{nil}

%global crate pop-launcher

Name:           %{crate}
Version:        1.2.1
Release:        1%{?dist}
Summary:        Library for writing plugins and frontends for pop-launcher

# Upstream license specification: MPL-2.0
License:        MPL-2.0
URL:            https://github.com/pop-os/launcher/
Source:         https://github.com/pop-os/launcher/archive/refs/tags/%{version}.tar.gz
Patch:          0001-Copy-instead-of-symlink.patch
Patch1:         0001-Remove-frozen-lock.patch

Provides:       rust-%{crate} = 1.2.1

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21
BuildRequires:  external:crate:just
BuildRequires:  anda-srpm-macros


%global _description %{expand:
Library for writing plugins and frontends for pop-launcher.}

%description %{_description}


%prep
%autosetup -n launcher-%{version_no_tilde}
%cargo_prep_online

%build
just

%install
just rootdir=%{buildroot} install
chmod +x %buildroot%_prefix/lib/pop-launcher/scripts/{session,system76-power}/*.sh


%if %{with check}
%check
%cargo_test
%endif


%files
%doc README.md
%license LICENSE
%{_bindir}/pop-launcher
%{_prefix}/lib/pop-launcher/

%changelog
%autochangelog
