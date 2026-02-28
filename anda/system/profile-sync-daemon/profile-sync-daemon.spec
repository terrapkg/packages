%undefine __brp_add_determinism
# disable debuginfo subpackage
%global debug_package %{nil}
# don't strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%global __strip /bin/true

Name:           profile-sync-daemon
Version:        6.55
Release:        1%?dist
Summary:        Symlinks and syncs browser profile dirs to RAM thus reducing HDD/SDD calls and speeding-up browsers
URL:            https://github.com/graysky2/profile-sync-daemon
License:        MIT
Packager:       veuxit <erroor234@gmail.com>

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  bash coreutils findutils fuse-overlayfs glib2 kmod rsync systemd make cmake
Requires:       bash coreutils findutils fuse-overlayfs glib2 kmod rsync systemd

%description
Profile-sync-daemon (psd) is a tiny pseudo-daemon designed to manage your browser's
 profile in tmpfs and to periodically sync it back to your physical disc (HDD/SSD). 
This is accomplished via a symlinking step and an innovative use of rsync to
 maintain back-up and synchronization between the two. 
One of the major design goals of psd is a completely transparent user experience.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build

%install
%make_install

%files
%{_bindir}/profile-sync-daemon
%{_bindir}/psd-suspend-sync
%{_bindir}/psd
%{_datadir}/zsh/site-functions/_psd
%{_datadir}/psd/browsers
%{_datadir}/psd/psd.conf
%{_datadir}/psd/contrib
%{_userunitdir}/psd.service
%{_userunitdir}/psd-resync.service
%{_userunitdir}/psd-resync.timer
%{_mandir}/man1/profile-sync-daemon.1.gz
%{_mandir}/man1/psd.1.gz
%{_bindir}/psd-overlay-helper
%{_datadir}/man/man1/psd-overlay-helper.1.gz


%changelog
* Sat Feb 28 2026 veux <erroor234@gmail.com> - 6.55
- Initial package release