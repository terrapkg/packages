%global xurl https://files.pythonhosted.org/packages/e1/dc/585eee290ff22d3ea0a7067e16aa27bd9d1f4dbf8aee9397255eed8d3376/anki-26.9.3-cp310-abi3-manylinux_2_35_x86_64.whl
%global aurl https://files.pythonhosted.org/packages/36/34/40c929f171cdc7d6d3d9c93e557ee63ba8b64cb99b8b7d102cc7eda88750/anki-26.9.3-cp310-abi3-manylinux_2_35_aarch64.whl
%global qurl https://files.pythonhosted.org/packages/5b/d0/ee07f6baf6ce68a8a80dc58f1ec9b958e405cfe075626e6c662b2e60f21d/aqt-26.9.3-py3-none-any.whl
%global appid net.ankiweb.Anki

Name:			anki-bin
Version:		26.09.3
Release:		1%{?dist}
Summary:		Flashcard program for using space repetition learning (Installed with wheel)
License:		AGPL-3.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-3.0 AND Apache-2.0 AND CC-BY-2.5
URL:			https://apps.ankiweb.net/
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	python3-devel
BuildRequires:	python3-pip rpm_macro(fdupes) cargo
BuildRequires:	python3-sqlalchemy python3-simplejson python3-matplotlib python3-decorator python3-markdown python3-orjson
BuildRequires:	python3-requests python3-pygame python3-beautifulsoup4 python3-httplib2 python3-pyaudio python3-jsonschema
BuildRequires:	python3-flask-cors python3-protobuf python3-requests python3-waitress python3-pyqt6-webengine python3-send2trash
Requires:		libxcrypt-compat hicolor-icon-theme sox
Requires:		(mpv or mpv-nightly)

Conflicts:		anki
%ifarch x86_64
Source0:		%xurl
%elifarch aarch64
Source0:                %aurl
%endif
Source1:		%qurl
Source2:		https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/runanki.py
Source3:    https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/installer/linux-template/%7B%7B%20cookiecutter.format%20%7D%7D/%7B%7B%20cookiecutter.app_name%20%7D%7D/anki.desktop
Source4:    https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/aqt/data/qt/icons/anki.png
Source5:		https://raw.githubusercontent.com/ankitects/anki/%{version}/LICENSE
Source6:		https://raw.githubusercontent.com/ankitects/anki/%{version}/README.md

%description
Anki is a program designed to help you remember facts (such as words and
phrases in a foreign language) as easily, quickly and efficiently as possible.
Anki is based on a theory called spaced repetition.

%prep

%build

%install
mkdir -p %_pyproject_wheeldir
cp %{S:0} %{S:1} %_pyproject_wheeldir
%pyproject_install
%pyproject_save_files -D aqt '*aqt*'
%pyproject_save_files -D anki '*anki*'
install -Dm755 %{SOURCE2} "%{buildroot}/usr/bin/anki"
install -Dm644 %{SOURCE3} "%{buildroot}/usr/share/applications/anki.desktop"
install -Dm644 %{SOURCE4} "%{buildroot}/usr/share/pixmaps/anki.png"
install -Dm644 %{SOURCE5} "%{buildroot}/%{_datadir}/licenses/%{name}/LICENSE"
install -Dm644 %{SOURCE6} "%{buildroot}/%{_datadir}/doc/%{name}/README.md"

%terra_appstream


%files -f %{pyproject_files}-anki -f %{pyproject_files}-aqt
%license LICENSE
%doc README.md
%_bindir/anki
%_bindir/ankiw
%_datadir/applications/anki.desktop
%_datadir/pixmaps/anki.png
%_metainfodir/%appid.metainfo.xml

%changelog
* Thu Aug 13 2026 madonuko <madonuko@outlook.com> - 26.08.1-1
- update sources and versioning

* Fri Nov 10 2023 hazel-bunny <dabiswas112@gmail.com> - 23.10-2
- Add python3-orjson and mpv as dependencies

* Wed Jan 11 2023 madonuko <mado@fyralabs.com> - 2.1.60
- Initial package
