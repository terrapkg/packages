# Prebuilt upstream bundle, there are no sources to extract debuginfo from.
%define debug_package %nil

%ifarch x86_64
%global a x86-64
%elifarch aarch64
%global a arm-64
%endif

%global appid               org.localsend.localsend_app
%global name_pretty         LocalSend
%global appstream_component desktop-application
%global developer           Tien Do Nam
# The Flutter bundle links its plugins with an $ORIGIN/lib rpath, so the whole
# tree has to stay together next to the executable.
%global bundledir           %{_libdir}/localsend

# The bundled Flutter engine and plugins are private to this package. Without
# this they would export sonames as generic as libapp.so into the global
# namespace, colliding with any other Flutter application packaged this way,
# and depend on themselves. Requires are filtered by soname rather than by path
# so that genuine external dependencies of those same libraries -- GTK, epoxy,
# libayatana-appindicator -- are still picked up.
%global __provides_exclude_from ^%{bundledir}/lib/.*$
%global __requires_exclude ^(libapp|librhttp|libflutter_linux_gtk|lib.*_plugin)\\.so.*$

Name:           localsend-bin
Version:        1.18.2
Release:        1%{?dist}
Summary:        An open source cross-platform alternative to AirDrop
URL:            https://localsend.org
Source0:        https://github.com/localsend/localsend/releases/download/v%{version}/LocalSend-%{version}-linux-%{a}.tar.gz
Source1:        localsend.desktop
# The release tarball ships no licence text.
Source2:        https://raw.githubusercontent.com/localsend/localsend/v%{version}/LICENSE

# app/linux/packaging/rpm/make_config.yaml claims MIT, but the LICENSE file in
# the repository is Apache-2.0. Going with the actual licence text.
License:        Apache-2.0

# Upstream publishes Linux bundles for these two only.
ExclusiveArch:  x86_64 aarch64

BuildRequires:  desktop-file-utils
BuildRequires:  patchelf
BuildRequires:  anda-srpm-macros
BuildRequires:  terra-appstream-helper

Requires:       libayatana-appindicator-gtk3
Requires:       xdg-user-dirs

Provides:       localsend = %{version}-%{release}

Packager:       NichSchlagen <tim-rosenhagen@web.de>

%description
LocalSend lets you share files and messages with nearby devices over your local
network, without an internet connection and without a third-party server. It
speaks a common protocol across Linux, Windows, macOS, Android and iOS.

This package repackages the official upstream build. LocalSend %{version} pins
wechat_assets_picker and yaru to versions that predate Flutter's Material theme
migration, so it cannot currently be built from source against the Flutter in
Terra.

%prep
# The tarball has no top level directory of its own.
%autosetup -c -n localsend-%{version}
cp -p %{SOURCE2} LICENSE

%install
install -dm755 %{buildroot}%{bundledir}
cp -a data lib localsend_app %{buildroot}%{bundledir}/

# Upstream's CI leaks its own build directory into the plugin RUNPATHs
# ("/home/runner/work/localsend/...", plus a Debian multiarch path). rpm's
# check-rpaths rejects that, rightly. The plugins only need libflutter_linux_gtk
# .so, which sits beside them and already carries $ORIGIN itself.
for so in %{buildroot}%{bundledir}/lib/*.so; do
    case "$(patchelf --print-rpath "$so")" in
        ''|'$ORIGIN') ;;
        *) patchelf --set-rpath '$ORIGIN' "$so" ;;
    esac
done

install -dm755 %{buildroot}%{_bindir}
ln -s %{bundledir}/localsend_app %{buildroot}%{_bindir}/localsend

%desktop_file_install %{SOURCE1}

for px in 32 128 256 512; do
    install -Dpm644 data/flutter_assets/assets/img/logo-${px}.png \
        %{buildroot}%{_hicolordir}/${px}x${px}/apps/%{appid}.png
done

%terra_appstream

%check
%desktop_file_validate %{buildroot}%{_appsdir}/localsend.desktop

%files
%license LICENSE
%{_bindir}/localsend
%{bundledir}
%{_appsdir}/localsend.desktop
%{_hicolordir}/32x32/apps/%{appid}.png
%{_hicolordir}/128x128/apps/%{appid}.png
%{_hicolordir}/256x256/apps/%{appid}.png
%{_hicolordir}/512x512/apps/%{appid}.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Jul 26 2026 NichSchlagen <tim-rosenhagen@web.de>
- Initial package
