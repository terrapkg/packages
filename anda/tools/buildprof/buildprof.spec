Name:           buildprof
Version:        0.2.7
Release:        1%{?dist}
Summary:        Records every process and file access in a build and shows it as an interactive timeline
URL:            https://buildprof.lalitm.com
Source0:        https://github.com/LalitMaganti/%{name}/archive/refs/tags/v%{version}.tar.gz
License:        (Apache-2.0 OR MIT) AND MIT AND Apache-2.0 AND (Unlicense OR MIT)
BuildRequires:  cargo rust-srpm-macros anda-srpm-macros cargo-rpm-macros

Packager:       julian45 <julian@julian45.net>

%description
Buildprof records every process a build starts and every file it opens, and
turns the recording into an interactive timeline in the browser. It works below
any build system: Make, Ninja, CMake, Meson, Cargo, Go, and wrapper scripts.

%prep
%autosetup -n %name-%version
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online

%install
install -Dm755 target/rpm/buildprof %{buildroot}%{_bindir}/buildprof
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/buildprof

%changelog
* Sat Sep 19 2026 julian45 <julian@julian45.net>
- Initial package
