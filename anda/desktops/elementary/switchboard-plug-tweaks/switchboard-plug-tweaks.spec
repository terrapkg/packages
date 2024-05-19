%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type personal
%global plug_name pantheon-tweaks

Name:           switchboard-plug-tweaks
Summary:        Switchboard Tweaks Plug
Version:        2.0.0
Release:        1%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/pantheon-tweaks/pantheon-tweaks
Source0:        %{url}/archive/%{version}/%{plug_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}

Requires:       hicolor-icon-theme


%description
A system settings panel for the Pantheon Desktop Environment that lets
you easily and safely customise your desktop's appearance.

%description -l de
Ein Systemeinstellungsmodul für die Arbeitsumgebung »Pantheon«, mit die
Erscheinung der Arbeitsumgebung sicher und einfach angepasst werden kann.

%description -l fr
Un panneau de configuration système pour le bureau Pantheon qui vous permet
de personnaliser facilement et en toute sécurité l’apparence de votre bureau.

%description -l ja
簡単かつ安全にデスクトップの外観をカスタマイズできる、Pantheon デスクトップ向
けのシステム設定パネルです。

%description -l pt
Um painel de definições do sistema para o ambiente de trabalho Pantheon que
permite personalizar com facilidade e segurança a aparência do seu ambiente
de trabalho.


%prep
%autosetup -n %{plug_name}-%{version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug

# remove the specified stock icon from metainfo (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_name}.metainfo.xml

%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_name}.metainfo.xml


%files -f %{plug_name}-plug.lang
%license COPYING
%doc README.md
%doc AUTHORS
%doc CONTRIBUTORS

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_name}.metainfo.xml
%{_datadir}/icons/hicolor/*/categories/preferences-*.svg


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
