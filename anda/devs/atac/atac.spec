%global crate atac

%if 0%{?fedora} >= 42
%global build_cflags %{__build_flags_lang_c} %{?_distro_extra_cflags} -std=gnu18
%endif
%global __brp_mangle_shebangs %{nil}

Name:           atac
Version:        0.19.0
Release:        1%?dist
Summary:        Arguably a Terminal API Client

License:        MIT
URL:            https://crates.io/crates/atac
Source:         %{crates_source}

Packager:       xiaoshihou <xiaoshihou@tutamail.com>
BuildRequires:  anda-srpm-macros cargo-rpm-macros mold

%global _description %{expand:
Arguably a Terminal API Client. Feature-full, free, open-source, offline
and account-less.}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{crate}


%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install
