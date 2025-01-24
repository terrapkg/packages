%global debug_package %{nil}
%define _disable_source_fetch 0
%bcond_without check
%global debug_package %{nil}

%global crate pop-launcher

Name:           %{crate}
Version:        1.2.4
Release:        1%?dist
Summary:        Library for writing plugins and frontends for pop-launcher

# Upstream license specification: MPL-2.0
License:        MPL-2.0
URL:            https://github.com/pop-os/launcher/
Source:         %{url}/archive/refs/tags/%{version}.tar.gz
Patch:          0001-Copy-instead-of-symlink.patch

Provides:       rust-%{crate} = 1.2.4

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21
BuildRequires:  just
BuildRequires:  anda-srpm-macros
BuildRequires:  fdupes
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  mold

Requires:       (gnome-shell-extension-pop-shell or cosmic-launcher)

%global _description %{expand:
Library for writing plugins and frontends for pop-launcher.}

%description %{_description}


%prep
%autosetup -n launcher-%{version_no_tilde}
%cargo_prep_online

%build
%set_build_flags
just build-release

%install
just rootdir=%{buildroot} install
chmod +x %buildroot%_prefix/lib/pop-launcher/scripts/{session,system76-power}/*.sh

%fdupes %buildroot%_prefix/

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
