# Generated by rust2rpm 24
#bcond_without check

%global crate bandwhich

Name:           rust-bandwhich
Version:        0.21.0
Release:        %autorelease
Summary:        Display current network utilization by process, connection and remote IP/hostname

License:        MIT
URL:            https://crates.io/crates/bandwhich
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          bandwhich-fix-metadata-auto.diff

BuildRequires:  anda-srpm-macros rust-packaging >= 23

%global _description %{expand:
Display current network utilization by process, connection and remote
IP/hostname.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# FIXME: paste output of %%cargo_license_summary here
License:        # FIXME
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.md
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/bandwhich

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
rm %{buildroot}/.cargo -rf

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
