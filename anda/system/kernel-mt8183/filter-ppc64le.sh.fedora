#! /bin/bash

# This is the ppc64le override file for the core/drivers package split.  The
# module directories listed here and in the generic list in filter-modules.sh
# will be moved to the resulting kernel-modules package for this arch.
# Anything not listed in those files will be in the kernel-core package.
#
# Please review the default list in filter-modules.sh before making
# modifications to the overrides below.  If something should be removed across
# all arches, remove it in the default instead of per-arch.

driverdirs="atm auxdisplay bcma bluetooth firewire fpga infiniband leds media memstick message mmc mtd nfc ntb pcmcia platform power ssb staging tty uio w1"

singlemods="ntb_netdev iscsi_ibft iscsi_boot_sysfs megaraid pmcraid qedi qla1280 9pnet_rdma rpcrdma nvmet-rdma nvme-rdma hid-picolcd hid-prodikeys hwpoison-inject target_core_user sbp_target cxgbit chcr rnbd-client rnbd-server mlx5_vdpa hid-playstation hid-nintendo mlx5-vfio-pci nvmem_u-boot-env intel-m10-bmc-pmci intel-m10-bmc-hwmon ptp_dfl_tod pds_vdpa pds-vfio-pci"
