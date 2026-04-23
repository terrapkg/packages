%undefine __brp_mangle_shebangs

Name:           framework-tool-tui
Version:        0.8.3
Release:        1%{?dist}
Summary:        A TUI for controlling and monitoring Framework Computers hardware built in Rust
URL:            https://github.com/grouzen/framework-tool-tui
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
License:        MIT
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libudev)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A snappy TUI dashboard for controlling and monitoring your Framework Laptop
hardware — charging, privacy, lighting, USB PD ports, and more.

%package doc
Summary:	Documentations for %{name}
BuildArch:	noarch

%description doc
Documentations for %{name}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/framework-tool-tui %{buildroot}%{_bindir}/framework-tool-tui
%{cargo_license_online} > LICENSE.dependencies

mkdir -p %{buildroot}%{_docdir}/%{name}/
cp -r docs/*.md %{buildroot}%{_docdir}/%{name}/

%files
%{_bindir}/framework-tool-tui
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%files doc
%{_docdir}/%{name}/

%changelog
* Thu Apr 23 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
