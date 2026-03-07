%define debug_package %nil

Name:           anki
Version:        25.09.2
Release:        1%?dist
Summary:        Flashcard program for using space repetition learning
License:        AGPL-3.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-3.0 AND Apache-2.0 AND CC-BY-2.5
URL:            https://apps.ankiweb.net/
BuildRequires:  python3-devel python3-setuptools python3-waitress python3-protobuf python3-pysocks rpm_macro(fdupes)
BuildRequires:  python3-distro python3-flask-cors python3-jsonschema python3-send2trash python3-certifi python3-simplejson
BuildRequires:  python3-installer python-unversioned-command python3-pyqt6-webengine python3-pyqt6
BuildRequires:  anda-srpm-macros make mold cargo git protobuf-compiler rsync yarnpkg ninja-build pnpm libxcrypt-compat nodejs gcc
Requires:       hicolor-icon-theme python3-sqlalchemy python3-simplejson python3-matplotlib python3-decorator python3-markdown python3-send2trash
Requires:       python3-requests python3-pygame python3-beautifulsoup4 python3-httplib2 python3-pyaudio python3-jsonschema sox libxcrypt-compat python3-pyqt6-webengine
Recommends:     (mpv or mpv-nightly)
Obsoletes:      anki <= 2.1.15
Conflicts:      anki-qt5
Patch0:         0001-No-update.patch

%description
Anki is a program designed to help you remember facts (such as words and
phrases in a foreign language) as easily, quickly and efficiently as possible.
Anki is based on a theory called spaced repetition.

%prep
%git_clone https://github.com/ankitects/anki
%patch 0 -p1

# See https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=anki
# See https://git.alpinelinux.org/aports/tree/testing/anki/APKBUILD


export CARGO_HOME="./.cargo}"       # do not litter in ~
export YARN_CACHE_FOLDER="./.yarn}" # do not litter in ~

# fetch rust packages
cargo fetch --locked --target "%_arch-unknown-linux-gnu" &

# fetch node packages already in prepare()
yarn install --immutable --modules-folder out/node_modules --ignore-scripts
ln -sf out/node_modules ./

wait

%build
export RELEASE=2
export PYTHONPATH=%python3_sitelib
export PYTHON_BINARY=%__python3
export PROTOC_BINARY=$(which protoc)
export NODE_BINARY=$(which node)
export YARN_BINARY=$(which pnpm)
export CARGO_HOME="./.cargo}"       # do not litter in ~
export YARN_CACHE_FOLDER="./.yarn}" # do not litter in ~
cargo update
mold -run ./tools/build

%install
for file in out/wheels/*.whl; do
    python -m installer --destdir="%{buildroot}" $file
done

install -Dm644 qt/bundle/lin/anki.desktop %{buildroot}/%{_datadir}/applications/anki.desktop
install -Dm644 qt/bundle/lin/anki.png %{buildroot}/%{_datadir}/pixmaps/anki.png

sed -i "s*^#!/usr/bin/python\$*#!/usr/bin/python3*" %{buildroot}/%{_bindir}/anki

find %{buildroot} -iname __pycache__ | xargs -r rm -rf
find %{buildroot} -iname direct_url.json | xargs -r rm -rf

chmod 755 %{buildroot}%{_bindir}/anki

%fdupes %_libdir/python*/site-packages/_aqt/data/


%files
%license LICENSE*
%doc README*
%{_bindir}/anki
%{_datadir}/applications/anki.desktop
%{_datadir}/pixmaps/anki.png
%_libdir/python*/site-packages/aqt/
%_libdir/python*/site-packages/aqt-%{version}.dist-info/
%_libdir/python*/site-packages/_aqt/
%_libdir/python*/site-packages/anki/
%_libdir/python*/site-packages/anki-%{version}.dist-info/

%changelog
* Tue Jan 3 2023 madonuko <mado@fyralabs.com> - 2.1.60
- Initial package
