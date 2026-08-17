%global appid com.github.craftablescience.VPKEdit
%global _distro_extra_ldflags -fuse-ld=mold

Name:           vpkedit
Version:        5.0.0.4
Release:        2%?dist
Summary:        A CLI/GUI tool to create, read, and write several pack file formats
License:        MIT
URL:            https://github.com/craftablescience/VPKEdit
Requires:       qt6-qtbase hicolor-icon-theme
Suggests:       qt6-qtwayland
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  cmake git-core gcc gcc-c++ binutils mold
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
ExclusiveArch:  x86_64

%description
VPKEdit is an open source MIT-licensed tool that can extract from, preview the
contents of and write to several pack file formats. It also supports creating
new VPKs.


%prep
%git_clone %url v%version


%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF          \
   -DCMAKE_BUILD_TYPE=Release                \
   -DCPACK_GENERATOR=RPM                     \
   -DVPKEDIT_USE_LTO=ON
%cmake_build


%install
%cmake_install
pushd %buildroot%_libdir/%name
rm -rf {libQt*,*.md,LICENSE}
popd
mkdir -p %buildroot%_bindir
#ln -sf %_libdir/vpkedit/vpkedit %buildroot%_bindir/vpkedit
#ln -sf %_libdir/vpkedit/vpkeditcli %buildroot%_bindir/vpkeditcli
desktop-file-edit --set-key=Exec --set-value=%_bindir/vpkedit %buildroot%_datadir/applications/vpkedit.desktop
%terra_appstream

%check
desktop-file-validate %buildroot%_appsdir/%name.desktop


%files
%doc README.md CODE_OF_CONDUCT.md INSTALL.md CREDITS.md
%license LICENSE CREDITS.md
%_bindir/vpkedit
%_bindir/vpkeditcli
%_libdir/%name/
%_datadir/applications/vpkedit.desktop
%_hicolordir/*x*/apps/vpkedit.png
%_datadir/mime/packages/vpkedit.xml
%_metainfodir/%appid.metainfo.xml
