%global _binfmtdir %{_sysconfdir}/binfmt.d

Name:           java-binfmt
Version:        1.0.0
Release:        1%{?dist}
Summary:        Binfmt wrappers and utilities for Java and Jar files.
### License for the C file used in the binary.
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Source0:        https://github.com/terrapkg/pkg-java-binfmt/raw/refs/heads/main/javaclassname.c
Source1:        https://github.com/terrapkg/pkg-java-binfmt/raw/refs/heads/main/javawrapper
Source2:        https://github.com/terrapkg/pkg-java-binfmt/raw/refs/heads/main/jarwrapper
Source3:        https://github.com/terrapkg/pkg-java-binfmt/raw/refs/heads/main/Java.conf
Source4:        https://github.com/terrapkg/pkg-java-binfmt/raw/refs/heads/main/ExecutableJAR.conf
Source5:        https://github.com/terrapkg/pkg-java-binfmt/raw/refs/heads/main/Applet.conf
BuildRequires:  gcc
Packager:       ShinyGil <rockgrub@disroot.org>

%description
This package installs binfmt files for use with Java wrappers.

%package -n java-jarwrapper
Summary:        Wrapper to execute Jar files
Requires:       bash
Requires:       java
BuildArch:      noarch

%description -n java-jarwrapper
A binfmt wrapper to more easily execute Jar files.

%package -n java-javawrapper
Summary:       Wrapper for Java
Requires:      bash
Requires:      java
Requires:      java-javaclassname
BuildArch:     noarch

%description -n java-javawrapper
A wrapper for Java functions.

%package -n java-javaclassname
Summary:     The javaclassname executable
Requires:    java

%description -n java-javaclassname
The javaclassname executable for use with javawrapper.

%package -n java-applet-binfmt
Summary:      binfmt file for Java applets
Requires:     java-1.8.0-openjdk-devel
BuildArch:    noarch

%description -n java-applet-binfmt
This binfmt file runs Java applets in the usual way. This package contains a single file.

%build
gcc -O2 -o javaclassname %{SOURCE0}

install -Dpm755 javaclassname %{buildroot}%{_bindir}/javaclassname
install -Dpm755 %{SOURCE1} %{buildroot}%{_bindir}/javawrapper
install -Dpm755 %{SOURCE2} %{buildroot}%{_bindir}/jarwrapper

install -Dpm644 %{SOURCE3} %{buildroot}%{_binfmtdir}/Java.conf
install -Dpm644 %{SOURCE4} %{buildroot}%{_binfmtdir}/ExecutableJAR.conf
install -Dpm644 %{SOURCE5} %{buildroot}%{_binfmtdir}/Applet.conf

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

%posttrans -n java-jarwrapper
systemctl restart systemd-binfmt.service

%posttrans -n java-javawrapper
systemctl restart systemd-binfmt.service

%posttrans -n java-applet-binfmt
systemctl restart systemd-binfmt.service

%changelog
* Thu Jan 30 2025 ShinyGil <rockgrub@disroot.org>
- Initial package
