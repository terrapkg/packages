%define _unpackaged_files_terminate_build 0

Name:           vpkedit
Version:        5.0.0.4
Release:        1%?dist
Summary:        A CLI/GUI tool to create, read, and write several pack file formats
License:        MIT
URL:            https://github.com/craftablescience/VPKEdit
Requires:       qt6-qtbase hicolor-icon-theme
Suggests:       qt6-qtwayland
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  cmake git-core gcc gcc-c++ binutils
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6LinguistTools)
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
   -DCPACK_GENERATOR=RPM
#   -DVPKEDIT_BUILD_LIBC=ON
%cmake_build


%install
%cmake_install
pushd %buildroot%_libdir/%name
rm -rf {libQt*,*.md,LICENSE}
popd
mkdir -p %buildroot%_bindir
ln -sf %_libdir/vpkedit/vpkedit %buildroot%_bindir/vpkedit
ln -sf %_libdir/vpkedit/vpkeditcli %buildroot%_bindir/vpkeditcli
sed -i 's@Exec=/opt/vpkedit/@Exec=@g' %buildroot%_datadir/applications/vpkedit.desktop


%files
%doc README.md CODE_OF_CONDUCT.md INSTALL.md CREDITS.md
%license LICENSE
%_bindir/vpkedit
%_bindir/vpkeditcli
%_libdir/%name/
%_datadir/applications/vpkedit.desktop
%_hicolordir/*x*/apps/vpkedit.png
%_datadir/mime/packages/vpkedit.xml
