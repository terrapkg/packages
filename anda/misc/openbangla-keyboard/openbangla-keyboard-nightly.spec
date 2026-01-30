%global ver 2.0.0
%global commit bc0772cd6fb341de623d5370c913520c871648b6
%global commit_date 20260119
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
BuildRequires:  qt5-qtbase-devel qt5-qtdeclarative-devel pkgconfig(ibus-1.0) fcitx5-devel pkgconfig(libzstd)
Requires:       qt5-qtbase hicolor-icon-theme zstd
Requires:       openbangla-im = %version-%release
Provides:       openbangla-keyboard = %version-%release
Conflicts:      openbangla-keyboard
Obsoletes:      ibus-openbangla <= 2.0.0^20260113.7c19213
Obsoletes:      fcitx5-openbangla <= 2.0.0^20260113.7c19213

%description
OpenBangla Keyboard is an open source, Unicode compliant, Bangla input method for GNU/Linux systems.
It’s a full-fledged Bangla input method with typing automation tools, includes many famous typing
methods such as Avro Phonetic, Probhat, Munir Optima, National (Jatiya) etc.

%prep
%git_clone https://github.com/OpenBangla/OpenBangla-Keyboard.git %{commit}
%cargo_prep_online

%build
%cmake \
  -DCMAKE_BUILD_TYPE=None \
  -DCMAKE_SKIP_INSTALL_RPATH=YES \
  -DCMAKE_SKIP_RPATH=YES \
  -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_bindir}
ln -sr %{_datadir}/openbangla-gui %{buildroot}%{_bindir}/openbangla-gui
ln -sr %{_datadir}/ibus-openbangla %{buildroot}%{_bindir}/ibus-openbangla

%files
%lang(bn) %doc README.bn.adoc
%lang(en) %doc README.adoc
%license LICENSE
%_bindir/openbangla-gui
%_bindir/ibus-openbangla
%_datadir/applications/openbangla-keyboard.desktop
%_datadir/icons/hicolor/*/apps/openbangla-keyboard.png
%_datadir/metainfo/io.github.openbangla.keyboard.metainfo.xml
%_datadir/openbangla-keyboard/
%_datadir/pixmaps/openbangla-keyboard.png
%_datadir/ibus/component/openbangla.xml


%changelog
%autochangelog
