Name:			anki-bin
Version:		2.1.61
Release:		1%{?dist}
Summary:		Flashcard program for using space repetition learning (Installed with wheel)
License:		AGPL-3.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-3.0 AND Apache-2.0 AND CC-BY-2.5
URL:			https://apps.ankiweb.net/
BuildRequires:	python3-installer python3.11
Requires:		hicolor-icon-theme python3-sqlalchemy python3-simplejson python3-matplotlib python3-decorator python3-markdown python3-send2trash
Requires:		python3-requests python3-pygame python3-beautifulsoup4 python3-httplib2 python3-pyaudio python3-jsonschema sox libxcrypt-compat
Requires:		python3-flask-cors python3-protobuf python3-requests python3-waitress
BuildArch:		noarch
Conflicts:		anki
Source0:		https://files.pythonhosted.org/packages/cp39/a/anki/anki-%{version}-cp39-abi3-manylinux_2_28_%{_arch}.whl
Source1:		https://files.pythonhosted.org/packages/py3/a/aqt/aqt-%{version}-py3-none-any.whl
Source2:		https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/runanki.py
Source3:		https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/bundle/lin/anki.desktop
Source4:		https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/bundle/lin/anki.png
Source5:		https://raw.githubusercontent.com/ankitects/anki/%{version}/LICENSE
Source6:		https://raw.githubusercontent.com/ankitects/anki/%{version}/README.md

%description
Anki is a program designed to help you remember facts (such as words
and phrases in a foreign language) as easily, quickly and efficiently
as possible. Anki is based on a theory called spaced repetition.

%prep

%build

%install
python3.11 -m installer --destdir="%{buildroot}" %{SOURCE0}
python3.11 -m installer --destdir="%{buildroot}" %{SOURCE1}
install -Dm755 %{SOURCE2} "%{buildroot}/usr/bin/anki"
install -Dm644 %{SOURCE3} "%{buildroot}/usr/share/applications/anki.desktop"
install -Dm644 %{SOURCE4} "%{buildroot}/usr/share/pixmaps/anki.png"
install -Dm644 %{SOURCE5} "%{buildroot}/%{_datadir}/licenses/%{name}/LICENSE"
install -Dm644 %{SOURCE6} "%{buildroot}/%{_datadir}/doc/%{name}/README.md"


%files
%license LICENSE
%doc README.md
/usr/bin/anki
/usr/lib64/python*/site-packages/_aqt/
/usr/lib64/python*/site-packages/anki-%{version}.dist-info/
/usr/lib64/python*/site-packages/anki/
/usr/lib64/python*/site-packages/aqt-%{version}.dist-info/
/usr/lib64/python*/site-packages/aqt/
/usr/share/applications/anki.desktop
/usr/share/pixmaps/anki.png

%changelog
* Wed Jan 11 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
