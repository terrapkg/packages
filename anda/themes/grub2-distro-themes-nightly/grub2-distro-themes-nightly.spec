%global commit 6e9e018abf38c0b3ed2bff1912ecf30a94e0c917
%global commit_date 20260328
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           grub2-distro-themes-nightly
Version:        3.2~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Distro themes for GRUB
License:        GPL-3.0-or-later
URL:            https://github.com/AdisonCavani/distro-grub-themes
Source0:        %url/archive/%commit/distro-grub-themes-%commit.tar.gz
Provides:       grub2-distro-themes

%ifnarch aarch64
Requires:       grub2
%else
Requires:       grub2-efi
%endif

Packager:       Its-J <jonah@fyralabs.com>, Owen Zimmerman <owen@fyralabs.com>

%global debug_package   %{nil}
%global _grubthemedir /boot/grub2/themes

%package        acer
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for acer

%description    acer
GRUB2 theme for acer.

%package        almalinux
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for almalinux

%description    almalinux
GRUB2 theme for almalinux.

%package        aorus
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for aorus

%description    aorus
GRUB2 theme for aorus.

%package        apple
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for apple

%description    apple
GRUB2 theme for apple.

%package        arch-linux
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for arch-linux

%description    arch-linux
GRUB2 theme for arch-linux.

%package        archcraft
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for archcraft

%description    archcraft
GRUB2 theme for archcraft.

%package        arco-linux
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for arco-linux

%description    arco-linux
GRUB2 theme for arco-linux.

%package        artix-linux
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for artix-linux

%description    artix-linux
GRUB2 theme for artix-linux.

%package        asrock
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for asrock

%description    asrock
GRUB2 theme for asrock.

%package        asus-rog
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for asus-rog

%description    asus-rog
GRUB2 theme for asus-rog.

%package        asus-tuf
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for asus-tuf

%description    asus-tuf
GRUB2 theme for asus-tuf.

%package        asus
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for asus

%description    asus
GRUB2 theme for asus.

%package        bedrock-linux
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for bedrock-linux

%description    bedrock-linux
GRUB2 theme for bedrock-linux.

%package        centos
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for centos

%description    centos
GRUB2 theme for centos.

%package        chromeos
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for chromeos

%description    chromeos
GRUB2 theme for chromeos.

%package        debian
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for debian

%description    debian
GRUB2 theme for debian.

%package        deepin
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for deepin

%description    deepin
GRUB2 theme for deepin.

%package        dell
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for dell

%description    dell
GRUB2 theme for dell.

%package        elementaryos
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for elementaryos

%description    elementaryos
GRUB2 theme for elementaryos.

%package        endeavouros
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for endeavouros

%description    endeavouros
GRUB2 theme for endeavouros.

%package        fedora
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for fedora

%description    fedora
GRUB2 theme for fedora.

%package        framework
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for framework

%description    framework
GRUB2 theme for framework.

%package        framework13
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for framework13

%description    framework13
GRUB2 theme for framework13.

%package        freebsd
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for freebsd

%description    freebsd
GRUB2 theme for freebsd.

%package        fujitsu
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for fujitsu

%description    fujitsu
GRUB2 theme for fujitsu.

%package        garuda
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for garuda

%description    garuda
GRUB2 theme for garuda.

%package        gentoo
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for gentoo

%description    gentoo
GRUB2 theme for gentoo.

%package        gigabyte
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for gigabyte

%description    gigabyte
GRUB2 theme for gigabyte.

%package        hp-omen
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for hp-omen

%description    hp-omen
GRUB2 theme for hp-omen.

%package        hp-victus
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for hp-victus

%description    hp-victus
GRUB2 theme for hp-victus.

%package        hp
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for hp

%description    hp
GRUB2 theme for hp.

%package        huawei
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for huawei

%description    huawei
GRUB2 theme for huawei.

%package        kde-neon
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for kde-neon

%description    kde-neon
GRUB2 theme for kde-neon.

%package        kingston
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for kingston

%description    kingston
GRUB2 theme for kingston.

%package        kubuntu
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for kubuntu

