Name:           xwayland-satellite
Version:        0.5.1
Release:        1%?dist
Summary:        Xwayland outside your Wayland.
License:        MPL-2.0
URL:            https://github.com/supreeeme/xwayland-satellite
Source0:        %url/archive/refs/tags/v%version.tar.gz
BuildRequires:  anda-srpm-macros cargo-rpm-macros mold
BuildRequires:  pkgconfig(xcb)
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  clang-devel

%description
xwayland-satellite grants rootless Xwayland integration to any Wayland
compositor implementing xdg_wm_base. This is particularly useful for
compositors that (understandably) do not want to go through implementing
support for rootless Xwayland themselves.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%files
%doc README.md
%license LICENSE
%_bindir/xwayland-satellite
