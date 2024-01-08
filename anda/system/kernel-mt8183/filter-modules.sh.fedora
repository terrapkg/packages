#! /bin/bash
#
# Called as filter-modules.sh list-of-modules Arch

# This script filters the modules into the kernel-core and kernel-modules
# subpackages.  We list out subsystems/subdirs to prune from the installed
# module directory.  What is left is put into the kernel-core package.  What is
# pruned is contained in the kernel-modules package.
#
# This file contains the default subsys/subdirs to prune from all architectures.
# If an architecture needs to differ, we source a per-arch filter-<arch>.sh file
# that contains the set of override lists to be used instead.  If a module or
# subsys should be in kernel-modules on all arches, please change the defaults
# listed here.

# Overrides is individual modules which need to remain in kernel-core due to deps.
overrides="cec"

# Set the default dirs/modules to filter out
driverdirs="atm auxdisplay bcma bluetooth firewire fpga infiniband leds media memstick mfd mmc mtd nfc ntb pcmcia platform power ssb soundwire staging tty uio w1"

chardrvs="mwave pcmcia"

netdrvs="appletalk can dsa hamradio ieee802154 ppp slip usb wireless"

ethdrvs="3com adaptec alteon amd aquantia atheros broadcom cadence calxeda chelsio cisco dec dlink emulex marvell mellanox neterion nvidia packetengines qlogic rdc sfc silan sis smsc stmicro sun tehuti ti wiznet xircom"

cryptdrvs="bcm caam cavium chelsio hisilicon marvell qat"

iiodrvs="accel light pressure proximity"

iiocommondrvs="cros_ec_sensors"

inputdrvs="gameport tablet touchscreen"

hiddrvs="surface-hid"

scsidrvs="aacraid aic7xxx be2iscsi bfa bnx2i bnx2fc csiostor cxgbi esas2r fcoe fnic isci libsas lpfc megaraid mpt3sas mvsas pm8001 qla2xxx qla4xxx sym53c8xx_2 ufs qedf"

usbdrvs="atm image misc serial"

fsdrvs="affs befs coda cramfs dlm ecryptfs hfs hfsplus jfs jffs2 minix nilfs2 ocfs2 reiserfs romfs sysv ubifs ufs"

netprots="6lowpan appletalk atm ax25 batman-adv bluetooth can dsa ieee802154 l2tp mac80211 mac802154 mpls netrom nfc rds rfkill rose sctp smc wireless"

drmdrvs="amd ast bridge gma500 i2c i915 mgag200 nouveau panel radeon"

singlemods="ntb_netdev iscsi_ibft iscsi_boot_sysfs megaraid pmcraid qedi qla1280 9pnet_rdma rpcrdma nvmet-rdma nvme-rdma hid-picolcd hid-prodikeys hwpoison-inject target_core_user sbp_target cxgbit  chcr parport_serial regmap-sdw regmap-sdw-mbq arizona-micsupp hid-asus iTCO_wdt rnbd-client rnbd-server mlx5_vdpa spi-altera-dfl nct6775 hid-playstation hid-nintendo asus_wmi_sensors asus_wmi_ec_sensors mlx5-vfio-pci video int3406_thermal apple_bl ptp_dfl_tod intel-m10-bmc-hwmon intel_rapl_tpmi pds_vdpa hp-wmi-sensors pds-vfio-pci gpio-ljca spi-ljca i2c-ljca"

# Grab the arch-specific filter list overrides
source ./filter-$2.sh

filter_dir() {
	filelist=$1
	dir=$2

	grep -v -e "${dir}/" ${filelist} > ${filelist}.tmp

	if [ $? -ne 0 ]
	then
		echo "Couldn't remove ${dir}.  Skipping."
	else
		grep -e "${dir}/" ${filelist} >> k-d.list
		mv ${filelist}.tmp $filelist
	fi
	
	return 0
}

filter_ko() {
	filelist=$1
	mod=$2

	grep -v -e "${mod}.ko" ${filelist} > ${filelist}.tmp

	if [ $? -ne 0 ]
	then
		echo "Couldn't remove ${mod}.ko  Skipping."
	else
		grep -e "${mod}.ko" ${filelist} >> k-d.list
		mv ${filelist}.tmp $filelist
	fi
	
	return 0
}

# Filter the drivers/ subsystems
for subsys in ${driverdirs}
do
	filter_dir $1 drivers/${subsys}
done

# Filter the networking drivers
for netdrv in ${netdrvs}
do
	filter_dir $1 drivers/net/${netdrv}
done

# Filter the char drivers
for char in ${chardrvs}
do
	filter_dir $1 drivers/char/${char}
done

# Filter the ethernet drivers
for eth in ${ethdrvs}
do
	filter_dir $1 drivers/net/ethernet/${eth}
done

# Filter the crypto drivers
for crypt in ${cryptdrvs}
do
	filter_dir $1 drivers/crypto/${crypt}
done

# SCSI
for scsi in ${scsidrvs}
do
	filter_dir $1 drivers/scsi/${scsi}
done

# IIO
for iio in ${iiodrvs}
do
        filter_dir $1 drivers/iio/${iio}
done

# IIO Common
for iio in ${iiocommondrvs}
do
        filter_dir $1 drivers/iio/common/${iio}
done

# Input
for input in ${inputdrvs}
do
	filter_dir $1 drivers/input/${input}
done

# hid
for hid in ${hiddrvs}
do
	filter_dir $1 drivers/hid/${hid}
done

# USB
for usb in ${usbdrvs}
do
	filter_dir $1 drivers/usb/${usb}
done

# Filesystems
for fs in ${fsdrvs}
do
	filter_dir $1 fs/${fs}
done

# Network protocols
for prot in ${netprots}
do
	filter_dir $1 kernel/net/${prot}
done

# DRM
for drm in ${drmdrvs}
do
	filter_dir $1 drivers/gpu/drm/${drm}
done

# Just kill sound.
filter_dir $1 kernel/sound
filter_dir $1 kernel/drivers/soundwire

# Now go through and filter any single .ko files that might have deps on the
# things we filtered above
for mod in ${singlemods}
do
        filter_ko $1 ${mod}
done

# Now process the override list to bring those modules back into core
for mod in ${overrides}
do
	grep -v -e "/${mod}.ko" k-d.list > k-d.list.tmp
	if [ $? -ne 0 ]
        then
                echo "Couldn't save ${mod}.ko  Skipping."
        else
                grep -e "/${mod}.ko" k-d.list >> $filelist
                mv k-d.list.tmp k-d.list
        fi

done

# Go through our generated drivers list and remove the .ko files.  We'll
# restore them later.
for mod in `cat k-d.list`
do
	rm -rf $mod
done
