%global appid dev.khcrysalis.PlumeImpactor
%undefine __brp_mangle_shebangs

Name:           plumeimpactor
Version:        2.6.0
Release:        1%{?dist}
Summary:        Cross-platform & feature rich iOS/iPadOS/tvOS sideloading application
URL:            https://github.com/claration/Impactor
Source0:        %url/archive/refs/tags/v%version.tar.gz
SourceLicense:  MIT AND BSD-3-Clause
License:        MIT AND BSD-3-Clause
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
Requires:       hicolor-icon-theme
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
%dnl install -Dm755 target/rpm/plumesign 					%{buildroot}%{_bindir}/plumesign
install -Dm755 target/rpm/plumeimpactor 				%{buildroot}%{_bindir}/plumeimpactor
install -Dm644 package/linux/%{appid}.desktop 				%{buildroot}%{_appsdir}/%{appid}.desktop
for size in 16 32 48 64 128 256 512; do
	install -Dm644 package/linux/icons/hicolor/${size}x${size}/apps/%{appid}.png %{buildroot}%{_hicolordir}/${size}x${size}/apps/%{appid}.png
done
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md SECURITY.md
%license LICENSE LICENSE_ELLEKIT
%{_bindir}/plumeimpactor
%{_hicolordir}/*x*/apps/%{appid}.png
%{_appsdir}/%{appid}.desktop

%changelog
* Mon Aug 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
