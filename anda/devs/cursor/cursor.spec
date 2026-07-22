%undefine __brp_mangle_shebangs
%global __strip /bin/true
%global _build_id_links none

%global commit 63a2996a10d9e476b6c28e951dd7691d9c0cf480

%ifarch x86_64
%global platform x64
%global debarch amd64
%elifarch aarch64
%global platform arm64
%global debarch arm64
%endif

Name:           cursor
Version:        3.12.30
%electronmeta -D
Release:        1%{?dist}
Summary:        The AI Code Editor
License:        Proprietary AND %{electron_license}
URL:            https://cursor.com
Source0:        https://downloads.cursor.com/production/%{commit}/linux/%{platform}/deb/%{debarch}/deb/cursor_%{version}_%{debarch}.deb
ExclusiveArch:  x86_64 aarch64

BuildRequires:  anda-srpm-macros
BuildRequires:  binutils
BuildRequires:  tar
Requires:       ca-certificates

Packager:       Addison LeClair <me@addi.lol>

%description
The AI Code Editor.

%pkg_completion -Bz

%prep
%autosetup -Tc
ar x %{SOURCE0}
tar xf data.tar.xz

%build

%install
cp -pr usr %{buildroot}/
mv %{buildroot}%{_datadir}/appdata %{buildroot}%{_metainfodir}
mv %{buildroot}%{_datadir}/zsh/vendor-completions %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_bindir}
ln -sf %{_datadir}/%{name}/bin/%{name} %{buildroot}%{_bindir}/%{name}
cp -p usr/share/cursor/resources/app/LICENSE.txt .

%files
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%attr(4755, root, root) %{_datadir}/%{name}/chrome-sandbox
%{_appsdir}/%{name}.desktop
%{_appsdir}/%{name}-url-handler.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}-workspace.xml
%{_datadir}/pixmaps/co.anysphere.cursor.png

%changelog
* Thu Jul 09 2026 Addison LeClair <me@addi.lol> - 3.10.20-1
- Initial package