%description    kubuntu
GRUB2 theme for kubuntu.

%package        legion
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for legion

%description    legion
GRUB2 theme for legion.

%package        lenovo
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for lenovo

%description    lenovo
GRUB2 theme for lenovo.

%package        lg
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for lg

%description    lg
GRUB2 theme for lg.

%package        linux-lite
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for linux-lite

%description    linux-lite
GRUB2 theme for linux-lite.

%package        linux-mint
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for linux-mint

%description    linux-mint
GRUB2 theme for linux-mint.

%package        lubuntu
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for lubuntu

%description    lubuntu
GRUB2 theme for lubuntu.

%package        manjaro
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for manjaro

%description    manjaro
GRUB2 theme for manjaro.

%package        medion
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for medion

%description    medion
GRUB2 theme for medion.

%package        msi
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for msi

%description    msi
GRUB2 theme for msi.

%package        mx-linux
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for mx-linux

%description    mx-linux
GRUB2 theme for mx-linux.

%package        nixos
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for nixos

%description    nixos
GRUB2 theme for nixos.

%package        nobara
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for nobara

%description    nobara
GRUB2 theme for nobara.

%package        opensuse
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for opensuse

%description    opensuse
GRUB2 theme for opensuse.

%package        parabola
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for parabola

%description    parabola
GRUB2 theme for parabola.

%package        pop-os
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for pop-os

%description    pop-os
GRUB2 theme for pop-os.

%package        proxmox
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for proxmox

%description    proxmox
GRUB2 theme for proxmox.

%package        razer
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for razer

%description    razer
GRUB2 theme for razer.

%package        rocky-linux
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for rocky-linux

%description    rocky-linux
GRUB2 theme for rocky-linux.

%package        samsung
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for samsung

%description    samsung
GRUB2 theme for samsung.

%package        slackware
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for slackware

%description    slackware
GRUB2 theme for slackware.

%package        solus
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for solus

%description    solus
GRUB2 theme for solus.

%package        supermicro
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for supermicro

%description    supermicro
GRUB2 theme for supermicro.

%package        system76
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for system76

%description    system76
GRUB2 theme for system76.

%package        thinkpad
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for thinkpad

%description    thinkpad
GRUB2 theme for thinkpad.

%package        toshiba
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for toshiba

%description    toshiba
GRUB2 theme for toshiba.

%package        ubuntu-mate
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for ubuntu-mate

%description    ubuntu-mate
GRUB2 theme for ubuntu-mate.

%package        ubuntu
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for ubuntu

%description    ubuntu
GRUB2 theme for ubuntu.

%package        ultramarine
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for ultramarine

%description    ultramarine
GRUB2 theme for ultramarine.

%package        vaio
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for vaio

%description    vaio
GRUB2 theme for vaio.

%package        vanilla-os
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for vanilla-os

%description    vanilla-os
GRUB2 theme for vanilla-os.

%package        ventoy
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for ventoy

%description    ventoy
GRUB2 theme for ventoy.

%package        void-linux
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for void-linux

%description    void-linux
GRUB2 theme for void-linux.

%package        windows-10
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for windows-10

%description    windows-10
GRUB2 theme for windows-10.

%package        windows-11
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for windows-11

%description    windows-11
GRUB2 theme for windows-11.

%package        xero-linux
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for xero-linux

%description    xero-linux
GRUB2 theme for xero-linux.

%package        zorin-os
Requires:       %{name}%{?_isa} = %{evr}
Summary:        GRUB2 theme for zorin-os

%description    zorin-os
GRUB2 theme for zorin-os.

%description
%{summary}.

%prep
%autosetup -C

%build

