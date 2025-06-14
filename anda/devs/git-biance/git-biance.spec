%global crate git-biance

Name:           git-biance
Version:        0.1.2
Release:        1%?dist
Summary:        Visualize code contributions in a GitHub-style graph.

License:        GPL-3.0
URL:            https://crates.io/crates/git-biance
Source:         %{crates_source}

Packager:       xiaoshihou <xiaoshihou@tutamail.com>
BuildRequires:  anda-srpm-macros cargo-rpm-macros mold

%global _description %{expand:
biance（鞭策，biān cè，spur）is a small rust
program that shows and visualizes code contributions
in a git repository.
}

%description %{_description}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md README-zh.md
%{_bindir}/%{crate}


%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install
