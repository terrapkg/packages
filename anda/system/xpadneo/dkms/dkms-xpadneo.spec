%global commit 8d20a23e38883f45c78f48c8574ac93945b4cb03
%global date 20241224
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 0.9.7

%global debug_package %{nil}
%global dkms_name xpadneo

Name:       dkms-%{dkms_name}
Version:    %{ver}^%{date}git.%{shortcommit}
Release:    1%{?dist}
Summary:    Advanced Linux Driver for Xbox One Wireless Gamepad
License:    GPLv3
URL:        https://atar-axis.github.io/%{dkms_name}
BuildArch:  noarch
Source0:    https://github.com/atar-axis/%{dkms_name}/archive/%{commit}.tar.gz#/%{dkms_name}-%{shortcommit}.tar.gz
Source1:    %{name}.conf
BuildRequires:  sed
Provides:   %{dkms_name}-kmod = %{?epoch:%{epoch}:}%{version}
Requires:   %{dkms_name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:   dkms

%description
Advanced Linux Driver for Xbox One Wireless Gamepad.

%prep
%autosetup -p1 -n %{dkms_name}-%{commit}


cp -f %{SOURCE1} hid-xpadneo/src/dkms.conf

sed -i -e 's/__VERSION_STRING/%{version}/g' hid-xpadneo/src/dkms.conf
sed -i -e 's/$(VERSION)/v%{version}/g' hid-xpadneo/src/Makefile

%build

%install
# Create empty tree:
mkdir -p %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
cp -fr hid-xpadneo/src/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

%post
dkms add -m %{dkms_name} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{dkms_name} -v %{version} -q || :
dkms install -m %{dkms_name} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{dkms_name} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{dkms_name}-%{version}

%changelog
%autochangelog
