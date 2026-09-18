%global appid   com.abdownloadmanager
%global giturl  https://github.com/amir1376/ab-download-manager

Name:           ab-download-manager
Version:        1.10.4
Release:        1%?dist
Summary:        A fast, open-source download manager
URL:            https://abdownloadmanager.com
Source0:        abdownloadmanager.desktop
Source1:        com.abdownloadmanager.metainfo.xml

License:        Apache-2.0

BuildRequires:  gradle
BuildRequires:  java-25-openjdk-devel
BuildRequires:  java-25-openjdk-jmods

BuildRequires:  desktop-file-utils
BuildRequires:  terra-appstream-helper
BuildRequires:  appstream

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
AB Download Manager is a fast, modern download manager for Linux, Windows,
macOS, and Android. It supports download queues, scheduling, browser
integration, multiple connections, and a modern desktop interface.

%prep
# it's javaslop so of course there's some weird stuff
# in this case, that weird stuff is that it requires a git repository.
%git_clone %{giturl} v%{version}

%build
# The Android build is not needed for the Linux desktop package.
export SKIP_ANDROID_BUILD=true
./gradlew --no-daemon createReleaseFolderForCi

%install
install -dm755 %{buildroot}%{_libdir}/ABDownloadManager
install -dm755 %{buildroot}%{_bindir}

archive=$(find build -type f \( \
    -name 'ABDownloadManager_*_linux_*.tar.gz' -o \
    -name 'app.tar.gz' \
\) -print -quit)
test -n "$archive"
tar -xzf "$archive" -C %{buildroot}%{_libdir}

ln -s %{_libdir}/ABDownloadManager/bin/ABDownloadManager \
      %{buildroot}%{_bindir}/ABDownloadManager

%desktop_file_install %{SOURCE0} %{buildroot}%{_appsdir}/abdownloadmanager.desktop
%terra_appstream -o %{SOURCE1}

install -Dm644 desktop/app/icons/icon.png \
    %{buildroot}%{_iconsdir}/hicolor/512x512/apps/abdownloadmanager.png

%check
%desktop_file_validate %{buildroot}%{_appsdir}/abdownloadmanager.desktop
appstreamcli validate --no-net \
    %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%files
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md DONATE.md
%{_bindir}/ABDownloadManager
%{_libdir}/ABDownloadManager/
%{_appsdir}/abdownloadmanager.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/512x512/apps/abdownloadmanager.png

%changelog
* Fri Sep 18 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
