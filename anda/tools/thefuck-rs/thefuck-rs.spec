Name:           thefuck-rs
Version:        0.1.0
Release:        1%{?dist}
Summary:        thefuck, written in rust
SourceLicense:  MIT
License:        (Apache-2.0 OR MIT) AND MIT AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MPL-2.0 AND (Unlicense OR MIT)
URL:            https://github.com/dianyo/thefuck-rs
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    terra_cargo
BuildRequires:  cargo-rpm-macros
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A blazingly fast Rust implementation of thefuck,
the magnificent app that corrects your previous console command.

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/thefuck

%changelog
* Sat Oct 24 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.0-1
- Initial commit
