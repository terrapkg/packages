Name:           wluma
Version:        4.10.0
Release:        1%?dist
Summary:        Automatic brightness adjustment based on screen contents and ALS
URL:            https://github.com/max-baz/wluma
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
License:        ISC
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold v4l-utils libv4l-devel rust-libudev-devel vulkan-loader-devel dbus-devel clang
Packager:       Its-J

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install
%cargo_license_summary_online
%{cargo_license_online -a} > LICENSE.dependencies

%files
%doc README.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/wluma

%changelog
* Fri Nov 28 2025 Its-J
- Package wluma
