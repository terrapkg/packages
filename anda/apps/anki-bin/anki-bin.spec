%global xurl https://files.pythonhosted.org/packages/2d/cc/3d1fd48589b288347c7d8cc39018a61ec7ca704059c1185925657bd6e4f9/anki-26.8.1-cp310-abi3-manylinux_2_35_x86_64.whl
%global aurl https://files.pythonhosted.org/packages/0a/bd/82f15738d7d356b69f708816ecb9699bf2dd4a9ead26d17ab4f1010f5607/anki-26.8.1-cp310-abi3-manylinux_2_35_aarch64.whl
%global qurl https://files.pythonhosted.org/packages/a7/5f/7d08084d5c97b1bad03b9bd64d24246b0918e94faf22ddd5e76fa2e52f7f/aqt-26.8.1-py3-none-any.whl

Name:			anki-bin
Version:		26.08.1
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
BuildRequires:	python3-protobuf >= 4.21
Requires:		python3-sqlalchemy python3-simplejson python3-matplotlib python3-decorator python3-markdown python3-orjson
Requires:		python3-requests python3-pygame python3-beautifulsoup4 python3-httplib2 python3-pyaudio python3-jsonschema
Requires:		python3-flask-cors python3-protobuf python3-requests python3-waitress python3-pyqt6-webengine python3-send2trash
Requires:		python3-protobuf >= 4.21
Requires:		pt-compat hicolor-icon-theme sox
Requires:		pv or mpv-nightly)

%dnl ExclusiveArch:	        x86_64
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
pip3 install --root=%{buildroot} %SOURCE0 %SOURCE1
install -Dm755 %{SOURCE2} "%{buildroot}/usr/bin/anki"
install -Dm644 %{SOURCE3} "%{buildroot}/usr/share/applications/anki.desktop"
install -Dm644 %{SOURCE4} "%{buildroot}/usr/share/pixmaps/anki.png"
install -Dm644 %{SOURCE5} "%{buildroot}/%{_datadir}/licenses/%{name}/LICENSE"
install -Dm644 %{SOURCE6} "%{buildroot}/%{_datadir}/doc/%{name}/README.md"

rm -rf %buildroot%_bindir/{distro,flask,jsonschema,markdown_py,normalizer,send2trash,waitress-serve}

%fdupes %buildroot%_libdir/python*/site-packages/_aqt/data/


%files
%license LICENSE
%doc README.md
%_bindir/anki
%_bindir/pyuic6
%_bindir/pylupdate6
%python3_sitearch/_aqt/
%python3_sitearch/anki-%{version}.dist-info/
%python3_sitearch/anki/
%python3_sitearch/aqt-%{version}.dist-info/
%python3_sitearch/aqt/
%_datadir/applications/anki.desktop
%_datadir/pixmaps/anki.png

%changelog
* Thu Aug 13 2026 madonuko <madonuko@outlook.com> - 26.08.1-1
- update sources and versioning

* Fri Nov 10 2023 hazel-bunny <dabiswas112@gmail.com> - 23.10-2
- Add python3-orjson and mpv as dependencies

* Wed Jan 11 2023 madonuko <mado@fyralabs.com> - 2.1.60
- Initial package
