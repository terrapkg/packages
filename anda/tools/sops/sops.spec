Name:			sops
Version:		3.7.3
Release:		1%?dist
Summary:		Simple and flexible tool for managing secrets
License:		MPL-2.0
URL:			https://github.com/getsops/sops
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildRequires:	go

%description
An editor of encrypted files that supports YAML, JSON, ENV, INI and BINARY
formats and encrypts with AWS KMS, GCP KMS, Azure Key Vault, age, and PGP.

%prep
%autosetup

%build
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n') -s -w" -buildmode=pie -o build/bin/sops ./sops

%install
mkdir -p %buildroot%_bindir
install -pm755 build/bin/sops %buildroot%_bindir/

%files
%doc README.rst
%license LICENSE
%_bindir/sops

%changelog
%autochangelog
