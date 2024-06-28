%define debug_package %nil
Name:			sops
Version:		3.9.0
Release:		1%?dist
Summary:		Simple and flexible tool for managing secrets
License:		MPL-2.0
URL:			https://github.com/getsops/sops
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildRequires:	go git

%description
An editor of encrypted files that supports YAML, JSON, ENV, INI and BINARY
formats and encrypts with AWS KMS, GCP KMS, Azure Key Vault, age, and PGP.

%prep
%autosetup
go mod download -x

%build
mkdir -p build/bin
go build -ldflags "-s -w" -v -x -buildmode=pie -o build/bin/sops ./cmd/sops

%install
mkdir -p %buildroot%_bindir
install -pm755 build/bin/sops %buildroot%_bindir/

%files
%doc README.rst
%license LICENSE
%_bindir/sops

%changelog
%autochangelog
