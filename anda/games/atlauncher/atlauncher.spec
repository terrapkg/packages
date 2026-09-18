%global debug_package %{nil}

%global appid com.atlauncher.atlauncher

Name:           atlauncher
Version:        3.4.41.2
Release:        1%{?dist}
Summary:        A launcher for Minecraft which integrates multiple different modpacks

License:        GPL-3.0-only
URL:            https://atlauncher.com/
Source0:        https://github.com/ATLauncher/ATLauncher/archive/refs/tags/v%{version}.tar.gz
Source1:        https://services.gradle.org/distributions/gradle-8.12.1-bin.zip

BuildRequires:  unzip
BuildRequires:  temurin-17-jdk
BuildRequires:  anda-srpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  terra-appstream-helper
BuildRequires:  appstream

Requires:       java >= 1.8.0
Requires:       alsa-lib
Requires:       libglvnd
Requires:       libpulseaudio
Requires:       libudev
Requires:       libX11
Requires:       libXcursor
Requires:       libXxf86vm
Recommends:     flite
Suggests:       gamemode

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n ATLauncher-%{version}

sed -i "/include('app')/d" settings.gradle
# Normalize upstream AppStream metadata for Terra.
sed -i \
    -e 's|<id>atlauncher</id>|<id>%{appid}</id>|' \
    -e 's|<icon type="remote"[^>]*>[^<]*</icon>|<icon type="stock">atlauncher</icon>|' \
    -e 's|<summary>[^<]*</summary>|<summary>A launcher for Minecraft modpacks</summary>|' \
    -e '/<releases>/,/<\/releases>/d' \
    packaging/linux/_common/atlauncher.metainfo.xml

# Older build plugins use APIs removed by the Gradle version in Terra.
sed -i "/id 'org.cadixdev.licenser'/d; s/id 'com.github.johnrengelman.shadow' version '8.1.1'/id 'com.gradleup.shadow' version '9.2.2'/" build.gradle
awk '
  /^license \{$/ { skip = 1; depth = 1; next }
  skip {
    line = $0
    depth += gsub(/\{/, "", line)
    depth -= gsub(/\}/, "", line)
    if (depth <= 0) skip = 0
    next
  }
  { print }
' build.gradle > build.gradle.tmp
mv build.gradle.tmp build.gradle
unzip -q %{SOURCE1}

%build
./gradle-8.12.1/bin/gradle --no-daemon --no-build-cache shadowJar

%install
install -Dpm644 build/libs/ATLauncher-%{version}.jar \
    %{buildroot}%{_datadir}/java/ATLauncher.jar

mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/atlauncher <<'EOF'
#!/bin/sh
exec %{_bindir}/java -jar %{_datadir}/java/ATLauncher.jar \
    --working-dir "${XDG_DATA_HOME:-$HOME/.local/share}/ATLauncher" \
    --no-launcher-update "$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/atlauncher

%desktop_file_install packaging/linux/_common/atlauncher.desktop
%desktop_file_edit -k Path -v %{_datadir}/java -f %{buildroot}%{_appsdir}/atlauncher.desktop
sed -i '/^TerminalOptions=/d' %{buildroot}%{_appsdir}/atlauncher.desktop
install -Dpm644 packaging/linux/_common/atlauncher.metainfo.xml \
    %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dpm644 packaging/linux/_common/atlauncher.svg \
    %{buildroot}%{_scalableiconsdir}/atlauncher.svg
install -Dpm644 packaging/linux/_common/atlauncher.png \
    %{buildroot}%{_hicolordir}/128x128/apps/atlauncher.png
%terra_appstream
release_date=$(date -u -d "@${SOURCE_DATE_EPOCH}" +%Y-%m-%d)
sed -Ei "s|(<release version=\"%{version}\")([^>]*)/>|\1 date=\"${release_date}\"\2/>|" \
    %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%check
%desktop_file_validate %{buildroot}%{_appsdir}/atlauncher.desktop
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/atlauncher
%{_datadir}/java/ATLauncher.jar
%{_appsdir}/atlauncher.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/atlauncher.svg
%{_hicolordir}/128x128/apps/atlauncher.png

%changelog
* Thu Sep 17 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
