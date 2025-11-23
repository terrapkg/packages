%global debug_package %{nil}
%define __requires_exclude_from ^/usr/libexec/android-studio/.*$
%define __provides_exclude_from ^/usr/libexec/android-studio/.*|libedit\\so.*$
%global __requires_exclude ^libaaudio\\.so.*|^libandroid\\.so.*|^libmediandk\\.so.*|^liblog\\.so.*|^libc\\.so.*|^libm\\.so.*|^libdl\\.so.*|^libcrypt\\.so.*|^libstdc\\+\\+\\.so.*|^libncursesw\\.so.*|^libtinfo\\.so.*|^libnsl\\.so.*|^libpanelw\\.so.*$

Name:           android-studio
Version:        2025.2.1.8
Release:        1%?dist
Summary:        Official IDE for Android development
License:        Apache-2.0
Packager:       like-engels <higashikataengels@icloud.com>
URL:            https://developer.android.com/studio
Source0:        https://dl.google.com/dl/android/studio/ide-zips/%{version}/android-studio-%{version}-linux.tar.gz

Requires:       alsa-lib
Requires:       freetype
Requires:       which
Requires:       libXrender
Requires:       libXtst
Requires:       glibc
Requires:       libsecret

%description
Android Studio is the official IDE for Android development, and includes everything you need to build Android apps.

%prep
%setup -q -n android-studio

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}

cp -a * %{buildroot}%{_libexecdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
ln -s %{_libexecdir}/%{name}/bin/studio %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_licensedir}/%{name}
install -Dm644 LICENSE.txt %{buildroot}%{_licensedir}/%{name}/LICENSE.txt

install -Dm644 bin/studio.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Android Studio
Exec=android-studio %f
Icon=android-studio
Comment=The official Android IDE
Categories=Development;IDE;
Terminal=false
StartupNotify=true
StartupWMClass=jetbrains-studio
MimeType=application/x-extension-iml;
EOF

%files
%license %{_licensedir}/%{name}/LICENSE.txt
%{_libexecdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
