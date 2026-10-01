%global appid   app.winboat

Name:           winboat
%electronmeta -D
Version:        0.9.2
Release:        1%{?dist}
Summary:        Run Windows apps on Linux with seamless integration
License:        MIT AND %{electron_license}
URL:            https://github.com/winboat-org/winboat
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        %{appid}.metainfo.xml
ExclusiveArch:  %{electron_arches}

BuildRequires:  git-core
BuildRequires:  libxcrypt-compat
BuildRequires:  golang
BuildRequires:  /usr/bin/zip
BuildRequires:  nodejs24-bin
BuildRequires:  systemd-devel
%dnl BuildRequires:  tree

Requires:       pkgconfig(alsa)
Requires:       freerdp
Requires:       gtk3
Requires:       nss
Requires:       (moby-engine or podman)

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -S git
%{__npm} i

%build
npm run build:linux-gs
echo "Electron Builder" > %{rpmbuilddir}/webapp-tool.txt

%install
%electron_install -D -I icons/
%dnl tree -L 4 -f
%dnl install -Dm 755 %{name} -t %{buildroot}%{_bindir}

%terra_appstream -o %{S:1}

%files
%license README.md
%doc LICENSE
%{_bindir}/%{name}
%{_scalableiconsdir}/*.svg
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Sep 30 2026 Its-J <jonah@fyralabs.com> - 0.9.2-1
- Initial commit