%install
for theme in themes/*.tar; do
    name=$(basename "$theme" .tar)
    mkdir -p %{buildroot}%{_grubthemedir}/$name
    tar -C %{buildroot}%{_grubthemedir}/$name -xf "$theme"
done

%files
%license LICENSE
%doc README.md docs/*

%files acer
%{_grubthemedir}/acer

%files almalinux
%{_grubthemedir}/almalinux

%files aorus
%{_grubthemedir}/aorus

%files apple
%{_grubthemedir}/apple

%files arch-linux
%{_grubthemedir}/arch-linux

%files archcraft
%{_grubthemedir}/archcraft

%files arco-linux
%{_grubthemedir}/arco-linux

%files artix-linux
%{_grubthemedir}/artix-linux

%files asrock
%{_grubthemedir}/asrock

%files asus-rog
%{_grubthemedir}/asus-rog

%files asus-tuf
%{_grubthemedir}/asus-tuf

%files asus
%{_grubthemedir}/asus

%files bedrock-linux
%{_grubthemedir}/bedrock-linux

%files centos
%{_grubthemedir}/centos

%files chromeos
%{_grubthemedir}/chromeos

%files debian
%{_grubthemedir}/debian

%files deepin
%{_grubthemedir}/deepin

%files dell
%{_grubthemedir}/dell

%files elementaryos
%{_grubthemedir}/elementaryos

%files endeavouros
%{_grubthemedir}/endeavouros

%files fedora
%{_grubthemedir}/fedora

%files framework
%{_grubthemedir}/framework

%files framework13
%{_grubthemedir}/framework13

%files freebsd
%{_grubthemedir}/freebsd

%files fujitsu
%{_grubthemedir}/fujitsu

%files garuda
%{_grubthemedir}/garuda

%files gentoo
%{_grubthemedir}/gentoo

%files gigabyte
%{_grubthemedir}/gigabyte

%files hp-omen
%{_grubthemedir}/hp-omen

%files hp-victus
%{_grubthemedir}/hp-victus

%files hp
%{_grubthemedir}/hp

%files huawei
%{_grubthemedir}/huawei

%files kde-neon
%{_grubthemedir}/kde-neon

%files kingston
%{_grubthemedir}/kingston

%files kubuntu
%{_grubthemedir}/kubuntu

%files legion
%{_grubthemedir}/legion

%files lenovo
%{_grubthemedir}/lenovo

%files lg
%{_grubthemedir}/lg

%files linux-lite
%{_grubthemedir}/linux-lite

%files linux-mint
%{_grubthemedir}/linux-mint

%files lubuntu
%{_grubthemedir}/lubuntu

%files manjaro
%{_grubthemedir}/manjaro

%files medion
%{_grubthemedir}/medion

%files msi
%{_grubthemedir}/msi

%files mx-linux
%{_grubthemedir}/mx-linux

%files nixos
%{_grubthemedir}/nixos

%files nobara
%{_grubthemedir}/nobara

%files opensuse
%{_grubthemedir}/opensuse

%files parabola
%{_grubthemedir}/parabola

%files pop-os
%{_grubthemedir}/pop-os

%files proxmox
%{_grubthemedir}/proxmox

%files razer
%{_grubthemedir}/razer

%files rocky-linux
%{_grubthemedir}/rocky-linux

%files samsung
%{_grubthemedir}/samsung

%files slackware
%{_grubthemedir}/slackware

%files solus
%{_grubthemedir}/solus

%files supermicro
%{_grubthemedir}/supermicro

%files system76
%{_grubthemedir}/system76

%files thinkpad
%{_grubthemedir}/thinkpad

%files toshiba
%{_grubthemedir}/toshiba

%files ubuntu-mate
%{_grubthemedir}/ubuntu-mate

%files ubuntu
%{_grubthemedir}/ubuntu

%files ultramarine
%{_grubthemedir}/ultramarine

%files vaio
%{_grubthemedir}/vaio

%files vanilla-os
%{_grubthemedir}/vanilla-os

%files ventoy
%{_grubthemedir}/ventoy

%files void-linux
%{_grubthemedir}/void-linux

%files windows-10
%{_grubthemedir}/windows-10

%files windows-11
%{_grubthemedir}/windows-11

%files xero-linux
%{_grubthemedir}/xero-linux

%files zorin-os
%{_grubthemedir}/zorin-os

%changelog
* Sun Oct 18 2026 Its-J <jonah@fyralabs.com>, Owen Zimmerman <owen@fyralabs.com>
- Initial package
