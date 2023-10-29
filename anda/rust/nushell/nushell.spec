Name:			nushell
Version:		0.86.0
Release:		1%{?dist}
Summary:		A new type of shell
License:		MIT
URL:			https://www.nushell.sh/
Source0:		https://github.com/nushell/nushell/archive/refs/tags/%version.tar.gz
BuildRequires:	anda-srpm-macros rust-packaging openssl-devel
Requires:		glibc gcc-libs openssl zlib

%description
%summary.

%prep
%autosetup
%cargo_prep_online

%build
%{cargo_build -f extra,dataframe} --workspace

%install
find target/release -maxdepth 1 -executable -type f -name "nu*" -exec install -vDm755 -t %buildroot%_bindir "{}" +

%files
%doc README.md
%license LICENSE
%_bindir/nu*

%changelog
%autochangelog
