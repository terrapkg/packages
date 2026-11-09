%global name RetroDebugger
%global appid com.github.%{name}
%global name_pretty %{name}
%global appstream_component desktop-application
%global developer "Marcin Skoczylas"
# The below is required because %description doesn't provide a macro to infer from
%global _description %{expand:
A visual Debugger/debugging Host for 8 bit systems:<li>C64 (VICE emulation)</li><li>NES ()</li><li>Atari 800</li><li>C64Ultimate</li>}

Name:          %{name}
Version:       0.0.1
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
BuildRequires: terra-appstream-helper
BuildRequires: glibc-2.43
Requires:      glibc-2.43
Requires:      libGLEW
Requires:      sndio-libs
Packager:      Stefan Kaps <st0ff.npl@gmail.com>

%description %_description

# The old SPEC used a special build-project to make the SPECfile-calls much simpler.
# but that is not required, it'd be bloat.
%prep
%git_clone --branch=Terra-linux-deployment https://github.com/St0fF-NPL-ToM/RetroDebugger %name

%build
cd %name && /bin/sh build-linux.sh

%install
install -Dm 755 target/rpm/rush %{buildroot}%{_bindir}/rush

install -Dm644 extra/desktop/tracy.desktop %buildroot%_datadir/applications/tracy.desktop
install -Dm644 icon/icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/tracy.svg
install -Dm644 extra/desktop/application-tracy.xml %buildroot%_datadir/mime/packages/application-tracy.xml
install -Dm644 icon/application-tracy.svg %buildroot%_iconsdir/hicolor/scalable/apps/application-tracy.svg

%terra_appstream -o RetroDebugger/assets/%appid.metainfo.xml
%__desktop_file_edit retrodebugger/assets/%appid.desktop \
    --set-key=Exec --set-value=%{_bindir}/retrodebugger \
    --set-key=Type --set-value=Application \
    --set-icon=RetroDebugger

%files
%{_bindir}/retrodebugger
%{_docdir}/retrodebugger/README.md
%{_docdir}/retrodebugger/docs/
%{_scalableiconsdir}/%{name}.svg
%{_metainfodir}/%{appid}.metainfo.xml
%{_appsdir}/%{name}.desktop

%changelog
* Sun Nov 01 2026 Stefan Kaps <st0ff.npl@gmail.com> - 1.0.0
- Initial package
