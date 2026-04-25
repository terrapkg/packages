Name:      vapor-mod-overlay
Version:   0.0.1
Release:   1%{?dist}
Summary:   A fairly basic OverlayFS powered mod loader for Steam
License:   MIT
URL:       https://github.com/ChristianSilvermoon/vapor-mod-overlay
Source0:   %{url}/archive/refs/tags/v%{version}.tar.gz
Requires:  bash
Requires:  fuse-overlayfs
BuildArch: noarch
Packager:  Gilver E. <roachy@fyralabs.com>

%description
This is an attempt at a very basic sort of Mod Loader for Valve's Steam Client on GNU/Linux systems that uses OverlayFS.
This was inspired by a bug in Portal 2 VR that required the mod to be disabled temporarily to bypass a crash.

%prep
%autosetup -n %{name}-%{version}

%build
# The voices are getting louder.

%install
install -Dpm755 %{name}.sh %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}

%changelog
* Mon Mar 2 2026 Gilver E. <roachy@fyralabs.com>
- Initial package
