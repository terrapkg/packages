# Generated by rust2rpm 26
%bcond_without check

%global crate bottom

Name:           rust-bottom
Version:        0.10.2
Release:        %autorelease
Summary:        Customizable cross-platform graphical process/system monitor for the terminal

License:        MIT
URL:            https://crates.io/crates/bottom
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          bottom-fix-metadata-auto.diff

BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A customizable cross-platform graphical process/system monitor for the
terminal. Supports Linux, macOS, and Windows.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        MIT
Packager:       Ben Woods <git@ben.woods.am>

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/btm
%{_datadir}/bash-completion/completions/btm
%{_datadir}/fish/vendor_completions.d/btm.fish
%{_datadir}/zsh/site-functions/_btm
%{_mandir}/man1/btm.1*

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
#cargo_build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
# https://github.com/ClementTsang/bottom/blob/main/docs/content/contribution/packaging-and-distribution.md#manpage-and-completion-generation
export BTM_GENERATE=true
%cargo_install
# Completions
install -Dpm 0644 target/tmp/bottom/completion/btm.bash %{buildroot}%{_datadir}/bash-completion/completions/btm
install -Dpm 0644 target/tmp/bottom/completion/btm.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/btm.fish
install -Dpm 0644 target/tmp/bottom/completion/_btm %{buildroot}%{_datadir}/zsh/site-functions/_btm
install -Dpm 0644 target/tmp/bottom/manpage/btm.1 %{buildroot}%{_mandir}/man1/btm.1

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
