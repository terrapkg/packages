Name:           anki-qt5
Version:        2.1.55
Release:        %autorelease
Summary:        Flashcard program for using space repetition learning
License:        AGPLv3+ and GPLv3+ and LGPLv3 and MIT and BSD and ASL 2.0 and CC-BY-SA and CC-BY
URL:            https://apps.ankiweb.net/
BuildRequires:  python3-devel python3-setuptools python3-beautifulsoup4 python3-waitress python3-decorator python3-markdown python3-protobuf python3-pysocks 
BuildRequires:  python3-distro python3-flask-cors python3-jsonschema python3-requests python3-send2trash python3-certifi python3-pyqt5-sip python3-simplejson
BuildRequires:  desktop-file-utils libappstream-glib python3-installer make xdg-utils
BuildRequires:  cargo git rsync ninja-build libxcrypt-compat nodejs python3.9 python-unversioned-command
Requires:       hicolor-icon-theme python3-sqlalchemy python3-simplejson python3-matplotlib python3-decorator python3-markdown python3-send2trash
Requires:       python3-requests python3-pygame python3-beautifulsoup4 python3-httplib2 python3-pyaudio python3-jsonschema sox libxcrypt-compat
ExclusiveArch:  %{qt5_qtwebengine_arches} noarch
Patch0:         0001-Force-qt5.patch
Patch1:         0001-No-update.patch
BuildArch:      noarch
Conflicts:      anki

%description
Anki is a program designed to help you remember facts (such as words
and phrases in a foreign language) as easily, quickly and efficiently
as possible. Anki is based on a theory called spaced repetition.

%prep
git clone https://github.com/ankitects/anki .
git checkout %{version}
%patch0 -p1
%patch1 -p1

# See https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=anki

%build
./tools/build

%install
for file in out/wheels/*.whl; do
    python -m installer --destdir="%{buildroot}" $file
done

install -Dm644 qt/bundle/lin/anki.desktop %{buildroot}/%{_datadir}/applications/anki.desktop
install -Dm644 qt/bundle/lin/anki.png %{buildroot}/%{_datadir}/pixmaps/anki.png

sed "s*^#!/usr/bin/python\$*#!/usr/bin/python3*" %{buildroot}/%{_bindir}/anki > %{buildroot}/%{_bindir}/anki


%files
%license LICENSE*
%doc README*
%{_bindir}/anki
%{_datadir}/pixmaps/anki.png
%{_datadir}/applications/anki.desktop
/usr/lib64/python*/site-packages/aqt/
/usr/lib64/python*/site-packages/aqt-%{version}.dist-info/
/usr/lib64/python*/site-packages/_aqt/
/usr/lib64/python*/site-packages/_aqt-%{version}.dist-info/
/usr/lib64/python*/site-packages/anki/
/usr/lib64/python*/site-packages/anki-%{version}.dist-info/


%changelog
* Tue Jan 3 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
