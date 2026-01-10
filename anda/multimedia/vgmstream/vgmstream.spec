%global commit      3d145c46ae32409594fa561967bbe0f7cb027482
%global shortcommit %{sub %{commit} 1 7}
%global commit_date 20260110

Name:			vgmstream
Version:		0~%{commit_date}git.%shortcommit
Release:		1%?dist
Summary:		A library for playback of various streamed audio formats used in video games
License:		ISC
URL:			https://vgmstream.org
Packager:		madonuko <mado@fyralabs.com>
Source0:		https://github.com/vgmstream/vgmstream/archive/%commit.tar.gz
# https://github.com/vgmstream/vgmstream/blob/master/make-build-cmake.sh
BuildRequires:	gcc gcc-c++ cmake git-core
BuildRequires:	pkgconfig(libmpg123) pkgconfig(vorbis) pkgconfig(speex)
BuildRequires:	pkgconfig(libavformat) pkgconfig(libavcodec) pkgconfig(libavutil) pkgconfig(libswresample)
BuildRequires:	yasm pkgconfig(opus) pkgconfig(ao) pkgconfig(audacious)

%description
%summary.

%package devel
%pkg_devel_files
%license COPYING
%_libdir/cmake/vgmstream

%package -n audacious-plugins-vgmstream
Summary:		Audacious input plugin for vgmstream
Supplements:	(vgmstream and audacious)
%description -n audacious-plugins-vgmstream
Audacious input plugin for vgmstream.
For more information, see the main vgmstream package.

%files -n audacious-plugins-vgmstream
%license COPYING
%_libdir/audacious/Input/vgmstream.so

%prep
%autosetup -n %name-%commit

sed 's/VERSION=""/VERSION="%shortcommit"/g' -i version-make.sh

%build
# https://github.com/vgmstream/vgmstream/issues/1780
%cmake -DCMAKE_BUILD_TYPE=Release -DUSE_G719=0 %["%_arch" == "x86_64" ? "" : "-DUSE_CELT=0"]
%cmake_build

%install
%cmake_install

%files
%doc README.md SECURITY.md doc/*.md
%license COPYING
%_bindir/vgmstream-cli
%_bindir/vgmstream123
