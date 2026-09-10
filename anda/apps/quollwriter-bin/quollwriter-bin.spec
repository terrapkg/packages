# idek
%define _javadir /usr/share/java

AutoReq: no
AutoProv: no

Name:           QuollWriter-bin
Version:        3.0.5
Release:        1%?dist
Summary:        A writing application that lets you focus on your words
URL:            https://quollwriter.com/index.html
Source0:        https://quollwriter.com/download/linux/QuollWriter-linux-install-%{version}.deb
Source1:        https://github.com/garybentley/quollwriter/blob/master/license.txt
License:        Apache-2.0
BuildRequires:  anda-srpm-macros
BuildRequires:  dpkg
BuildRequires:  wget
Requires:       openjfx

Provides:       quollwriter
Provides:       Quollwriter

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
wget https://quollwriter.com/download/linux/QuollWriter-linux-install-%{version}.deb
mkdir QuollWriter
dpkg-deb -R QuollWriter-linux-install-%{version}.deb QuollWriter

%build

%install
mkdir -p %{buildroot}%{_datadir}/QuollWriter/test/
mkdir -p %{buildroot}%{_datadir}/QuollWriter/jre/bin
mkdir -p %{buildroot}%{_datadir}/QuollWriter/jre/conf
mkdir -p %{buildroot}%{_datadir}/QuollWriter/jre/conf/sdp
mkdir -p %{buildroot}%{_datadir}/QuollWriter/jre/conf/security
mkdir -p %{buildroot}%{_datadir}/QuollWriter/jre/include
mkdir -p %{buildroot}%{_datadir}/QuollWriter/jre/legal
mkdir -p %{buildroot}%{_datadir}/QuollWriter/jre/lib
mkdir -p %{buildroot}%{_datadir}/QuollWriter/jre/man
mkdir -p %{buildroot}%{_javadir}/QuollWriter

install -Dm755 QuollWriter/opt/QuollWriter/QuollWriter         %{buildroot}%{_bindir}/QuollWriter
install -Dm644 QuollWriter/opt/QuollWriter/*.jar               %{buildroot}%{_javadir}/QuollWriter/
%dnl install -Dm644 QuollWriter/opt/QuollWriter/jre/*.jar           %{buildroot}%{_javadir}/QuollWriter/
cp -a QuollWriter/opt/QuollWriter/                             %{buildroot}%{_datadir}/QuollWriter/
install -Dm644 %{SOURCE1}                                      %{buildroot}%{_defaultlicensedir}/%{name}/license.txt

sed -i \
    's|app_home=.*|app_home=%{_datadir}/QuollWriter|' \
    %{buildroot}%{_bindir}/QuollWriter

%files
%{_bindir}/QuollWriter
%{_datadir}/QuollWriter/
%{_javadir}/QuollWriter/
%{_defaultlicensedir}/%{name}/license.txt
%dnl %license license.txt

%changelog
* Thu Dec 04 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
