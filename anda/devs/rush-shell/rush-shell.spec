Name:           rush-shell
Version:        0.1.5
Release:        1%{?dist}
Summary:        Fast terminal shell written in Rust
URL:            https://github.com/isene/rush
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://unlicense.org/UNLICENSE
License:        Unlicense AND (Apache-2.0 OR MIT) AND MIT AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MPL-2.0 AND (Unlicense OR MIT)
BuildRequires:  cargo-rpm-macros

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Fast terminal shell written in Rust. Feature clone
of rsh with 26ms startup, syntax highlighting, tab
completion, nick aliases, and bookmarks.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
install -Dm 755 target/release/rush %{buildroot}%{_bindir}/rush
%{cargo_license_online} > LICENSE.dependencies
cp %{S:1} UNLICENSE

%files
%{_bindir}/rush
%license UNLICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Fri Jul 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
