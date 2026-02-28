%define appid org.signal.Signal

Name:			signal-desktop
%electronmeta -aD
Version:		8.0.0
Release:		3%?dist
Summary:		A private messenger for Windows, macOS, and Linux
URL:			https://signal.org
Source0:		https://github.com/signalapp/Signal-Desktop/archive/refs/tags/v%{version}.tar.gz
Source1:		signal.desktop
Source2:        org.signal.Signal.metainfo.xml
License:		AGPL-3.0-only AND %{electron_license}

BuildRequires:	pulseaudio-libs-devel
BuildRequires:  libX11-devel
BuildRequires:	git-lfs
BuildRequires:  anda-srpm-macros
BuildRequires:	pnpm
BuildRequires:  python3
BuildRequires:  terra-appstream-helper
BuildRequires:  nodejs-full-i18n

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
Signal Desktop links with Signal on Android or iOS and lets you message from your Windows, macOS, and Linux computers.

%prep
%autosetup -n Signal-Desktop-%{version}

%build
export SIGNAL_ENV=production
%{__pnpm} install --frozen-lockfile
%{__pnpm} run clean-transpile
pushd sticker-creator
%{__pnpm} install --frozen-lockfile
%{__pnpm} run build
popd
%pnpm_build -r generate,prepare-beta-build

%install
%electron_install -i signal -l -I build/icons/png

%desktop_file_install %{SOURCE1}

for policy in org.signalapp.view-aep.policy org.signalapp.enable-backups.policy; do
install -Dm644 $OUTDIR/resources/$policy %{buildroot}%{_datadir}/polkit-1/rules.d/$policy
rm $OUTDIR/resources/$policy
done

%terra_appstream -o %{SOURCE2}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/signal.desktop

%files
%license LICENSE
%doc README.md CONTRIBUTING.md ACKNOWLEDGMENTS.md
%license bundled_licenses/*
%{_bindir}/signal-desktop
%{_libdir}/signal-desktop/
%{_datadir}/polkit-1/rules.d/org.signalapp.view-aep.policy
%{_datadir}/polkit-1/rules.d/org.signalapp.enable-backups.policy
%{_appsdir}/signal.desktop
%{_hicolordir}/*x*/apps/signal.png
%{_metainfodir}/org.signal.Signal.metainfo.xml

%changelog
* Mon Dec 22 2025 Owen Zimmerman <owen@fyralabs.com>
- Use more electron macros, correct build failures

* Wed Dec 10 2025 Owen Zimmerman <owen@fyralabs.com>
- Add metainfo

* Tue Nov 11 2025 Owen Zimmerman <owen@fyralabs.com>
- Add more Requires:, fix electron_license macro application, fix some formatting

* Fri Aug 8 2025 june-fish <git@june.fish>
- Initial Package
