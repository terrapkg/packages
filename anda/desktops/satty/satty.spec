Name:           satty
Version:        0.20.1
Release:        1%{?dist}
Summary:        Modern screenshot annotation tool
URL:            https://github.com/Satty-org/Satty
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  libadwaita-devel
BuildRequires:  libepoxy-devel
License:        MPL-2.0 AND (MIT OR Apache-2.0) AND Unicode-3.0 AND Apache-2.0 AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR Apache-2.0) AND CC0-1.0 AND (CC0-1.0 OR Apache-2.0) AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
Packager:       Tulip Blossom <tulilirockz@outlook.com>

%description
%{summary}.

%pkg_completion -BNfz

%prep
%autosetup -n Satty-%{version}
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dpm0755 -t %{buildroot}%{_bindir} ./target/rpm/satty 
install -Dpm0644 -t %{buildroot}%{_datadir}/applications/ ./satty.desktop
install -Dpm0644 -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/ ./assets/satty.svg
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d/ ./completions/satty.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions/ ./completions/_satty
install -Dpm0644 ./completions/satty.bash %{buildroot}%{_datadir}/bash-completion/completions/satty
install -Dpm0644 -t %{buildroot}%{_datadir}/nushell/vendor/autoload/ ./completions/satty.nu

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}
%{_datadir}/applications/satty.desktop
%{_datadir}/icons/hicolor/scalable/apps/satty.svg

%changelog
* Sun Mar 29 2026 Tulip Blossom <tulilirockz@outlook.com>
- Initial commit
