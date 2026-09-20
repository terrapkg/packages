%global debug_package %{nil}
%global appid com.quollwriter.QuollWriter

AutoReq: no
AutoProv: no

Name:           quollwriter
Version:        3.0.4
Release:        1%?dist
Summary:        A writing application that lets you focus on your words
URL:            https://quollwriter.com/
Source0:        https://github.com/garybentley/quollwriter/archive/refs/tags/v%{version}.tar.gz
Source1:        %{appid}.metainfo.xml
Source2:        %{appid}.desktop
Source3:        quollwriter.sh
License:        Apache-2.0
BuildRequires:  anda-srpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  gradle
BuildRequires:  java-25-openjdk-devel
BuildRequires:  openjfx
BuildRequires:  terra-appstream-helper
BuildRequires:  appstream
Requires:       java-25-openjdk
Requires:       openjfx

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n quollwriter-%{version}
# Gradle 9 removed the application plugin's mainClassName method.
sed -i "s/mainClassName 'com\.quollwriter\.Startup'/mainClass = 'com.quollwriter.Startup'/" build.gradle

%build
# copyToLib clears build/libs, so preserve its runtime JARs before creating
# QuollWriter's application JAR.
gradle -Pmodule_path=/usr/lib/jvm/openjfx copyToLib
mkdir runtime-libs
mv build/libs/*.jar runtime-libs/
gradle -Pmodule_path=/usr/lib/jvm/openjfx jar

%install
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/quollwriter
install -Dm644 build/libs/QuollWriter-*.jar %{buildroot}%{_javadir}/quollwriter/QuollWriter.jar
install -Dm644 runtime-libs/*.jar %{buildroot}%{_javadir}/quollwriter/
install -Dm644 imgs/window-icon-v3.png %{buildroot}%{_hicolordir}/48x48/apps/quollwriter.png
%desktop_file_install %{SOURCE2}

%terra_appstream -o %{SOURCE1}

%check
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%{_bindir}/quollwriter
%{_javadir}/quollwriter/
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/48x48/apps/quollwriter.png
%{_metainfodir}/%{appid}.metainfo.xml
%license license.txt

%changelog
* Sun Sep 20 2026 Cypress Reed <cypress@fyralabs.com>
- Build from the upstream GitHub release

* Thu Dec 04 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
