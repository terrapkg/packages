# Generated by rust2rpm 23
%bcond_without check

%global crate maturin

Name:           rust-maturin
Version:        0.14.13
Release:        %autorelease
Summary:        Build and publish crates with pyo3, rust-cpython and cffi bindings as well as rust binaries as python packages

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/maturin
Source:         %{crates_source}

BuildRequires:  pkgconfig anda-srpm-macros rust-packaging >= 23

%global _description %{expand:
Build and publish crates with pyo3, rust-cpython and cffi bindings as well as
rust binaries as python packages.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license license-apache
%license license-mit
%doc Changelog.md
%doc Code-of-Conduct.md
%doc README.md
%{_bindir}/maturin

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/license-apache
%license %{crate_instdir}/license-mit
%doc %{crate_instdir}/Changelog.md
%doc %{crate_instdir}/Code-of-Conduct.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bytesize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytesize-devel %{_description}

This package contains library source intended for building other packages which
use the "bytesize" feature of the "%{crate}" crate.

%files       -n %{name}+bytesize-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+configparser-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+configparser-devel %{_description}

This package contains library source intended for building other packages which
use the "configparser" feature of the "%{crate}" crate.

%files       -n %{name}+configparser-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+faster-tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+faster-tests-devel %{_description}

This package contains library source intended for building other packages which
use the "faster-tests" feature of the "%{crate}" crate.

%files       -n %{name}+faster-tests-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+human-panic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+human-panic-devel %{_description}

This package contains library source intended for building other packages which
use the "human-panic" feature of the "%{crate}" crate.

%files       -n %{name}+human-panic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+keyring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+keyring-devel %{_description}

This package contains library source intended for building other packages which
use the "keyring" feature of the "%{crate}" crate.

%files       -n %{name}+keyring-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+multipart-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+multipart-devel %{_description}

This package contains library source intended for building other packages which
use the "multipart" feature of the "%{crate}" crate.

%files       -n %{name}+multipart-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%files       -n %{name}+native-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+native-tls-crate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-crate-devel %{_description}

This package contains library source intended for building other packages which
use the "native-tls-crate" feature of the "%{crate}" crate.

%files       -n %{name}+native-tls-crate-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+password-storage-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+password-storage-devel %{_description}

This package contains library source intended for building other packages which
use the "password-storage" feature of the "%{crate}" crate.

%files       -n %{name}+password-storage-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rpassword-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rpassword-devel %{_description}

This package contains library source intended for building other packages which
use the "rpassword" feature of the "%{crate}" crate.

%files       -n %{name}+rpassword-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tracing-subscriber-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tracing-subscriber-devel %{_description}

This package contains library source intended for building other packages which
use the "tracing-subscriber" feature of the "%{crate}" crate.

%files       -n %{name}+tracing-subscriber-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+upload-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+upload-devel %{_description}

This package contains library source intended for building other packages which
use the "upload" feature of the "%{crate}" crate.

%files       -n %{name}+upload-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ureq-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ureq-devel %{_description}

This package contains library source intended for building other packages which
use the "ureq" feature of the "%{crate}" crate.

%files       -n %{name}+ureq-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
cargo add time -F macros
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
