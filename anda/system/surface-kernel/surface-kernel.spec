# This bootstrap spec lets Andaman discover the package.  pre.rhai replaces it
# with the pinned linux-surface-generated Fedora kernel spec before builddep.
Name:           terra-surface-kernel
Version:        6.19.8
Release:        1%{?dist}
Summary:        Fedora kernel with Ultramarine linux-surface patches
License:        GPL-2.0-only
URL:            https://github.com/Ultramarine-Linux/linux-surface

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Bootstrap specification for the Terra linux-surface Fedora kernel source build.
