%global waydroid_commit a33a5c0b31d89d6ce687381104b30aff4dd2d330
%global waydroid_version 1.6.3
%global selinuxtype targeted
%global debug_package %{nil}

Name:           waydroid-nvidia
Version:        0.1.2
%global tag v%{version}

Release:        1%{?dist}
Summary:        Waydroid with NVIDIA GPU acceleration
License:        GPL-3.0-or-later AND MIT
URL:            https://github.com/Shiro836/waydroid-nvidia
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
Source0:        %{url}/archive/refs/tags/%{tag}.tar.gz
Source1:        https://github.com/waydroid/waydroid/archive/%{waydroid_commit}.tar.gz
Source2:        %{url}/releases/download/%{tag}/waydroid-nvidia-host-x86_64-%{tag}.tar.zst
Source3:        %{url}/releases/download/%{tag}/waydroid-nvidia-guest-android-x86_64-%{tag}.tar.zst
Source4:        %{url}/releases/download/%{tag}/waydroid-nvidia-guest-prebuilts-%{tag}.tar.zst
Source5:        waydroid-nvidia.te
Source6:        dev-binderfs.mount
Source7:        waydroid-nvidia.fc

# Assign the Waydroid network interface to the trusted firewalld zone
Patch0:         setup-firewalld.patch
# Mount the Android rootfs with the Waydroid SELinux context
Patch1:         mount-secontext.patch
# Fedora LXC is built without AppArmor support
Patch2:         no-apparmor.patch

ExclusiveArch:  x86_64

BuildRequires:  make
BuildRequires:  tar
BuildRequires:  zstd
BuildRequires:  selinux-policy-devel
BuildRequires:  container-selinux
BuildRequires:  systemd
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       python3dist(gbinder-python) >= 1.3
Requires:       python3dist(dbus-python)
Requires:       python3-gobject
Requires:       lxc
Requires:       gtk3
Requires:       (%{name}-selinux = %{evr} if selinux-policy-%{selinuxtype})
Requires:       nftables
Requires:       iproute
Requires:       dnsmasq
Requires:       binutils
Requires:       libepoxy
Requires:       libdrm
Requires:       mesa-libgbm
Requires:       libX11
Requires:       expat
Requires:       vulkan-loader
Provides:       waydroid = %{waydroid_version}
Conflicts:      waydroid

%description
Waydroid with NVIDIA GPU acceleration through Mesa Venus and a host-side
renderer. This package replaces the stock Waydroid package and requires the
NVIDIA open kernel modules with nvidia-drm.modeset=1.

%package selinux
Summary:        SELinux policy module for Waydroid
Requires:       %{name} = %{evr}
Requires:       container-selinux
%{?selinux_requires}

%description selinux
This package contains the SELinux policy module necessary to run Waydroid.

%prep
%setup -q -n waydroid-nvidia-%{version} -a 1

pushd waydroid-%{waydroid_commit}
patch -p1 < ../patches/waydroid/0001-nvidia-integration.patch
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
popd

mkdir host guest SELinux
tar --zstd -xf %{SOURCE2} -C host
tar --zstd -xf %{SOURCE3} -C guest
tar --zstd -xf %{SOURCE4} -C guest
cp %{SOURCE5} %{SOURCE7} SELinux/
cp waydroid-%{waydroid_commit}/LICENSE LICENSE.waydroid

%build
pushd waydroid-%{waydroid_commit}
# Require users to select OTA channels explicitly.
sed -i -e '/"system_channel":/ s/: ".*"/: ""/' tools/config/__init__.py
sed -i -e '/"vendor_channel":/ s/: ".*"/: ""/' tools/config/__init__.py
sed -i -e '/options: OTA channel URL/ s/default is Official OTA server/mandatory/' tools/helpers/arguments.py
popd

%{__make} -C SELinux NAME=%{selinuxtype} -f /usr/share/selinux/devel/Makefile

%install
%{__make} -C waydroid-%{waydroid_commit} install \
    DESTDIR=%{buildroot} USE_SYSTEMD=1 USE_DBUS_ACTIVATION=1 USE_NFTABLES=1
%py_byte_compile %{python3} %{buildroot}%{_prefix}/lib/waydroid

%{__install} -d %{buildroot}%{_unitdir}
%{__install} -d %{buildroot}%{_datadir}/selinux/%{selinuxtype}
%{__install} -p -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/
%{__install} -p -m 0644 SELinux/waydroid-nvidia.pp \
    %{buildroot}%{_datadir}/selinux/%{selinuxtype}/waydroid-nvidia.pp
sed -i '/^\[Unit\]/a Wants=dev-binderfs.mount' %{buildroot}%{_unitdir}/waydroid-container.service
sed -i '/^\[Service\]/a ExecStartPre=/usr/bin/ln -sf /dev/binderfs/binder /dev/binderfs/vndbinder /dev/binderfs/hwbinder /dev/' %{buildroot}%{_unitdir}/waydroid-container.service

%{__install} -d %{buildroot}%{_prefix}/lib/waydroid-nvidia/guest
%{__install} -p -m 0755 host/virgl_test_server host/virgl_render_server \
    %{buildroot}%{_prefix}/lib/waydroid-nvidia/
