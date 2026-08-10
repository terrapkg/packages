Name:           sniffnet
Version:        1.5.1
Release:        1%{?dist}
Summary:        Comfortably monitor your Internet traffic
URL:            https://github.com/GyulyVGC/sniffnet
Source0:        %url/archive/refs/tags/v%version.tar.gz
SourceLicense:  MIT AND Apache-2.0
License:        MIT AND Apache-2.0
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(alsa)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/sniffnet                        %{buildroot}%{_bindir}/sniffnet
install -Dm644 resources/logos/raw/icon.png               %{buildroot}%{_hicolordir}/1024x1024/apps/sniffnet.png
install -Dm644 resources/logos/raw/icon.svg               %{buildroot}%{_scalableiconsdir}/sniffnet.svg
install -Dm644 resources/packaging/linux/sniffnet.desktop %{buildroot}%{_appsdir}/sniffnet.desktop

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE-MIT LICENSE-APACHE
%license LICENSE.dependencies
%{_bindir}/sniffnet
%{_hicolordir}/1024x1024/apps/sniffnet.png
%{_scalableiconsdir}/sniffnet.svg
%{_appsdir}/sniffnet.desktop

%changelog
* Sun Aug 09 2026 Owen Zimmerman <owen@fyralabs.com> - 1.5.1-1
- Initial commit
