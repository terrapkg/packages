%define appid org.signal.Signal
%global pnpm_major 11

Name:			signal-desktop
%electronmeta -aD
Version:		8.30.0
Release:		1%{?dist}
Summary:		A private messenger for Windows, macOS, and Linux
URL:			https://signal.org
Source0:		https://github.com/signalapp/Signal-Desktop/archive/refs/tags/v%{version}.tar.gz
Source1:		signal.desktop
Source2:        org.signal.Signal.metainfo.xml
License:		AGPL-3.0-only AND %{electron_license}

BuildRequires:	pulseaudio-libs-devel
BuildRequires:  libX11-devel
BuildRequires:	git-lfs
%if 0%{?fedora} > 45
BuildRequires:	pnpm%{pnpm_major}
%endif
BuildRequires:  python3
BuildRequires:  terra-appstream-helper
BuildRequires:  libxcrypt-compat

Requires:		libwayland-cursor
Requires:		libwayland-client
Requires:		libxkbcommon
Requires:		gdk-pixbuf2
Requires:		libthai
Requires:		nettle
Requires:		avahi-libs
Requires:		libXfixes
Requires:		libjpeg-turbo
Requires:		sqlite-libs
Requires:		json-glib
Requires:		libdatrie
Requires:		libxml2
Requires:		libbrotli
Requires:		cairo
Requires:		xz-libs
Requires:		libxcb
Requires:		nss-util
Requires:		dbus-libs
Requires:		mesa-libgbm
Requires:		at-spi2-atk
Requires:		expat
Requires:		alsa-lib
Requires:       minizip

Provides:       signal
Provides:       Signal
Provides:       Signal-Desktop

Packager:       junefish <june@fyralabs.com>

%description
Signal Desktop links with Signal on Android or iOS and
lets you message from your Windows, macOS, and Linux computers.

%prep
%autosetup -n Signal-Desktop-%{version}
sed -i 's/--config.directories.output=release//g' package.json
sed -i '/"target": "deb",/{N;s/"arch": "x64"/"arch": "%{_electron_cpu}"/}' package.json

%build
%if 0%{?fedora} <= 45 || %{defined rhel}
%vendor_pnpm -v %{pnpm_major}
%endif
export SIGNAL_ENV=production
export SOURCE_DATE_EPOCH="$(date +"%s")"
%pnpm_build -F -r clean-transpile,generate,build:policy-files,generate,build:esbuild:prod
%pnpm_build -F -r build -- --dir sticker-creator

%install
mv ./packages/mute-state-change/LICENSE ./packages/mute-state-change/LICENSE.mute-state-change
mv ./packages/windows-ucv/LICENSE ./packages/windows-ucv/LICENSE.windows-ucv
mv ./packages/types/LICENSE ./packages/types/LICENSE.types
mv ./packages/lame/LICENSE ./packages/lame/LICENSE.lame
mv LICENSE LICENSE.signal-desktop
%electron_install -i signal -l -I build/icons/png

%desktop_file_install %{SOURCE1}

%terra_appstream -o %{SOURCE2}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/signal.desktop

%files
%license LICENSE.signal-desktop
%doc README.md CONTRIBUTING.md ACKNOWLEDGMENTS.md
%license bundled_licenses/*
%{_bindir}/signal-desktop
%{_libdir}/signal-desktop/
%{_appsdir}/signal.desktop
%{_hicolordir}/*x*/apps/signal.png
%{_metainfodir}/org.signal.Signal.metainfo.xml

%changelog
* Thu Oct 08 2026 Owen Zimmerman <owen@fyralabs.com> - 8.30.0-1
- Dep on pnpm11
- Fix arch-specific builds
- Consolidate and clean up build scripts
- Fix license mv lines
- Remove redundant policy files
- Use %%vendor_pnpm for branches without pnpm11

* Thu Jun 25 2026 Owen Zimmerman <owen@fyralabs.com>
- Fix more license name conflicts, remove patch

* Sun Jun 14 2026 june-fish <git@june.fish>
- Fix license name conflicts

* Mon Dec 22 2025 Owen Zimmerman <owen@fyralabs.com>
- Use more electron macros, correct build failures

* Wed Dec 10 2025 Owen Zimmerman <owen@fyralabs.com>
- Add metainfo

* Tue Nov 11 2025 Owen Zimmerman <owen@fyralabs.com>
- Add more Requires:, fix electron_license macro application, fix some formatting

* Fri Aug 8 2025 june-fish <git@june.fish>
- Initial Package
