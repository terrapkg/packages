%global themes breeze-dark breeze-light breeze-darker
%global debug_package %{nil}

Name:           ultramarine-grub-theme
Version:        1.0.0
Release:        1%{?dist}
Summary:        KDE Breeze style GRUB themes for Ultramarine Linux
SourceLicense:  AGPL-3.0-or-later
License:        %{sourcelicense} AND OFL-1.1 AND GPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND (LGPL-3.0-or-later OR CC-BY-SA-3.0) AND CC-BY-SA-4.0 AND CC-BY-4.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/Ultramarine-Linux/grub-theme
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  grub2-tools-extra
BuildRequires:  google-noto-sans-fonts

%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%package        breeze-dark
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense}
Summary:        Breeze Dark GRUB theme for Ultramarine Linux

%description    breeze-dark
GRUB theme for Ultramarine Linux using KDE's Breeze Dark colours.

%package        breeze-light
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense}
Summary:        Breeze Light GRUB theme for Ultramarine Linux

%description    breeze-light
GRUB theme for Ultramarine Linux using KDE's Breeze Light colours.

%package        breeze-darker
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense}
Summary:        Breeze Darker GRUB theme for Ultramarine Linux

%description    breeze-darker
GRUB theme for Ultramarine Linux using the Xela Breeze Darker colours.

%prep
%autosetup -n grub-theme-%{version}

%build
for t in %{themes}; do
  grub2-mkfont -s 16 -o themes/$t/noto_sans_regular_16.pf2 %{_fontbasedir}/google-noto/NotoSans-Regular.ttf
  grub2-mkfont -s 13 -o themes/$t/noto_sans_regular_13.pf2 %{_fontbasedir}/google-noto/NotoSans-Regular.ttf
done

%install
for t in %{themes}; do
  install -d %{buildroot}%{_grubthemedir}/ultramarine-$t
  cp -a themes/$t/. %{buildroot}%{_grubthemedir}/ultramarine-$t/
done
install -Dm755 -t %{buildroot}%{_sysconfdir}/grub.d grub.d/*

%files
%license LICENSE licenses/*
%doc README.md
%config(noreplace) %{_sysconfdir}/grub.d/06_ultramarine-theme
%config(noreplace) %{_sysconfdir}/grub.d/30_uefi-class
%config(noreplace) %{_sysconfdir}/grub.d/30_uefi-firmware-z

%files breeze-dark
%{_grubthemedir}/ultramarine-breeze-dark

%files breeze-light
%{_grubthemedir}/ultramarine-breeze-light

%files breeze-darker
%{_grubthemedir}/ultramarine-breeze-darker

%changelog
* Mon Nov 02 2026 Its-J <jonah@fyralabs.com> - 1.0.0-1
- Initial package
