%global ver 2.0.0
%global commit 2e6d0996c1e7f58889b222ae2fdece110b737433
%global commit_date 20240813
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           openbangla-keyboard-nightly
Version:        %ver^%commit_date.%shortcommit
Release:        1%?dist
Summary:        An OpenSource, Unicode compliant Bengali Input Method 
License:        GPL-3.0-or-later
URL:            https://openbangla.github.io/
Source0:        https://github.com/OpenBangla/OpenBangla-Keyboard/archive/%commit.tar.gz
Source1:        https://github.com/OpenBangla/riti/archive/master.tar.gz
BuildRequires:  cmake anda-srpm-macros rust-packaging git-core gcc-c++
BuildRequires:  qt5-qtbase-devel pkgconfig(ibus-1.0) fcitx5-devel pkgconfig(libzstd)
Requires:       qt5-qtbase hicolor-icon-theme zstd
Requires:       openbangla-im = %version-%release
Provides:       openbangla-keyboard = %version-%release
Conflicts:      openbangla-keyboard

%description
OpenBangla Keyboard is an open source, Unicode compliant, Bangla input method for GNU/Linux systems.
It’s a full-fledged Bangla input method with typing automation tools, includes many famous typing
methods such as Avro Phonetic, Probhat, Munir Optima, National (Jatiya) etc.


%package -n ibus-openbangla
Summary:    OpenBangla Keyboard for IBus
Requires:   ibus
Requires:   openbangla-keyboard = %version-%release
Provides:   openbangla-im = %version-%release
Conflicts:  openbangla-im

%description -n ibus-openbangla
OpenBangla Keyboard for IBus.


%package -n fcitx5-openbangla
Summary:    OpenBangla Keyboard for Fcitx5
Requires:   fcitx5
Requires:   openbangla-keyboard = %version-%release
Provides:   openbangla-im = %version-%release
Conflicts:  openbangla-im

%description -n fcitx5-openbangla
OpenBangla Keyboard for Fcitx5.


%prep
%autosetup -n OpenBangla-Keyboard-%commit
rmdir src/engine/riti
tar xf %SOURCE1 -C src/engine/
mv src/engine/riti-master src/engine/riti

%build
if [[ -d build ]]; then rm -rf build; fi
%cmake -DENABLE_FCITX=YES -DENABLE_IBUS=YES
%cmake_build

%install
%cmake_install

%files
%doc README.adoc
%license LICENSE
%_bindir/openbangla-gui
%_datadir/applications/openbangla-keyboard.desktop
%_datadir/icons/hicolor/*/apps/openbangla-keyboard.png
%_datadir/metainfo/io.github.openbangla.keyboard.metainfo.xml
%_datadir/openbangla-keyboard/
%_datadir/pixmaps/openbangla-keyboard.png

%files -n ibus-openbangla
%_libexecdir/ibus-engine-openbangla
%_datadir/ibus/component/openbangla.xml

%files -n fcitx5-openbangla
%_libdir/fcitx5/openbangla.so
%_datadir/fcitx5/addon/openbangla.conf
%_datadir/fcitx5/inputmethod/openbangla.conf


%changelog
%autochangelog
