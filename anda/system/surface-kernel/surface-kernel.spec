# This bootstrap spec lets Andaman discover the package.  pre.rhai replaces it
# with the pinned linux-surface-generated Fedora kernel spec before builddep.
Name:           kernel-surface
Version:        6.19.8
Release:        3%{?dist}
Summary:        Fedora kernel with linux-surface patches
License:        GPL-2.0-only
URL:            https://github.com/Ultramarine-Linux/linux-surface

%description
Bootstrap specification for the linux-surface Fedora kernel source build.
