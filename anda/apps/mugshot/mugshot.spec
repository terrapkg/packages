%global app org.bluesabre.Mugshot
%global _description %{expand:
Mugshot is a lightweight user configuration utility for Linux designed for simplicity and ease of
use. Quickly update your personal profile and sync your updates across applications.}


Name:           python-mugshot
Version:        0.4.3
Release:        1%?dist
Summary:        User Management Utility for Linux
License:        GPL-3.0
URL:            https://github.com/bluesabre/mugshot
Source0:        %url/archive/refs/tags/mugshot-%version.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  glib2
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-wheel

%description %_description

%package -n mugshot
Requires:       util-linux-user
Requires:       python3-cairo
Requires:       python3-gi
Requires:       python3-pexpect
Summary:        User Management Utility for Linux

%description -n mugshot %_description

%prep
%autosetup -n mugshot-mugshot-%version

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L 'mugshot*'
install -Dm644 data/glib-2.0/schemas/%{lower:%app}.gschema.xml %buildroot%_datadir/glib-2.0/schemas/

%find_lang mugshot

%check
#pyproject_check_import
desktop-file-validate %buildroot%_datadir/applications/%app.desktop
appstream-util validate-relax --nonet %buildroot%_metainfodir/mugshot.appdata.xml

%files -n mugshot -f %{pyproject_files} -f mugshot.lang
%doc README.md NEWS
%license COPYING
%_bindir/mugshot
%_datadir/glib-2.0/schemas/%{lower:%app}.gschema.xml
%_datadir/applications/%app.desktop
%_datadir/mugshot/
%_metainfodir/mugshot.appdata.xml
%_mandir/man1/mugshot.1.gz
%_iconsdir/hicolor/*/apps/mugshot.svg
