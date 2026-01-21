%global crate tauri-cli
%undefine __brp_mangle_shebangs

Name:           rust-tauri
Version:        2.9.6
Release:        4%{?dist}
Summary:        Command line interface for building Tauri apps
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/create-tauri-app
Source:         %{crates_source}
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  mold
Suggests:       libayatana-appindicator-gtk3
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Build smaller, faster, and more secure desktop and mobile applications with a web frontend.

%package -n    tauri
Summary:       %{summary}
License:       ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSL-1.0 AND BlueOak-1.0.0 AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND ISC AND MIT AND (MIT AND (MIT OR Apache-2.0)) AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR NCSA) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MIT-0 AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)

%description -n tauri
Build smaller, faster, and more secure desktop and mobile applications with a web frontend.

%pkg_completion -n tauri -fz

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
%cargo_build

%install
install -Dpm755 target/rpm/cargo-tauri %{buildroot}%{_bindir}/tauri
%{cargo_license_online} > LICENSE.dependencies
mkdir -p %{buildroot}{%{bash_completions_dir},%{fish_completions_dir},%{zsh_completions_dir}}

#target/rpm/cargo-tauri completions --shell bash --output %{buildroot}%{bash_completions_dir}/tauri || :
target/rpm/cargo-tauri completions --shell fish --output %{buildroot}%{fish_completions_dir}/tauri.fish
target/rpm/cargo-tauri completions --shell zsh --output %{buildroot}%{zsh_completions_dir}/_tauri

%files -n tauri
%license LICENSE_APACHE-2.0
%license LICENSE_MIT
%license LICENSE.dependencies
%doc README.md
%{_bindir}/tauri

%changelog
* Thu Jan 1 2026 <rockgrub@disroot.org> - 4.6.2-3
- Added shell completion subpackages
* Thu Dec 25 2025 Gilver E. <rockgrub@disroot.org> - 4.6.2-1
- Initial package
