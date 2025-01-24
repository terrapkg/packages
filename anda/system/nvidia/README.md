# The Terra NVIDIA Driver tree

This directory contains the Terra distribution of NVIDIA drivers.

These driver packages are based on negativo17's NVIDIA driver packages for Fedora, with very slight modifications for hardware compatibility, and conforming to the Terra packaging guidelines.

Unlike negativo17 and Nobara, we do not manually generate a tarball of the NVIDIA drivers, but directly generate them
on-the-fly from the NVIDIA installer. This ensures that the packages can be easily maintained and updated, as long as the
self-extracting NVIDIA installer still has the same command-line options.

One major difference for Terra's distro is that we install the closed-source kernel modules by default, instead of the newer open-source kernel modules. This is because the open-source modules only support GPUs that have a GSP (GPU System Processor), which only includes Turing (RTX 20 series) and newer GPUs. As we would like to still support older GPUs, we install the closed-source modules by default.

## How Terra unpacks the self-extracting archive

Instead of pre-generating the tarball, we run the NVIDIA installer with the `-x` flag to extract the contents directly to the build directory. We then make use of an RPM macro to set the new build directory as that tree.

```rpmspec
Source0:        http://download.nvidia.com/XFree86/Linux-%{_arch}/%{version}/NVIDIA-Linux-%{_arch}-%{version}.run


... skip to the %prep section ...

%prep
sh %{SOURCE0} -x --target nvidia-driver-%{version}
%setup -T -D -n nvidia-driver-%{version}

%build

... Build the package as usual ...

```

This is simpler than manually generating the tarball, but comes with a slight cost of having to download the NVIDIA installer every time we build any package that relies on that archive.

## Support

If you have any issues with the NVIDIA drivers, please file an issue on the [Terra Monorepo](https://github.com/terrapkg/packages/issues). We will try to help you as best as we can.

## License

The NVIDIA drivers are licensed under the NVIDIA Software License. Please refer to the [NVIDIA Software License](https://www.nvidia.com/content/DriverDownload-March2009/licence.php?lang=us) for more information.

We do not modify the actual NVIDIA drivers in any way, only providing a re-packaged version compatible with Ultramarine and Fedora.
