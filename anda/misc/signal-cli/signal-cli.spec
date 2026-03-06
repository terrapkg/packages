%global appid org.asamk.SignalCli

%define debug_package %{nil}

Name:             signal-cli
Version:          0.14.0
Release:          1%?dist
Summary:          signal-cli provides an unofficial commandline, JSON-RPC and dbus interface for the Signal messenger
License:          GPL-3.0-only
URL:              https://github.com/AsamK/signal-cli
Source0:          %url/releases/download/v%version/%name-%version.tar.gz
BuildArch:        noarch

BuildRequires:    gcc-c++
BuildRequires:    gradle
BuildRequires:    anda-srpm-macros
BuildRequires:    java-21-openjdk
BuildRequires:    java-21-openjdk-devel
BuildRequires:    systemd-rpm-macros
BuildRequires:    make
BuildRequires:    asciidoc

Recommends:       java-21-openjdk

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
signal-cli is a commandline interface for the Signal messenger.
It supports registering, verifying, sending and receiving messages.
signal-cli uses a patched libsignal-service-java, extracted from the Signal-Android source code.
For registering you need a phone number where you can receive SMS or incoming calls.

signal-cli is primarily intended to be used on servers to notify admins of important events.
For this use-case, it has a daemon mode with JSON-RPC interface (man page) and D-BUS interface (man page).
For the JSON-RPC interface there's also a simple example client, written in Rust.

signal-cli needs to be kept up-to-date to keep up with Signal-Server changes.
The official Signal clients expire after three months and then the Signal-Server can make incompatible changes.
So signal-cli releases older than three months may not work correctly.

%prep
# The release tarballs don't include buildable source code
%git_clone %{url} v%{version}

%build
./gradlew build \
--no-daemon
./gradlew installDist

pushd man
%{make_build}
popd

%install
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_iconsdir}/hicolor/scalable/apps
mkdir -p %{buildroot}%{_javadir}/%{name}/lib
install -Dm755 build/install/signal-cli/bin/signal-cli          %{buildroot}%{_bindir}/%{name}
install -Dm644 data/signal-cli.sysusers.conf                    %{buildroot}%{_libdir}/sysusers.d/signal-cli.sysusers.conf
install -Dm644 data/signal-cli.tmpfiles.conf                    %{buildroot}%{_libdir}/tmpfiles.d/signal-cli.tmpfiles.conf
install -Dm644 data/org.asamk.Signal.conf                       %{buildroot}%{_sysconfdir}/dbus-1/system.d/org.asamk.Signal.conf
install -Dm644 data/*.service                                   %{buildroot}%{_unitdir}/
install -Dm644 data/*.socket                                    %{buildroot}%{_unitdir}/
install -Dm644 data/org.asamk.SignalCli.metainfo.xml            %{buildroot}%{_metainfodir}/org.asamk.SignalCli.metainfo.xml
install -Dm644 data/org.asamk.SignalCli.svg                     %{buildroot}%{_iconsdir}/hicolor/scalable/apps/

install -Dm644 man/%{name}.1                                    %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm644 man/%{name}-dbus.5                               %{buildroot}%{_mandir}/man5/%{name}-dbus.5
install -Dm644 man/%{name}-jsonrpc.5                            %{buildroot}%{_mandir}/man5/%{name}-jsonrpc.5

rm -f lib/commons-logging-*.jar
rm -f lib/libsignal-client*.jar
install -Dm644 build/install/signal-cli/lib/*.jar               %{buildroot}%{_javadir}/%{name}/lib/

# Fix launcher to use the package-installed jars
sed -i \
  's|^APP_HOME=.*$|APP_HOME=%{_javadir}/%{name}|' \
  %{buildroot}%{_bindir}/signal-cli

%terra_appstream

%post
%systemd_post org.asamk.Signal.service
%systemd_post signal-cli.service
%systemd_post signal-cli@.service
%systemd_post signal-cli-socket.service

%preun
%systemd_preun org.asamk.Signal.service
%systemd_preun signal-cli.service
%systemd_preun signal-cli@.service
%systemd_preun signal-cli-socket.service

%postun
%systemd_postun_with_restart org.asamk.Signal.service
%systemd_postun_with_restart signal-cli.service
%systemd_postun_with_restart signal-cli@.service
%systemd_postun_with_restart signal-cli-socket.service

%files
%doc README.md CONTRIBUTING.md CHANGELOG.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/sysusers.d/signal-cli.sysusers.conf
%{_libdir}/tmpfiles.d/signal-cli.tmpfiles.conf
%{_sysconfdir}/dbus-1/system.d/org.asamk.Signal.conf
%{_unitdir}/org.asamk.Signal.service
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}-socket.service
%{_unitdir}/%{name}-socket.socket
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}-dbus.5.*
%{_mandir}/man5/%{name}-jsonrpc.5.*
%{_metainfodir}/%{appid}.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/%{appid}.svg
%{_javadir}/%{name}/lib/*.jar

%changelog
* Sun Dec 07 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
