Name:           vpkedit
Version:        4.2.0
Release:        1%?dist
Summary:        A CLI/GUI tool to create, read, and write several pack file formats
License:        MIT
URL:            https://github.com/craftablescience/VPKEdit
Requires:       qt6-qtbase hicolor-icon-theme
Suggests:       qt6-qtwayland
BuildRequires:  cmake git-core gcc gcc-c++ binutils
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6LinguistTools)

%description
VPKEdit is an open source MIT-licensed tool that can extract from, preview the
contents of and write to several pack file formats. It also supports creating
new VPKs.


%package -n libvpkeditc
Summary: A library to create, read, and write several pack file formats

%description -n libvpkeditc
VPKEdit is an open source MIT-licensed tool that can extract from, preview the
contents of and write to several pack file formats. It also supports creating
new VPKs.


%prep
git clone %url . --depth 1 --recursive --branch v%version
git checkout v%version


%build
%cmake -DVPKEDIT_BUILD_LIBC=ON
%cmake_build


%install
%cmake_install
ls %buildroot/usr/**
ln -sf %_libdir/vpkedit/vpkedit %buildroot%_bindir/vpkedit
ln -sf %_libdir/vpkedit/vpkeditcli %buildroot%_bindir/vpkeditcli
sed -i 's@Exec=/opt/vpkedit/@Exec=@g' %buildroot%_datadir/applications/vpkedit.desktop
install -Dpm755 include/vpkeditc %buildroot%_includedir/vpkeditc


%files
%doc README.md
%license LICENSE
%_bindir/vpkedit
%_bindir/vpkeditcli
%_datadir/applications/vpkedit.desktop

%files -n libvpkeditc
%doc README.md
%license LICENSE
%_includedir/vpkeditc
%_libdir/libvpkeditc.so

%changelog
%autochangelog
