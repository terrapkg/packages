%undefine __brp_add_determinism
# disable debuginfo subpackage
%global debug_package %{nil}
# Disable build-id symlinks to avoid conflicts
%global _build_id_links none
# don't strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%global __strip /bin/true
# disable rpath checks
%define __brp_check_rpaths %{nil}
%define _missing_build_ids_terminate_build 0

Name:           spotify-client
Version:        1.2.82.428
Release:        1%?dist
Summary:        Spotify desktop client
License:        Proprietary
Packager:       veuxit <erroor234@gmail.com>
ExclusiveArch:  x86_64
URL:            https://www.spotify.com/linux

%define suffixS g0ac8be2b

Source0:        https://repository-origin.spotify.com/pool/non-free/s/spotify-client/spotify-client_%{version}.%{suffixS}_amd64.deb

BuildRequires:  dpkg tar binutils desktop-file-utils 
Requires:       nss libcurl alsa-lib openssl libayatana-appindicator-gtk3 libayatana-ido-gtk3 libayatana-indicator-gtk3


%description
Spotify is a social music platform that gives you access to millions of songs

%prep
mkdir -p %{_builddir}/%{name}
cd %{_builddir}/%{name}
ar x %{SOURCE0}
tar -xvzf data.tar.gz

%install
cd %{_builddir}/%{name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/spotify
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

cp -r usr/share/spotify/* %{buildroot}%{_datadir}/spotify/
cp usr/share/spotify/icons/spotify-linux-256.png %{buildroot}%{_datadir}/pixmaps/spotify-client.png

ln -s %{_datadir}/spotify/spotify %{buildroot}%{_bindir}/spotify

cp usr/share/spotify/spotify.desktop %{buildroot}%{_datadir}/applications/

%files
%{_bindir}/spotify
%{_datadir}/spotify/
%{_datadir}/applications/spotify.desktop
%{_datadir}/pixmaps/spotify-client.png

%changelog
* Fri Feb 27 2026 veux <erroor234@gmail.com> - 1.2.56.502-1
- Initial package release
