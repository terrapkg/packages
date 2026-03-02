%define debug_package %{nil}
%define appid com.github.moonshot

Name:           moonshot
Version:        1.0.1
Release:        1%?dist
Summary:        A beautiful cross-platform flashing tool
License:        GPL-3.0-or-later
URL:            https://github.com/FyraLabs/moonshot
Source0:        %url/archive/refs/tags/v%version.tar.gz
Source1:        com.github.moonshot.metainfo.xml

BuildRequires:  wails-v3
BuildRequires:  webkit2gtk4.1
BuildRequires:  golang

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
install -Dm644 build/linux/moonshot.desktop %{buildroot}%{_appsdir}/moonshot.desktop
install -Dm644 build/appicon.png            %{buildroot}%{_hicolordir}/512x512/apps/moonshot.png

%terra_appstream -o %{SOURCE1}

%files
%doc README.md
%license LICENSE
%{_bindir}/moonshot
%{_appsdir}/moonshot.desktop
%{_hicolordir}/512x512/apps/moonshot.png
%{_metainfodir}/com.github.moonshot.metainfo.xml

%changelog
* Mon Mar 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
