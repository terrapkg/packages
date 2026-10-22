%global commit d890a93105a0aa52028ac49282fa1b579e12566e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260826
%global ver 0.83

# Pinned to the hid-tminit submodule commit of the hid-tmff2 commit above
%global tminit_commit 8c4547288a6c182ed4ff131e36f710f11a76c4a9
%global tminit_shortcommit %(c=%{tminit_commit}; echo ${c:0:7})

%global debug_package %{nil}
%global modulename hid-tmff2

Name:           dkms-%{modulename}
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        3%{?dist}
Summary:        Thrustmaster Force Feedback kernel module (DKMS)
License:        GPL-2.0-only
URL:            https://github.com/Kimplul/%{modulename}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
Source1:        https://github.com/Kimplul/hid-tminit/archive/%{tminit_commit}.tar.gz#/hid-tminit-%{tminit_shortcommit}.tar.gz
Source2:        %{name}.conf
Source3:        no-weak-modules.conf
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}
Provides:       %{modulename}-kmod
BuildArch:      noarch

%description
Linux kernel module for Thrustmaster T300RS, T248 and (experimental) TX, T128,
T598, T-GT II and TS-XW wheels.

%prep
%autosetup -p1 -n %{modulename}-%{commit}

# Pull in the hid-tminit submodule sources. It builds hid-tminit-new and
# usb-tminit-new, required to switch wheels that enumerate as a generic
# "Thrustmaster FFB Wheel" (e.g. T128 Xbox version) into PC mode.
rm -rf deps/hid-tminit
mkdir -p deps/hid-tminit
tar -xf %{SOURCE1} -C deps/hid-tminit --strip-components=1

cp -f %{SOURCE2} dkms/dkms.conf
sed -i -e 's/__VERSION_STRING/%{version}/g' dkms/dkms.conf

%build

%install
# Create empty tree:
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr Kbuild Makefile src deps %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
install -Dpm644 dkms/dkms.conf %{buildroot}%{_usrsrc}/%{modulename}-%{version}/dkms.conf

%if 0%{?fedora}
# Do not enable weak modules support in Fedora (no kABI):
install -Dpm644 %{SOURCE3} %{buildroot}%{_sysconfdir}/dkms/%{modulename}.conf
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
* Tue Oct 20 2026 Potajito <potajito@gmail.com> - 0.83^20260826git.d890a93-3
- Build and ship hid-tminit-new and usb-tminit-new from the hid-tminit
- dependency (required for wheels needing mode switching, e.g. T128X)
- https://github.com/ublue-os/bazzite/issues/3555

* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
