Name:           unl0kr
Version:        2.0.3
Release:        %autorelease
Summary:        Disk unlocker for the initramfs based on LVGL.

License:        GPL-v3.0
URL:            https://gitlab.com/postmarketOS/buffybox

BuildRequires:  pkgconfig(inih) pkgconfig(libinput) pkgconfig(libudev) pkgconfig(xkbcommon) git
Requires:       kernel

%description


%prep
git clone --recursive --shallow-submodules --branch unl0kr-%version %url.git .


%build
%meson/
%meson_build


%install
mv _build/unl0kr %{buildroot}/%{_bindir}/unl0kr
chmod 755 %{buildroot}%{_bindir}/unl0kr


%check


%files
%license    COPYING
%doc        doc/*
%{buildroot}%{_bindir}/unl0kr


%changelog
* Fri Feb 2 2024 infinitebash <infinitebash@fyralabs.com>
%autochangelog
