%undefine __brp_mangle_shebangs
%global __strip /bin/true
%global _build_id_links none

%ifarch x86_64
%global rpmarch x86_64
%elifarch aarch64
%global rpmarch arm64
%endif

Name:           desktop-plus-bin
%global appname desktop-plus
%global appid   org.desktop-plus.DesktopPlus
Version:        3.6.4.3
%electronmeta -D
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}CURL_GNUTLS
Release:        1%{?dist}
Summary:        A GitHub Desktop fork with advanced functionality and improvements
License:        MIT AND %{electron_license}
URL:            https://desktop-plus.org
Source0:        https://github.com/desktop-plus/desktop-plus/releases/download/v%{version}/DesktopPlus-v%{version}-linux-%{rpmarch}.rpm
Source1:        %{appid}.metainfo.xml
Packager:       Caio Bruno <cbrunofb@gmail.com>

ExclusiveArch:  x86_64 aarch64

BuildRequires:  anda-srpm-macros
BuildRequires:  cpio
BuildRequires:  terra-appstream-helper
Recommends:     (gnome-keyring or kf6-kwallet)

%description
Desktop Plus is a community fork of GitHub Desktop with additional features:
commit search, multi-account support (GitHub, Bitbucket, GitLab, Codeberg),
commit graph, multiple stashes per branch, and more.

%prep
%autosetup -Tc
rpm2cpio %{SOURCE0} | cpio -idm

%build

%install
cp -pr usr %{buildroot}/
rm -f %{buildroot}%{_prefix}/lib/%{appname}/chrome-sandbox
find %{buildroot}%{_prefix}/lib/%{appname} -type f -executable -exec \
  sed -i 's/libcurl-gnutls\.so\.4/libcurl.so.4\x00\x00\x00\x00\x00\x00\x00/g' {} \;
chmod 0755 %{buildroot}%{_prefix}/lib/%{appname}/resources/app/static/desktop-plus-cli
ln -sf %{_prefix}/lib/%{appname}/resources/app/static/desktop-plus-cli %{buildroot}%{_bindir}/desktop-plus-cli
rm -f %{buildroot}%{_datadir}/doc/%{appname}/copyright
cp -p usr/lib/%{appname}/LICENSE .
%terra_appstream -o %{SOURCE1}

%files
%license LICENSE
%{_bindir}/%{appname}
%{_bindir}/desktop-plus-cli
%{_prefix}/lib/%{appname}/
%{_appsdir}/%{appname}.desktop
%{_hicolordir}/*/apps/gh-desktop-plus.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Thu Jul 30 2026 Caio Bruno <cbrunofb@gmail.com>
- Initial package
