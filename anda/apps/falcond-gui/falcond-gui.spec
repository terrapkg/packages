Name:           falcond-gui
Version:        1.0.1
Release:        1%{?dist}
Summary:        A GTK4/LibAdwaita application to control and monitor the Falcond gaming optimization daemon
SourceLicense:  MIT
License:        (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND CC0-1.0 AND ISC AND (MIT OR Apache-2.0) AND MIT AND (Unlicense OR MIT)
URL:            https://git.pika-os.com/general-packages/falcond-gui
Source0:        %{url}/archive/v%{version}.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  mold
Requires:       gtk4
Requires:       falcond
Requires:       falcond-profiles
Requires:       libadwaita
Requires(post): gtk-update-icon-cache
Packager:      Gilver E. <roachy@fyralabs.com>

%description
falcond-gui provides a user-friendly graphical interface for managing falcond. It allows users to view the status of the daemon and customize its behavior.

%prep
%autosetup -n %{name}/%{name}
%cargo_prep_online

%build

%install
%cargo_install
desktop-file-install res/%{name}.desktop
install -Dm644 res/falcond.png -t %{buildroot}%{_hicolordir}/512x512/apps/
%{cargo_license_online} > LICENSE.dependencies

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor/ &>/dev/null || :

%files
%doc ../README.md
%license ../LICENSE.md
%{_bindir}/%{name}
%{_hicolordir}/512x512/apps/falcond.png
%{_appsdir}/%{name}.desktop

%changelog
* Thu Jan 1 2026 Gilver E. <roachy@fyralabs.com> - 1.0.0-1
- Initial package
