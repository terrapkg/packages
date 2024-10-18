%global git_commit 0f918015fa418affec32435d1c61c6ae473f2af5
%global git_shortcommit %(c=%{git_commit}; echo ${c:0:7})

Name:           appimagelauncher
Version:        2.2.0
Release:        2%{?dist}
Summary:        Helper application for Linux distributions serving as a kind of "entry point" for running and integrating AppImages

License:        MIT
URL:            https://github.com/TheAssassin/AppImageLauncher
Source0:        %{url}/releases/download/v%{version}/appimagelauncher-%{git_shortcommit}.source.tar.xz
Patch0:         use-fedora-qtlinguist.patch


BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  cairo-devel
BuildRequires:  fuse-devel
BuildRequires:  libarchive-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  qt5-linguist
BuildRequires:  libcurl-devel
BuildRequires:  boost-devel
BuildRequires:  libappimage-devel
BuildRequires:  libappimageupdate-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  librsvg2-devel
BuildRequires:  libqtxdg-devel
BuildRequires:  /usr/bin/ranlib
BuildRequires:  /usr/bin/ar


%description
%{summary}.

%prep
%autosetup -n appimagelauncher-%{git_shortcommit}.source -p1


%build
%cmake \
 -DBUILD_SHARED_LIBS:BOOL=OFF \
 -DUSE_SYSTEM_LIBARCHIVE=ON \
 -DUSE_SYSTEM_LIBCURL=ON \
 -DUSE_SYSTEM_SQUASHFUSE=ON \
 -DUSE_SYSTEM_BOOST=ON \
 -DUSE_SYSTEM_CURL=ON \
 -DUSE_SYSTEM_XDGUTILS=ON \
 -DUSE_SYSTEM_LIBAPPIMAGE=ON \
 -DBUILD_TESTING='OFF' \
 -Wno-dev

make libappimageupdate libappimageupdate-qt
%cmake_build
make


%install
%cmake_install


%post
echo "Installing AppImageLauncher as interpreter for AppImages"
# as there's no _real_ package that we could use as a dependency to take care of the kernel module,
# we need to make sure that the kernel module is loaded manually
modprobe -v binfmt_misc

(set -x; systemctl restart systemd-binfmt)


%postun

echo "Removing AppImageLauncher as interpreter for AppImages"
(set -x; systemctl restart systemd-binfmt)

update_notifier="/usr/share/update-notifier/notify-reboot-required"
if [ -x "$update_notifier" ]; then
    "$update_notifier"
fi

cat <<EOF
#####################################################
#                                                   #
#  NOTE: you need to reboot your computer in order  #
#  to complete the uninstallation                   #
#                                                   #
#  (If you see this message during an upgrade:      #
#  don't worry, you do not have to take any         #
#  action, no reboot required!)                     #
#                                                   #
#####################################################
EOF

%files
%{_datadir}/appimagelauncher
%{_datadir}/applications/appimagelauncher.desktop
%{_datadir}/applications/appimagelaunchersettings.desktop
%{_bindir}/AppImageLauncher
%{_bindir}/AppImageLauncherSettings
%{_bindir}/appimagelauncherd
%{_bindir}/ail-cli
%{_prefix}/lib/binfmt.d/appimage.conf
%{_datadir}/icons/
%{_libdir}/appimagelauncher
%{_userunitdir}/appimagelauncherd.service
%{_datadir}/mime/packages/appimage.xml
%{_mandir}/man1/AppImageLauncher.1.gz

%changelog
* Mon Dec 26 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Bumped release, added missing dependency

* Tue Oct 25 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
