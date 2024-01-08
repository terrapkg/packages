# kernel-mt8183
This is a quick reference for those trying to build, update, or maintain this kernel build.

# Abstract
We use the kernel-ark sources, the upstream sources for the Fedora and Red Hat kernels to build an SRPM (they have a make target for this.)
From there, we unpack that SRPM into this directory, with our other Terra and mt8183 specific files and patches.
Yes, we know this is cursed, but this is how it's done in Fedora (as far as I can see)... so we might as well :p

# Upgrading/Unpacking the sources
1. Clone kernel-ark, checkout a branch/ref corresponding to the kernel version you want to base off. We currently use `kernel-6.7.0-0.rc8.1f874787ed9a.65`.
2. Generate the SRPM, using the following command: `IS_FEDORA=1 BUILD=500 SPECPACKAGE_NAME='kernel-mt8183' DISTLOCALVERSION=".fyra1" make dist-srpm`
3. Unpack the sources, into the Terra directory, by running `rpm2cpio <PATH_TO_SRPM> | cpio -idmv`. YOU NEED TO BE IN THE DIRECTORY OF THE TERRA PACKAGE, THIS WILL DROP FILES IN THE CWD.
4. Download the [config-chrultrabook-mt8184.aarch64](https://raw.githubusercontent.com/ellyq/board-google-kukui/main/linux/config-chrultrabook-mt8183.aarch64) config
5. Merge the config with the `kernel-mt8183-aarch64-fedora.config` using the command: `./merge.py config-chrultrabook-mt8183.aarch64 kernel-mt8183-aarch64-fedora.config  arm64 > kernel-mt8183-aarch64-fedora.config`
6. Add the following line after `Patch1` (line 978) in the spec file: ``Patch2: https://raw.githubusercontent.com/ellyq/board-google-kukui/main/linux/patches/mt8183-6.7-rc6.patch``
7. Track the linux kernel tarball using git lfs.