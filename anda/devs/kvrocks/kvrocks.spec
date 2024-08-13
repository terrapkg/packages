Name:           kvrocks
Version:        2.9.0
Release:        2%?dist
Summary:        Distributed key value NoSQL database that uses RocksDB
License:        Apache-2.0
URL:            https://kvrocks.apache.org/
Source0:        https://github.com/apache/kvrocks/archive/refs/tags/v%version.tar.gz
Patch0:         0001-Change-path-in-systemd-service-to-use-package-binary.patch
Requires:       openssl
BuildRequires:  autoconf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  openssl-devel
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros

%description
Apache Kvrocks is a distributed key value NoSQL database that uses RocksDB as storage
engine and is compatible with Redis protocol.

%prep
%autosetup -p1

%build
unset LDFLAGS
./x.py build -DPORTABLE=1 -DENABLE_STATIC_LIBSTDCXX=OFF -DENABLE_OPENSSL=ON -DCMAKE_BUILD_TYPE=Release --ghproxy -j $(nproc)

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}

install -pm755 build/%{name} %{buildroot}%{_bindir}/%{name}
install -pm755 build/kvrocks2redis %{buildroot}%{_bindir}/kvrocks2redis

install -pDm640 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -pDm644 utils/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service

%files
%{_bindir}/%{name}
%{_bindir}/kvrocks2redis
%attr(0750, root, root) %dir %{_sysconfdir}/%{name}
%attr(0640, root, root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_unitdir}/%{name}.service
%license LICENSE
%license NOTICE
%license licenses/LICENSE-*


%changelog
%autochangelog
