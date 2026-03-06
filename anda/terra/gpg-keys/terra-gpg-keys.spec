%undefine dist

Name:           terra-gpg-keys
Version:        %{?fedora:%{fedora}}%{?rhel:%{rhel}}
Release:        2%?dist
Summary:        GPG keys for Terra
Requires:       filesystem >= 3.18-6

License:        MIT
URL:            https://terra.fyralabs.com
# We aren't pulling keys from the origin URLs, since they shouldn't change and this is easier to audit.
Source0:        keys.tar.gz
BuildArch:      noarch

Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
GPG keys for Terra, used for verifying RPM package signatures.

%package -n     terra-mock-gpg-keys
Summary:        Terra GPG keys for Mock

%description -n terra-mock-gpg-keys
Terra GPG key copies for use in Mock.

%prep
%autosetup -D -n .

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 ./RPM-GPG-KEY* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/mock
install -m 644 %{_sourcedir}/RPM-GPG-KEY* $RPM_BUILD_ROOT/etc/pki/mock/

%files
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/RPM-GPG-KEY-*

%files -n terra-mock-gpg-keys
%dir /etc/pki/mock
/etc/pki/mock/RPM-GPG-KEY-*
