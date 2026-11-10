%global name RetroDebugger
%global appid com.github.%{name}
%global name_pretty %{name}
%global appstream_component desktop-application
%global developer "Marcin Skoczylas"
# The below is required because %description doesn't provide a macro to infer from
%global _description %{expand:
A visual Debugger/debugging Host for 8 bit systems:<li>C64 (VICE emulation)</li><li>NES ()</li><li>Atari 800</li><li>C64Ultimate</li>}

Name:          %{name}
Version:       1.0.0
Release:       1%{?dist}
Summary:       A visual debugger/debugging host for 8 bit systems.
License:       ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND BSD-2-Clause AND BSL-1.0 AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CC0-1.0 AND ISC AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND (MPL-2.0 OR GPL-3.0-only) AND MPL-2.0+ AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
URL:           https://github.com/slajerek/%{name}

BuildArch:     x86_64
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gtk3-devel
BuildRequires: sdl2-compat-devel
BuildRequires: alsa-lib-devel
BuildRequires: glew-devel
BuildRequires: sndio-devel
BuildRequires: desktop-file-utils
BuildRequires: terra-appstream-helper
Requires:      libGLEW
Requires:      sndio-libs
Requires:      desktop-file-utils
Packager:      Stefan Kaps <st0ff.npl@gmail.com>

%description %_description

# The old SPEC used a special build-project to make the SPECfile-calls much simpler.
# but that is not required, it'd be bloat.
%prep
# INTENAL TESTING SPEEDUP:
# git config --global url."http://192.168.2.192:8080/".insteadOf  "https://github.com/"

# final URL will point to main repository, use the named branch, but tags for versioning.
git clone --depth 1 --recurse-submodules --branch=Terra-linux-deployment https://github.com/St0fF-NPL-ToM/RetroDebugger %name

%build
cd %name && /bin/sh build-linux.sh

%install
install -Dm 755 %name/build/retrodebugger       %{buildroot}%{_bindir}/retrodebugger
install -Dm 644 %name/assets/icons/%{name}.svg  %{buildroot}%{_scalableiconsdir}/%{name}.svg
install -Dm 644 %name/README.md                 %{buildroot}%{_docdir}/retrodebugger/README.md
cp -a           %name/docs                   -t %{buildroot}%{_docdir}/retrodebugger/

%terra_appstream -o %name/assets/%appid.metainfo.xml
%desktop_file_install -k Exec,Icon -v %{_bindir}/retrodebugger,%{_scalableiconsdir}/%{name}.svg -u %f %name/assets/%{appid}.desktop

%files
%{_bindir}/retrodebugger
%{_scalableiconsdir}/%{name}.svg
%{_docdir}/retrodebugger/
%{_metainfodir}/%{appid}.metainfo.xml
%{_appsdir}/%{appid}.desktop

%post
%update_desktop_database

%postun
%update_desktop_database

%changelog
* Sun Nov 01 2026 Stefan Kaps <st0ff.npl@gmail.com> - 1.0.0
- Initial package
