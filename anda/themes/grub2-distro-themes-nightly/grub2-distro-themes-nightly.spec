%global commit 6e9e018abf38c0b3ed2bff1912ecf30a94e0c917
%global commit_date 20260328
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global debug_package   %{nil}
%global spdx_url        https://raw.githubusercontent.com/spdx/license-list-data/main/text

%global themes archcraft arco-linux debian deepin endeavouros garuda gentoo kde-neon kubuntu linux-mint lubuntu nixos opensuse pop-os ubuntu-mate ultramarine vanilla-os void-linux xero-linux

Name:           grub2-distro-themes-nightly
Version:        3.2~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Distro themes for GRUB
SourceLicense:  GPL-3.0-or-later
License:        GPL-3.0-or-later
URL:            https://github.com/AdisonCavani/distro-grub-themes
Source0:        %url/archive/%commit/distro-grub-themes-%commit.tar.gz
Source1:        %{spdx_url}/CC-BY-SA-4.0.txt
Source2:        %{spdx_url}/CC-BY-SA-3.0.txt
Source3:        %{spdx_url}/CC-BY-4.0.txt
Source4:        %{spdx_url}/LGPL-3.0-or-later.txt
Source5:        %{spdx_url}/GPL-2.0-or-later.txt
Provides:       grub2-distro-themes

%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif

Packager:       Its-J <jonah@fyralabs.com>, Owen Zimmerman <owen@fyralabs.com>

%package        archcraft
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND GPL-3.0-only
Summary:        GRUB2 theme for archcraft

%description    archcraft
GRUB2 theme for archcraft.

%package        arco-linux
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND GPL-3.0-only
Summary:        GRUB2 theme for arco-linux

%description    arco-linux
GRUB2 theme for arco-linux.

%package        debian
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND (LGPL-3.0-or-later OR CC-BY-SA-3.0)
Summary:        GRUB2 theme for debian

%description    debian
GRUB2 theme for debian.

%package        deepin
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense}
Summary:        GRUB2 theme for deepin

%description    deepin
GRUB2 theme for deepin.

%package        endeavouros
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND GPL-3.0-only
Summary:        GRUB2 theme for endeavouros

%description    endeavouros
GRUB2 theme for endeavouros.

%package        garuda
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND GPL-3.0-only
Summary:        GRUB2 theme for garuda

%description    garuda
GRUB2 theme for garuda.

%package        gentoo
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND CC-BY-SA-4.0
Summary:        GRUB2 theme for gentoo

%description    gentoo
GRUB2 theme for gentoo.

%package        kde-neon
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND CC-BY-SA-4.0
Summary:        GRUB2 theme for kde-neon

%description    kde-neon
GRUB2 theme for kde-neon.

%package        kubuntu
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense}
Summary:        GRUB2 theme for kubuntu

%description    kubuntu
GRUB2 theme for kubuntu.

%package        linux-mint
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense}
Summary:        GRUB2 theme for linux-mint

%description    linux-mint
GRUB2 theme for linux-mint.

%package        lubuntu
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND GPL-2.0-or-later
Summary:        GRUB2 theme for lubuntu

%description    lubuntu
GRUB2 theme for lubuntu.

%package        nixos
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND CC-BY-4.0
Summary:        GRUB2 theme for nixos

%description    nixos
GRUB2 theme for nixos.

%package        opensuse
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND CC-BY-SA-4.0
Summary:        GRUB2 theme for opensuse

%description    opensuse
GRUB2 theme for opensuse.

%package        pop-os
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND CC-BY-SA-4.0
Summary:        GRUB2 theme for pop-os

%description    pop-os
GRUB2 theme for pop-os.

%package        ubuntu-mate
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND CC-BY-SA-4.0
Summary:        GRUB2 theme for ubuntu-mate

%description    ubuntu-mate
GRUB2 theme for ubuntu-mate.

%package        ultramarine
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND LicenseRef-Fyra-Labs-Proprietary
Summary:        GRUB2 theme for ultramarine

%description    ultramarine
GRUB2 theme for ultramarine.

%package        vanilla-os
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND CC-BY-SA-4.0
Summary:        GRUB2 theme for vanilla-os

%description    vanilla-os
GRUB2 theme for vanilla-os.

%package        void-linux
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND LicenseRef-Fedora-Public-Domain
Summary:        GRUB2 theme for void-linux

%description    void-linux
GRUB2 theme for void-linux.

%package        xero-linux
Requires:       %{name}%{?_isa} = %{evr}
License:        %{sourcelicense} AND GPL-3.0-only
Summary:        GRUB2 theme for xero-linux

%description    xero-linux
GRUB2 theme for xero-linux.

%description
%{summary}.

%prep
%autosetup -C
cp -p %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} .

%build

%install
for name in %{themes}; do
    theme=themes/$name.tar
    mkdir -p %{buildroot}%{_grubthemedir}/$name
    tar -C %{buildroot}%{_grubthemedir}/$name -xf "$theme"
done

%files
%license LICENSE
%doc README.md docs/*

%files archcraft
%{_grubthemedir}/archcraft

%files arco-linux
%{_grubthemedir}/arco-linux

%files debian
%license LGPL-3.0-or-later.txt CC-BY-SA-3.0.txt
%{_grubthemedir}/debian

%files deepin
%{_grubthemedir}/deepin

%files endeavouros
%{_grubthemedir}/endeavouros

%files garuda
%{_grubthemedir}/garuda

%files gentoo
%license CC-BY-SA-4.0.txt
%{_grubthemedir}/gentoo

%files kde-neon
%license CC-BY-SA-4.0.txt
%{_grubthemedir}/kde-neon

%files kubuntu
%{_grubthemedir}/kubuntu

%files linux-mint
%{_grubthemedir}/linux-mint

%files lubuntu
%license GPL-2.0-or-later.txt
%{_grubthemedir}/lubuntu

%files nixos
%license CC-BY-4.0.txt
%{_grubthemedir}/nixos

%files opensuse
%license CC-BY-SA-4.0.txt
%{_grubthemedir}/opensuse

%files pop-os
%license CC-BY-SA-4.0.txt
%{_grubthemedir}/pop-os

%files ultramarine
%{_grubthemedir}/ultramarine

%files ubuntu-mate
%license CC-BY-SA-4.0.txt
%{_grubthemedir}/ubuntu-mate

%files vanilla-os
%license CC-BY-SA-4.0.txt
%{_grubthemedir}/vanilla-os

%files void-linux
%{_grubthemedir}/void-linux

%files xero-linux
%{_grubthemedir}/xero-linux

%changelog
* Sun Oct 18 2026 Its-J <jonah@fyralabs.com>, Owen Zimmerman <owen@fyralabs.com>
- Initial package
