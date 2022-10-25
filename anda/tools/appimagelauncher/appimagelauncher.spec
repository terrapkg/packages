%global git_commit 0f918015fa418affec32435d1c61c6ae473f2af5
%global git_shortcommit %(c=%{git_commit}; echo ${c:0:7})


Name:           appimagelauncher
Version:        2.2.0
Release:        1%{?dist}
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
BuildRequires:  systemd-rpm-macros

%description
%{summary}.

%prep
%autosetup -n appimagelauncher-%{git_shortcommit}.source -p1


%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF \
 -DUSE_SYSTEM_LIBARCHIVE=ON \
 -DUSE_SYSTEM_LIBCURL=ON \
 -DUSE_SYSTEM_SQUASHFUSE=ON \
 -DUSE_SYSTEM_BOOST=ON \
 -DUSE_SYSTEM_CURL=ON \
 -DUSE_SYSTEM_XDGUTILS=OFF \
 -DUSE_SYSTEM_LIBAPPIMAGE=ON

pushd redhat-linux-build
#make libappimageupdate libappimageupdate-qt
popd

%cmake_build


%install
%cmake_install


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
* Tue Oct 25 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
