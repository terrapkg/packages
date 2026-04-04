%define debug_package %{nil}

Name:           MareTF
Version:        0.10.2
Release:        1%{?dist}
License:        MIT
Summary:        A utility to create, edit, and display every type of VTF file ever made
URL:            https://github.com/craftablescience/MareTF
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>
Provides:       maretf

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  ninja-build
BuildRequires:  vulkan-headers

%description
%{summary}.

%prep
%git_clone

%conf
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DMARETF_BUILD_INSTALLER=ON \
    -DCPACK_GENERATOR=RPM \
    -DMARETF_BUILD_INSTALLER=ON

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/maretf
%{_bindir}/maretf_gui
%{_appsdir}/maretf.desktop
%{_hicolordir}/512x512/apps/maretf.png
%{_defaultlicensedir}/maretf/LICENSE
%{_datadir}/mime/packages/maretf.xml

%changelog
* Sun Mar 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Build release build

* Sat Mar 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
