%undefine dist

Name:           terra-gpg-keys
Version:        %{?fedora:%{fedora}}%{?rhel:%{rhel}}
Release:        6%{?dist}
Summary:        GPG keys for Terra
Requires:       filesystem >= 3.18-6

License:        MIT
URL:            https://terrapkg.com
# We aren't pulling keys from the origin URLs, since they shouldn't change and this is easier to audit.
Source0:        keys.tar.gz
BuildArch:      noarch
Obsoletes:      terra-mock-gpg-keys < %{version}-6

Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
GPG keys for Terra, used for verifying RPM package signatures.

%prep
%autosetup -D -n .

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 ./RPM-GPG-KEY* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%files
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/RPM-GPG-KEY-*
