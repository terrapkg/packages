%undefine __brp_add_determinism
# disable debuginfo subpackage
%global debug_package %{nil}
# Disable build-id symlinks to avoid conflicts
%global _build_id_links none
# don't strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%global __strip /bin/true
# dont repack jars
%global __jar_repack %{nil}
# disable rpath checks
%define __brp_check_rpaths %{nil}

%define __requires_exclude_from ^/usr/libexec/android-studio-canary/.*$
%define __provides_exclude_from ^/usr/libexec/android-studio-canary/.*|libedit\\so.*$
%global __requires_exclude ^libaaudio\\.so.*|^libandroid\\.so.*|^libmediandk\\.so.*|^liblog\\.so.*|^libc\\.so.*|^libm\\.so.*|^libdl\\.so.*|^libcrypt\\.so.*|^libstdc\\+\\+\\.so.*|^libncursesw\\.so.*|^libtinfo\\.so.*|^libnsl\\.so.*|^libpanelw\\.so.*$

Name:           android-studio-canary
Version:        2025.3.3.1
Release:        2%?dist
Summary:        Official IDE for Android development (Canary build)
License:        Apache-2.0
Packager:       veuxit <erroor234@gmail.com>
ExclusiveArch:  x86_64
URL:            https://developer.android.com/studio/preview

%define suffixS panda3-canary1

Source0:        https://dl.google.com/dl/android/studio/ide-zips/%{version}/android-studio-%{suffixS}-linux.tar.gz

Requires:       alsa-lib
Requires:       freetype
Requires:       which
Requires:       libXrender
Requires:       libXtst
Requires:       glibc
Requires:       libsecret

BuildRequires:  desktop-file-utils

%description
Android Studio is the official IDE for Android development, and includes everything you need to build Android apps.

%prep
%autosetup -n android-studio

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}

cp -a * %{buildroot}%{_libexecdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
ln -s %{_libexecdir}/%{name}/bin/studio %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_licensedir}/%{name}
install -Dm644 LICENSE.txt %{buildroot}%{_licensedir}/%{name}/LICENSE.txt

install -d %{buildroot}%{_datadir}/pixmaps
install -m 0644 -p bin/studio.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 0644 -p bin/studio.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Android Studio Canary
Exec=android-studio-canary
Icon=android-studio-canary
Comment=Official IDE for Android development (Canary build)
Categories=Development;IDE;
Terminal=false
StartupNotify=true
StartupWMClass=jetbrains-studio-canary
MimeType=application/x-extension-iml;
EOF

%check
%desktop_file_validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license %{_licensedir}/%{name}/LICENSE.txt
%{_libexecdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/pixmaps/android-studio-canary.png
%{_datadir}/icons/hicolor/scalable/apps/android-studio-canary.svg
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Feb 18 2026 veuxit <erroor234@gmail.com> - 2025.3.2.4
- Update .spec file 

* Sun Feb 15 2026 veuxit <erroor234@gmail.com> - 2025.3.2.4
- Initial package release