%global commit 8d20a23e38883f45c78f48c8574ac93945b4cb03
%global commitdate 20241224
%global commitdate 20241224
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20241224
%global ver 0.9.7
%global debug_package %{nil}
%global modulename xpadneo

Name:           dkms-%{modulename}
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%?dist
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad
License:        GPL-3.0
URL:            https://atar-axis.github.io/%{modulename}
Source0:        https://github.com/atar-axis/%{modulename}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
Source1:        %{name}.conf
Source2:        no-weak-modules.conf
BuildRequires:  sed
Requires:       bluez
Requires:       bluez-tools
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description
Advanced Linux Driver for Xbox One Wireless Gamepad.

%prep
%autosetup -p1 -n %{modulename}-%{commit}


cp -f %{SOURCE1} hid-xpadneo/src/dkms.conf

sed -i -e 's/__VERSION_STRING/%{version}/g' hid-xpadneo/src/dkms.conf
sed -i -e 's/$(VERSION)/v%{version}/g' hid-xpadneo/src/Makefile

%build

%install
# Create empty tree:
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr hid-xpadneo/src/* %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%if 0%{?fedora}
# Do not enable weak modules support in Fedora (no kABI):
install -Dpm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{modulename} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{modulename}-%{version}
%if 0%{?fedora}
%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%changelog
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