%{__install} -p -m 0755 host/libvirglrenderer.so.1 \
    %{buildroot}%{_prefix}/lib/waydroid-nvidia/

for rel in \
    vendor/lib/hw/vulkan.virtio.so \
    vendor/lib/egl/libEGL_angle.so \
    vendor/lib/egl/libGLESv1_CM_angle.so \
    vendor/lib/egl/libGLESv2_angle.so \
    vendor/lib64/hw/vulkan.virtio.so \
    vendor/lib64/egl/libEGL_angle.so \
    vendor/lib64/egl/libGLESv1_CM_angle.so \
    vendor/lib64/egl/libGLESv2_angle.so \
    vendor/lib64/libgbm_mesa_wrapper.so \
    vendor/lib64/hw/hwcomposer.waydroid.so; do
    test -f "guest/$rel"
    %{__install} -D -p -m 0644 "guest/$rel" \
        "%{buildroot}%{_prefix}/lib/waydroid-nvidia/guest/$rel"
done
%{__install} -D -p -m 0755 guest/system/bin/surfaceflinger \
    %{buildroot}%{_prefix}/lib/waydroid-nvidia/guest/system/bin/surfaceflinger

%global integration_dir packaging/aur/waydroid-nvidia-bin
%{__install} -D -p -m 0644 %{integration_dir}/wd-venus.service \
    %{buildroot}%{_userunitdir}/wd-venus.service
%{__install} -D -p -m 0644 %{integration_dir}/waydroid-venus.tmpfiles \
    %{buildroot}%{_tmpfilesdir}/waydroid-venus.conf
%{__install} -D -p -m 0644 %{integration_dir}/waydroid-nvidia.rules \
    %{buildroot}%{_udevrulesdir}/70-waydroid-nvidia.rules
%{__install} -D -p -m 0755 %{integration_dir}/waydroid-nvidia-setup \
    %{buildroot}%{_bindir}/waydroid-nvidia-setup

%check
%desktop_file_validate %{buildroot}%{_datadir}/applications/Waydroid.desktop
%desktop_file_validate %{buildroot}%{_datadir}/applications/waydroid.market.desktop
%desktop_file_validate %{buildroot}%{_datadir}/applications/waydroid.app.install.desktop
appstream-util validate --nonet %{buildroot}%{_metainfodir}/id.waydro.waydroid.metainfo.xml
test -x %{buildroot}%{_prefix}/lib/waydroid-nvidia/virgl_test_server
test -f %{buildroot}%{_prefix}/lib/waydroid-nvidia/guest/vendor/lib/hw/vulkan.virtio.so
test -f %{buildroot}%{_prefix}/lib/waydroid-nvidia/guest/vendor/lib64/hw/vulkan.virtio.so

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/%{selinuxtype}/waydroid-nvidia.pp
%selinux_relabel_post -s %{selinuxtype}
if [ "$1" -le "1" ]; then
    %systemd_postun_with_restart waydroid-container.service
fi

%postun selinux
if [ "$1" -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} waydroid-nvidia
    %selinux_relabel_post -s %{selinuxtype}
fi

%post
waydroid upgrade -o > /dev/null || :
%systemd_post waydroid-container.service
%systemd_user_post wd-venus.service
%tmpfiles_create waydroid-venus.conf
udevadm control --reload > /dev/null 2>&1 || :

%preun
%systemd_preun waydroid-container.service
%systemd_user_preun wd-venus.service

%postun
%systemd_postun_with_restart waydroid-container.service
%systemd_user_postun_with_restart wd-venus.service

%files
%license LICENSE LICENSE.waydroid
%doc README.md docs/
%{_prefix}/lib/waydroid
%{_prefix}/lib/waydroid-nvidia
%{_appsdir}/Waydroid.desktop
%{_appsdir}/waydroid.market.desktop
%{_appsdir}/waydroid.app.install.desktop
%{_metainfodir}/id.waydro.waydroid.metainfo.xml
%{_hicolordir}/512x512/apps/waydroid.png
%{_bindir}/waydroid
%{_bindir}/waydroid-nvidia-setup
%{_unitdir}/waydroid-container.service
%{_userunitdir}/wd-venus.service
%{_unitdir}/dev-binderfs.mount
%{_tmpfilesdir}/waydroid-venus.conf
%{_udevrulesdir}/70-waydroid-nvidia.rules
%{_datadir}/dbus-1/system-services/id.waydro.Container.service
%{_datadir}/dbus-1/system.d/id.waydro.Container.conf
%{_datadir}/polkit-1/actions/id.waydro.Container.policy
%{_datadir}/desktop-directories/waydroid.directory
%{_sysconfdir}/xdg/menus/applications-merged/waydroid.menu

%files selinux
%doc SELinux/waydroid-nvidia.te
%{_datadir}/selinux/%{selinuxtype}/waydroid-nvidia.pp

%changelog
* Sun Sep 13 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.1.2-1
- Package waydroid-nvidia with its pinned Waydroid base and NVIDIA payloads
- Preserve the Fedora patches and Waydroid SELinux policy
