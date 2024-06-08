Name:           anki-qt5
Version:        24.06.1
Release:        1%?dist
Summary:        Flashcard program for using space repetition learning
License:        AGPL-3.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-3.0 AND Apache-2.0 AND CC-BY-2.5
URL:            https://apps.ankiweb.net/
BuildRequires:  python3-devel python3-setuptools python3-waitress python3-protobuf python3-pysocks rpm_macro(fdupes)
BuildRequires:  python3-distro python3-flask-cors python3-jsonschema python3-send2trash python3-certifi python3-simplejson python3-pyqt5-sip
BuildRequires:  python3-installer make mold cargo git rsync ninja-build libxcrypt-compat nodejs python3.9 python-unversioned-command gcc
Requires:       hicolor-icon-theme python3-sqlalchemy python3-simplejson python3-matplotlib python3-decorator python3-markdown python3-send2trash python3-orjson mpv python3-qt5-webengine
Requires:       python3-requests python3-pygame python3-beautifulsoup4 python3-httplib2 python3-pyaudio python3-jsonschema sox libxcrypt-compat python3-pyqt5-sip
ExclusiveArch:  x86_64
Conflicts:      anki
Patch0:         0001-No-update.patch
Patch1:         0001-Force-qt5.patch

%description
Anki is a program designed to help you remember facts (such as words and
phrases in a foreign language) as easily, quickly and efficiently as possible.
Anki is based on a theory called spaced repetition.

%prep
git clone https://github.com/ankitects/anki .
git checkout %version
%patch1 -p1

# See https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=anki-qt5

%build
mold -run ./tools/build

%install
for file in out/wheels/*.whl; do
    python -m installer --destdir="%{buildroot}" $file
done

install -Dm644 qt/bundle/lin/anki.desktop %{buildroot}/%{_datadir}/applications/anki.desktop
install -Dm644 qt/bundle/lin/anki.png %{buildroot}/%{_datadir}/pixmaps/anki.png

sed "s*^#!/usr/bin/python\$*#!/usr/bin/python3*" %{buildroot}/%{_bindir}/anki > %{buildroot}/%{_bindir}/anki1
rm %{buildroot}/%{_bindir}/anki
mv %{buildroot}/%{_bindir}/anki1 %{buildroot}/%{_bindir}/anki
chmod 755 %{buildroot}%{_bindir}/anki

find %{buildroot} -iname __pycache__ | xargs -r rm -rf
find %{buildroot} -iname direct_url.json | xargs -r rm -rf

%fdupes %_libdir/python*/site-packages/_aqt/data/


%files
%license LICENSE*
%doc README*
%{_bindir}/anki
%{_datadir}/applications/anki.desktop
%{_datadir}/pixmaps/anki.png
/usr/lib64/python*/site-packages/aqt/
/usr/lib64/python*/site-packages/aqt-%{version}.dist-info/
/usr/lib64/python*/site-packages/_aqt/
/usr/lib64/python*/site-packages/anki/
/usr/lib64/python*/site-packages/anki-%{version}.dist-info/

%changelog
* Tue Jan 3 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.1.60
- Initial package
