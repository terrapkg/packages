Name:           juce
Version:        8.0.12
Release:        3%{?dist}
License:        AGPL-3.0
Summary:        framework for audio application and plug-in development
URL:            https://juce.com
Source:         https://github.com/juce-framework/JUCE/archive/refs/tags/%{version}.tar.gz
Patch0:         fix-install-dirs.patch
Packager:       metcya <metcya@gmail.com>

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  webkit2gtk4.1-devel

# for building docs
BuildRequires:  doxygen
BuildRequires:  python3
BuildRequires:  graphviz

%description
JUCE is an open-source cross-platform C++ application framework for creating
desktop and mobile applications, including VST, VST3, AU, AUv3, AAX and LV2
audio plug-ins and plug-in hosts. JUCE can be easily integrated with existing
projects via CMake, or can be used as a project generation tool via the
Projucer, which supports exporting projects for Xcode (macOS and iOS), Visual
Studio, Android Studio, and Linux Makefiles as well as containing a source code
editor.

%package doc
Summary:        Documentation files for %{name}

%description doc
Documentation files for %{name}

%prep
%autosetup -p1 -n JUCE-%{version}

%build
%cmake -DJUCER_ENABLE_GPL_MODE=1    \
       -DJUCE_BUILD_EXTRAS=ON       \
       -DJUCE_TOOL_INSTALL_DIR=bin
%cmake_build

pushd docs/doxygen
python3 build.py
popd

%install
%cmake_install

pushd docs/doxygen/doc
find -type f -exec install -Dm 644 '{}' -t %{buildroot}%{_pkgdocdir} \;
popd

%files
%doc README.md CODE_OF_CONDUCT.md CHANGE_LIST.md BREAKING_CHANGES.md
%license LICENSE.md
%{_bindir}/juceaide
%{_bindir}/juce_lv2_helper
%{_libdir}/cmake/%{name}/*
%{_datadir}/%{name}/modules/*

%files doc
%license LICENSE.md
%doc %{_pkgdocdir}/*

%changelog
* Tue Dec 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Install doc subpackage license

* Fri Dec 19 2025 metcya <metcya@gmail.com> - 8.0.12
- Package juce
