%define buildforkernels akmod
%global modulename       logitech-trueforce
# Out-of-tree kmod: no separate debug/debugsource package.
%global debug_package %{nil}

Name:           %{modulename}-kmod
Version:        0.39.2
Release:        1%{?dist}
Summary:        Kernel module for Logitech racing wheels (RS50, G PRO, G923)
License:        GPL-2.0-only
URL:            https://github.com/mescon/logitech-trueforce-linux-driver
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

buildarch:      x86_64
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  kmodtool

Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       gcc
Requires:       make
Requires:       kernel-devel
conflicts:      dkms-%{modulename}

Provides:       logitech-rs50-linux-driver-kmod = 1.0^20260904git.320bf50-100%{?dist}
Provides:       akmod-logitech-rs50-linux-driver = 1.0^20260904git.320bf50-100%{?dist}
Obsoletes:      logitech-rs50-linux-driver-kmod <= 1.0^20260904git.320bf50-1%{?dist}
Obsoletes:      akmod-logitech-rs50-linux-driver <= 1.0^20260904git.320bf50-1%{?dist}


# Two build modes from one spec, selected by whether `kernels` is defined:
#   * kernels defined      -> compile per-kernel kmod-%%{modulename}-<kver>
#     packages for exactly those kernels. This is the toolbox / atomic
#     static-kmod path (see the wiki's Installation page); it needs
#     kernel-devel for each listed kernel but no RPM Fusion buildsys.
#   * kernels NOT defined   -> emit the akmod-%%{modulename} package only. It
#     embeds the SRPM and rebuilds on the user's machine via the akmods
#     service, so it needs no kernel-devel at build time. This is the COPR
#     path: one build serves every kernel the user ever runs.
%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null)}

%description
Out-of-tree kernel module (hid-logitech-dd) for Logitech direct-drive
racing wheels: force feedback, TrueForce texture routing, and G Hub-
equivalent settings via sysfs. Scoped to the direct-drive wheel USB IDs
(RS50 c276, G PRO c272/c268); it coexists with the in-tree
hid-logitech-hidpp, which continues to serve every other Logitech device.

%prep
%setup -q -n logitech-trueforce-linux-driver-%{version}
# One build tree per target kernel (kmodtool convention).
for kver in %{?kernel_versions}; do
    cp -a mainline _kmod_build_${kver%%___*}
    echo "v%{version}" > _kmod_build_${kver%%___*}/.git_hash
done

%build
for kver in %{?kernel_versions}; do
    make -C "${kver##*___}" M="$PWD/_kmod_build_${kver%%___*}" modules
done

%install
for kver in %{?kernel_versions}; do
    install -D -m 0644 _kmod_build_${kver%%___*}/hid-logitech-dd.ko \
        "%{buildroot}%{kmodinstdir_prefix}/${kver%%___*}/%{kmodinstdir_postfix}/hid-logitech-dd.ko"
done
%{?akmod_install}

%changelog
* Wed Sep 2 2026 luan Oliveira <luanv.oliveira@outlook.com> - 0.39.2-1
- ported to terra

* Sun Jul 26 2026 mescon <5875228+mescon@users.noreply.github.com> - 0.20.0-1
- Renamed the settings subpackages: logi-dd -> logi-wheel, logi-dd-gui ->
  logi-wheel-gui ("dd" meant direct-drive, but the app now also covers the
  gear-driven G923). Provides/Obsoletes on the old names move existing
  installs over automatically.

* Sat Jul 18 2026 mescon <5875228+mescon@users.noreply.github.com> - 0.15.0-1
- Ship the userspace ecosystem as layered subpackages: logi-dd (settings
  TUI, logi-ffb DirectInput force-feedback proxy, logi-tf-sim
  simulated-TrueForce daemon, and the TrueForce SDK shim installer;
  requires the driver's -kmod-common, which now carries both udev rules)
  and logi-dd-gui (graphical settings app, GPL-3.0-or-later, with desktop
  entry, icon, and the GUI's windowing/rendering runtime dependencies;
  requires logi-dd). Built from the userspace/logi-dd Rust workspace.

* Thu Jul 09 2026 mescon <5875228+mescon@users.noreply.github.com> - 0.12.1-1
- kmod package for atomic distros (Bazzite/Silverblue/Kinoite). Verified on
  Fedora Silverblue 44: builds in a toolbox, layers with rpm-ostree, and the
  module loads on the running kernel.
