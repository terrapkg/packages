%undefine __brp_mangle_shebangs

Name:           chdig
Version:        26.2.3
Release:        1%?dist
Summary:        Dig into ClickHouse with TUI interface
URL:            https://github.com/azat/chdig
Source0:        %url/archive/refs/tags/v%{version}.tar.gz
License:        MIT
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold clang fontconfig-devel glib2 libgcc

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/chdig %{buildroot}%{_bindir}/chdig
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/chdig

%changelog
* Fri Nov 14 2025 Owen Zimmerman <owen@fyralabs.com>
- Intial Commit
