%define debug_package %{nil}
%define appid com.fyralabs.moonshot

Name:           moonshot
Version:        1.0.2
Release:        1%?dist
Summary:        A beautiful cross-platform flashing tool
License:        GPL-3.0-or-later
URL:            https://github.com/FyraLabs/moonshot
Source0:        %url/archive/refs/tags/v%version.tar.gz
Source1:        com.fyralabs.moonshot.metainfo.xml

BuildRequires:  wails3
BuildRequires:  golang
BuildRequires:  bun-bin
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libsoup-3.0)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.
Why?

    - Community frustration with existing flashing tools.
    - We have unique ideas that we want to implement in the future, ex: selecting distro images from within the app.
    - For fun.

%prep
%autosetup

%build
EXTRA_TAGS=gtk4 wails3 build

%install
install -Dm755 bin/moonshot                 %{buildroot}%{_bindir}/moonshot
install -Dm644 build/linux/moonshot.desktop %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm644 build/appicon.png            %{buildroot}%{_hicolordir}/512x512/apps/moonshot.png

%terra_appstream -o %{SOURCE1}

%files
%doc README.md
%license LICENSE
%{_bindir}/moonshot
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/512x512/apps/moonshot.png
%{_metainfodir}/com.fyralabs.moonshot.metainfo.xml

%changelog
* Mon Mar 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
