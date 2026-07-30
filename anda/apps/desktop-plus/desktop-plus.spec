%undefine __brp_mangle_shebangs
%define debug_package %{nil}
%global __strip /bin/true
%global _build_id_links none

%ifarch x86_64
%global rpmarch x86_64
%elifarch aarch64
%global rpmarch arm64
%endif

Name:           desktop-plus
Version:        3.6.4.1
%electronmeta
Release:        1%{?dist}
Summary:        A GitHub Desktop fork with advanced functionality and improvements
License:        MIT
URL:            https://desktop-plus.org
Source0:        https://github.com/desktop-plus/desktop-plus/releases/download/v%{version}/DesktopPlus-v%{version}-linux-%{rpmarch}.rpm
Packager:       Caio Bruno <cbrunofb@gmail.com>

ExclusiveArch:  x86_64 aarch64

BuildRequires:  cpio
Recommends:     (gnome-keyring or kf6-kwallet or kf5-wallet)

%description
Desktop Plus is a community fork of GitHub Desktop with additional features:
commit search, multi-account support (GitHub, Bitbucket, GitLab, Codeberg),
commit graph, multiple stashes per branch, and more.

%prep
%autosetup -Tc
rpm2cpio %{SOURCE0} | cpio -idm
chmod -R a+rX,u+w,go-w .

%build

%install
cp -pr usr %{buildroot}/
rm -f %{buildroot}%{_datadir}/doc/%{name}/copyright
cp -p usr/lib/%{name}/LICENSE .

%files
%license LICENSE
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%exclude %{_prefix}/lib/%{name}/chrome-sandbox
%attr(4755, root, root) %{_prefix}/lib/%{name}/chrome-sandbox
%{_appsdir}/%{name}.desktop
%{_hicolordir}/*/apps/gh-desktop-plus.png

%changelog
* Thu Jul 30 2026 Caio Bruno <cbrunofb@gmail.com>
- Initial package
