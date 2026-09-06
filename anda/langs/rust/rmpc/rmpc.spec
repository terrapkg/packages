%undefine __brp_mangle_shebangs

Name:           rmpc
Version:        0.11.0
Release:        1%?dist
Summary:        A modern, configurable, terminal based MPD Client with album art support via various terminal image protocols
URL:            https://rmpc.mierak.dev/
Source0:        https://github.com/mierak/rmpc/archive/refs/tags/v%version.tar.gz
License:        BSD-3-Clause
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Rmpc is a beautiful, modern and configurable terminal based Music Player Daemon client.
It is heavily inspired by ncmpcpp and ranger/lf file managers.

%pkg_completion -bfz

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
install -Dm755 target/rpm/%{name}                %{buildroot}%{_bindir}/%{name}
install -Dm644 target/completions/%{name}.bash   %{buildroot}%{bash_completions_dir}/
install -Dm644 target/completions/%{name}.fish   %{buildroot}%{fish_completions_dir}/
install -Dm644 target/completions/_%{name}       %{buildroot}%{zsh_completions_dir}/
install -Dm644 target/man/rmpc.1                 %{buildroot}%{_mandir}/man1/rmpc.1
%{cargo_license_online} > LICENSE.dependencies

%files
%license LICENSE LICENSE.dependencies
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_mandir}/man1/rmpc.*.*

%changelog
* Sat Dec 27 2025 Owen Zimmerman <owen@fyralabs.com> - 0.1.65-1
- Initial commit
