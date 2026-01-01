Name:          falcond-gui
Version:       1.0.0
Release:       1%{?dist}
Summary:       A GTK4/LibAdwaita application to control and monitor the Falcond gaming optimization daemon
License:       FIXME
URL:           https://git.pika-os.com/general-packages/falcond-gui
Source0:       %{url}/archive/v%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: gtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: mold
Requires:      gtk4
Requires:      falcond
Requires:      falcond-profiles
Requires:      libadwaita
Packager:      Gilver E. <roachy@fyralabs.com>

%description
falcond-gui provides a user-friendly graphical interface for managing falcond. It allows users to view the status of the daemon and customize its behavior.

%prep
%autosetup -n %{name}/%{name}
%cargo_prep_online

%build

%install
%cargo_install
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc ../README.md
%license ../LICENSE.md
%{_bindir}/%{name}

%changelog
* Thu Jan 1 2026 Gilver E. <roachy@fyralabs.com> - 1.0.0-1
- Initial package
