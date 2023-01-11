Name:			anki-bin
Version:		2.1.56
Release:		%autorelease
Summary:		Flashcard program for using space repetition learning (Installed with wheel)
License:		AGPLv3+ and GPLv3+ and LGPLv3 and MIT and BSD and ASL 2.0 and CC-BY-SA and CC-BY
URL:			https://apps.ankiweb.net/
BuildRequires:	python3-installer
Requires:		hicolor-icon-theme python3-sqlalchemy python3-simplejson python3-matplotlib python3-decorator python3-markdown python3-send2trash
Requires:		python3-requests python3-pygame python3-beautifulsoup4 python3-httplib2 python3-pyaudio python3-jsonschema sox libxcrypt-compat
BuildArch:		noarch
Conflicts:		anki
Source0:		https://files.pythonhosted.org/packages/cp39/a/anki/anki-%{version}-cp39-abi3-manylinux_2_28_%{_arch}.whl
Source1:		https://files.pythonhosted.org/packages/py3/a/aqt/aqt-%{version}-py3-none-any.whl
Source2:		https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/runanki.py
Source3:		https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/bundle/lin/anki.desktop
Source4:		https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/bundle/lin/anki.png

%description
Anki is a program designed to help you remember facts (such as words
and phrases in a foreign language) as easily, quickly and efficiently
as possible. Anki is based on a theory called spaced repetition.

%prep
%autosetup


%build


%install
python -m installer --destdir="%{buildroot}" %{SOURCE0}
python -m installer --destdir="%{buildroot}" %{SOURCE1}
install -Dm755 %{SOURCE2} "%{buildroot}/usr/bin/anki"
install -Dm644 %{SOURCE3} "%{buildroot}/usr/share/applications/anki.desktop"
install -Dm644 %{SOURCE4} "%{buildroot}/usr/share/pixmaps/anki.png"


%files
%license LICENSE*
%doc README*


%changelog
* Wed Jan 11 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
