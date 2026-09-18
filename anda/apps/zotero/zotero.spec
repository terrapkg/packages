%global debug_package %{nil}
%global appid org.zotero.Zotero
%global bundledir %{_libdir}/zotero

%ifarch x86_64
%global zotero_arch x64
%elifarch aarch64
%global zotero_arch arm64
%endif

Name:           zotero
Version:        10.0.3
Release:        1%{?dist}
Summary:        Collect, organize, cite, and share your research sources
URL:            https://www.zotero.org/
License:        AGPL-3.0-or-later
ExclusiveArch:  x86_64 aarch64

Source1:        %{appid}.metainfo.xml

BuildRequires:  nodejs >= 18
BuildRequires:  git-lfs
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  appstream
BuildRequires:  terra-appstream-helper
BuildRequires:  appstream
BuildRequires:  openssl
BuildRequires:  python3
BuildRequires:  perl
BuildRequires:  rsync
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  xz
BuildRequires:  pkgconfig(openssl)

Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       xdg-utils

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Zotero is a free, easy-to-use tool to help you collect, organize, cite, and
share research sources.

%prep
%git_clone https://github.com/zotero/zotero %{version}
git-lfs checkout

%__npm install --no-audit --no-fund

%build
%__npm run build
app/scripts/dir_build -f -p l -a %{zotero_arch}

%install
install -dm755 %{buildroot}%{bundledir}
cp -a app/staging/Zotero_linux-*/* %{buildroot}%{bundledir}/

install -dm755 %{buildroot}%{_bindir}
ln -sr %{buildroot}%{bundledir}/zotero %{buildroot}%{_bindir}/zotero

%desktop_file_install -k Exec,Icon -v zotero,zotero -u %U \
    %{buildroot}%{bundledir}/zotero.desktop
rm %{buildroot}%{bundledir}/zotero.desktop

for size in 32 64 128; do
    install -Dpm644 %{buildroot}%{bundledir}/icons/icon${size}.png \
        %{buildroot}%{_hicolordir}/${size}x${size}/apps/zotero.png
done

%terra_appstream -o %{SOURCE1}

%check
%desktop_file_validate -f %{buildroot}%{_appsdir}/zotero.desktop
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%files
%{_bindir}/zotero
%{bundledir}/
%{_appsdir}/zotero.desktop
%{_hicolordir}/32x32/apps/zotero.png
%{_hicolordir}/64x64/apps/zotero.png
%{_hicolordir}/128x128/apps/zotero.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Thu Sep 17 2026 Cypress Reed <cypress@fyralabs.com>
- initial commit
