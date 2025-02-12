%global commit 9b3c3202435720ad5d76928c94c8f1c6e22693b7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250131
%global _binfmtdir %{_exec_prefix}/lib/binfmt.d

Name:           java-binfmt
Version:        1.0.0^%{commit_date}git%{shortcommit}
Release:        2%{?dist}
Summary:        Binfmt wrappers and utilities for Java and Jar files.
### License for the C file used in the binary.
License:        GPL-2.0-or-later
Source0:        https://raw.githubusercontent.com/terrapkg/pkg-java-binfmt/%{commit}/javaclassname.c
Source1:        https://raw.githubusercontent.com/terrapkg/pkg-java-binfmt/%{commit}/javawrapper
Source2:        https://raw.githubusercontent.com/terrapkg/pkg-java-binfmt/%{commit}/jarwrapper
Source3:        https://raw.githubusercontent.com/terrapkg/pkg-java-binfmt/%{commit}/Java.conf
Source4:        https://raw.githubusercontent.com/terrapkg/pkg-java-binfmt/%{commit}/ExecutableJAR.conf
Source5:        https://raw.githubusercontent.com/terrapkg/pkg-java-binfmt/%{commit}/Applet.conf
Source6:        https://raw.githubusercontent.com/terrapkg/pkg-java-binfmt/%{commit}/Applet-lib64.conf
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
Packager:       ShinyGil <rockgrub@disroot.org>

%description
This package installs binfmt files for use with Java wrappers.

%package -n       java-jarwrapper
Summary:          Wrapper to execute Jar files
Requires:         bash
Requires:         java
Requires(post):   systemd
Requires(postun): systemd
BuildArch:        noarch

%description -n   java-jarwrapper
A binfmt wrapper to more easily execute Jar files.

%package -n       java-javawrapper
Summary:          Wrapper for Java
Requires:         bash
Requires:         java
Requires:         java-javaclassname
Requires(post):   systemd
Requires(postun): systemd
BuildArch:        noarch

%description -n   java-javawrapper
A wrapper for Java functions.

%package -n       java-javaclassname
Summary:          The javaclassname executable
Requires:         java

%description -n   java-javaclassname
The javaclassname executable for use with javawrapper.

%package -n       java-applet-binfmt
Summary:          binfmt file for Java applets
Requires(post):   systemd
Requires(postun): systemd
Recommends:       adoptium-temurin-java-repository
BuildArch:        noarch

%description -n   java-applet-binfmt
This binfmt file runs Java applets in the usual way. A compatible Java version will need to be manually installed and configured.

%build
/usr/bin/gcc %{optflags} -o javaclassname %{S:0}

install -Dpm755 javaclassname %{buildroot}%{_bindir}/javaclassname
install -Dpm755 %{SOURCE1} %{buildroot}%{_bindir}/javawrapper
install -Dpm755 %{SOURCE2} %{buildroot}%{_bindir}/jarwrapper

install -Dpm644 %{SOURCE3} %{buildroot}%{_binfmtdir}/Java.conf
install -Dpm644 %{SOURCE4} %{buildroot}%{_binfmtdir}/ExecutableJAR.conf
install -Dpm644 %{SOURCE5} %{buildroot}%{_binfmtdir}/Applet.conf
install -Dpm644 %{SOURCE6} %{buildroot}%{_binfmtdir}/Applet-lib64.conf

%files -n java-jarwrapper
%{_binfmtdir}/ExecutableJAR.conf
%{_bindir}/jarwrapper

%files -n java-javawrapper
%{_binfmtdir}/Java.conf
%{_bindir}/javawrapper

%files -n java-javaclassname
%{_bindir}/javaclassname

%files -n java-applet-binfmt
%{_binfmtdir}/Applet.conf
%{_binfmtdir}/Applet-lib64.conf

%post -n java-jarwrapper
/bin/systemctl --system try-restart systemd-binfmt.service &>/dev/null || :

%postun -n java-jarwrapper
/bin/systemctl --system try-restart systemd-binfmt.service &>/dev/null || :

%post -n java-javawrapper
/bin/systemctl --system try-restart systemd-binfmt.service &>/dev/null || :

%postun -n java-javawrapper
/bin/systemctl --system try-restart systemd-binfmt.service &>/dev/null || :

%post -n java-applet-binfmt
/bin/systemctl --system try-restart systemd-binfmt.service &>/dev/null || :

%postun -n java-applet-binfmt
/bin/systemctl --system try-restart systemd-binfmt.service &>/dev/null || :

%changelog
* Thu Jan 30 2025 ShinyGil <rockgrub@disroot.org>
- Initial package
