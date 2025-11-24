%define theme_name orchis
%define original_theme_name Orchis

%define ver 2025-04-25

Name: gtk-theme-%theme_name
Version: 20250425
Release: 1%{?dist}
Summary: Orchis is a Material Design theme for GNOME/GTK based desktop environments
License: GPL-3.0-only
Url: https://github.com/vinceliuice/Orchis-theme/
Source0: %{url}/archive/refs/tags/%{ver}.tar.gz

BuildRequires: sassc

Requires: cinnamon-theme-%theme_name
Requires: gtk2-theme-%theme_name
Requires: gtk3-theme-%theme_name
Requires: gtk4-theme-%theme_name
Requires: metacity-theme-%theme_name
Requires: plank-theme-%theme_name
Requires: xfwm4-theme-%theme_name
Requires: sassc

BuildArch: noarch

%description
Orchis is a Material Design theme for GNOME/GTK based desktop environments.
Based on nana-4 -- materia-theme (https://github.com/nana-4/materia-theme).

%package common
Summary: Common files for %original_theme_name theme
Group: Graphical desktop/GNOME

%description common
%summary.

%package -n cinnamon-theme-%theme_name
Summary: %original_theme_name Cinnamon theme
Group: Graphical desktop/GNOME

Requires: %name-common

%description -n cinnamon-theme-%theme_name
%summary.

%package -n gtk2-theme-%theme_name
Summary: %original_theme_name GTK2 theme
Group: Graphical desktop/GNOME

Requires: %name-common
Requires: gtk2-themes-murrine

%description -n gtk2-theme-%theme_name
%summary.

%package -n gtk3-theme-%theme_name
Summary: %original_theme_name GTK3 theme
Group: Graphical desktop/GNOME

Requires: %name-common

%description -n gtk3-theme-%theme_name
%summary.

%package -n gtk4-theme-%theme_name
Summary: %original_theme_name GTK4 theme
Group: Graphical desktop/GNOME

Requires: %name-common

%description -n gtk4-theme-%theme_name
%summary.

%package -n metacity-theme-%theme_name
Summary: %original_theme_name Metacity theme
Group: Graphical desktop/GNOME

Requires: %name-common

%description -n metacity-theme-%theme_name
%summary.

%package -n plank-theme-%theme_name
Summary: %original_theme_name Plank theme
Group: Graphical desktop/GNOME

Requires: %name-common

%description -n plank-theme-%theme_name
%summary.

%package -n xfwm4-theme-%theme_name
Summary: %original_theme_name Xfwm theme
Group: Graphical desktop/XFce

Requires: %name-common

%description -n xfwm4-theme-%theme_name
%summary.

%prep
%autosetup -n Orchis-theme-%{ver}

%install
mkdir -p %buildroot%_datadir/themes
./install.sh       \
  --tweaks submenu \
  --tweaks dock    \
  --theme  all     \
  --dest   %buildroot%_datadir/themes

%files common
%_datadir/themes/%{original_theme_name}*/index.theme
%_datadir/themes/%{original_theme_name}*/COPYING
%doc README.md

%files -n cinnamon-theme-%theme_name
%_datadir/themes/%{original_theme_name}*/cinnamon

%files -n gtk2-theme-%theme_name
%_datadir/themes/%{original_theme_name}*/gtk-2.0

%files -n gtk3-theme-%theme_name
%_datadir/themes/%{original_theme_name}*/gnome-shell
%_datadir/themes/%{original_theme_name}*/gtk-3.0

%files -n gtk4-theme-%theme_name
%_datadir/themes/%{original_theme_name}*/gtk-4.0

%files -n metacity-theme-%theme_name
%_datadir/themes/%{original_theme_name}*/metacity-1

%files -n plank-theme-%theme_name
%_datadir/themes/%{original_theme_name}*/plank

%files -n xfwm4-theme-%theme_name
%_datadir/themes/%{original_theme_name}*/xfwm4

%changelog
* Sun Nov 23 2025 Owen Zimmerman <owen@fyralabs.com>
- Port to Terra

* Tue Jul 08 2025 David Sultaniiazov <x1z53@altlinux.org> 20250405-alt1
- Initial build
