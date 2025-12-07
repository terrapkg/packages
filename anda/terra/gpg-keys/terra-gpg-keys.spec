Name:           terra-gpg-keys
Version:        1
Release:        1
Summary:        GPG keys for Terra
Requires:       filesystem >= 3.18-6

License:        MIT
URL:            https://terra.fyralabs.com
# We aren't pulling keys from the origin URLs, since they shouldn't change and this is easier to audit.
Source0:        RPM-GPG-KEY-terrarawhide.asc
Source1:        RPM-GPG-KEY-terra43.asc
Source2:        RPM-GPG-KEY-terra42.asc
BuildArch:      noarch

%description
GPG keys for Terra, used for verifying RPM package signatures.

%prep

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 %{_sourcedir}/RPM-GPG-KEY* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%files
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/RPM-GPG-KEY-*
