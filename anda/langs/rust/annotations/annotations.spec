%global crate annotations

Name:		annotations
Version:	0.3.0
Release:	1%{?dist}
Summary:	Minimal terminal tool for annotating code
URL:		https://crates.io/crates/annotations
Source0:	%{terra_crates_source}
SourceLicense:	MIT
License:	(Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND Zlib AND MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later)
BuildSystem:	terra_cargo
BuildRequires:	cargo-rpm-macros
Packager:	Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/annotator

%changelog
* Wed Oct 21 2026 Owen Zimmerman <owen@fyralabs.com> - 0.1.0-1
- Initial commit
