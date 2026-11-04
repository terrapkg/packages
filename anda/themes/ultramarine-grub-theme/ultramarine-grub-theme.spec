%global themes light dark darker
%global debug_package %{nil}
%global regen_grub [ -f /boot/grub2/grub.cfg ] && grub2-mkconfig -o /boot/grub2/grub.cfg >/dev/null 2>&1 || :

Name:           ultramarine-grub-theme
Version:        0.1.0
Release:        1%{?dist}
Summary:        KDE-style GRUB themes for Ultramarine Linux
License:        GPL-3.0-or-later
URL:            https://github.com/Ultramarine-Linux/grub-themes
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  grub2-tools-extra
BuildRequires:  google-noto-sans-fonts

%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif
Requires:       grub2-tools

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%package        light
Summary:        KDE-style Light GRUB theme for Ultramarine Linux
License:        GPL-3.0-or-later AND OFL-1.1 AND LicenseRef-Fyra-Labs-Proprietary
Requires:       %{name} = %{evr}
Conflicts:      %{name}-dark %{name}-darker
BuildArch:      noarch

%description    light
GRUB theme for Ultramarine Linux using KDE Plasma's default light colours.

%package        dark
Summary:        KDE-style Dark GRUB theme for Ultramarine Linux
License:        GPL-3.0-or-later AND OFL-1.1 AND LicenseRef-Fyra-Labs-Proprietary
Requires:       %{name} = %{evr}
Conflicts:      %{name}-light %{name}-darker
BuildArch:      noarch

%description    dark
GRUB theme for Ultramarine Linux using KDE Plasma's default dark colours.

%package        darker
Summary:        KDE-style Darker GRUB theme for Ultramarine Linux
License:        GPL-3.0-or-later AND OFL-1.1 AND LicenseRef-Fyra-Labs-Proprietary
Requires:       %{name} = %{evr}
Conflicts:      %{name}-light %{name}-dark
BuildArch:      noarch

%description    darker
GRUB theme for Ultramarine Linux with darker variant of KDE Plasma's default dark colors.

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

%transfiletriggerin -- %{_grubthemedir}/ultramarine- %{_sysconfdir}/grub.d/06_ultramarine-theme
%{regen_grub}

%transfiletriggerpostun -- %{_grubthemedir}/ultramarine-
%{regen_grub}

%postun
[ $1 -eq 0 ] && %{regen_grub}

%files
%license LICENSE LICENSE.notosans
%doc README.md
%config %{_sysconfdir}/grub.d/06_ultramarine-theme
%config %{_sysconfdir}/grub.d/30_uefi-class
%config %{_sysconfdir}/grub.d/30_uefi-firmware-z

%files light
%{_grubthemedir}/ultramarine-light

%files dark
%{_grubthemedir}/ultramarine-dark

%files darker
%{_grubthemedir}/ultramarine-darker

%changelog
* Mon Nov 02 2026 Its-J <jonah@fyralabs.com> - 0.1.0-1
- Initial package
