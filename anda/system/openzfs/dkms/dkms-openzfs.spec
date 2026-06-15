%global debug_package %{nil}
%global __brp_mangle_shebangs %{nil}

%define module openzfs
%define modulename %{module}
%define source_name zfs
%define _kmod_src_root %{_usrsrc}/%{module}-%{version}

Name:           dkms-%{module}
Version:        2.4.3
Release:        1%{?dist}
Summary:        ZFS DKMS Kernel Modules
URL:            https://github.com/openzfs/zfs
Source0:        https://github.com/openzfs/zfs/releases/download/zfs-%{version}/zfs-%{version}.tar.gz
License:        CDDL-1.0
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl

Requires:       dkms >= 2.2.0.3
Requires:       gcc
Requires:       make
Requires:       perl
Requires:       diffutils
Requires:       kernel-devel
Requires:       kernel-modules
Requires:       openzfs = %{?epoch:%{epoch}:}%{version}-%{release}

Provides:       %{module}-kmod = %{version}-%{release}
Provides:       dkms-openzfs = %{version}-%{release}
Conflicts:      akmod-openzfs
RemovePathPostfixes: .dkms

Packager:       Willow Reed <willow@willowidk.dev>

%description
This package contains the DKMS-managed OpenZFS kernel modules.

%prep
%autosetup -n zfs-%{version}

%build
scripts/dkms.mkconf -n %{module} -v %{version} -f dkms.conf

%install
INITIAL_ENVDIR=`pwd`

make distdir
cd %{source_name}-%{version}
for file in $(find cmd dracut etc lib man rpm udev tests -type f); do \
    rm "$file"; \
    test "$file" != "${file%%.in}" && printf "\x25:\n\t#\n" > "$file"; \
    true; \
done
cd $INITIAL_ENVDIR

printf "#!/bin/sh\ncp \"$@\"\n" > %{source_name}-%{version}/cp
chmod 755 %{source_name}-%{version}/cp

mkdir -p %{buildroot}%{_usrsrc}
mv %{source_name}-%{version} %{buildroot}%{_kmod_src_root}.dkms
cp dkms.conf %{buildroot}%{_kmod_src_root}.dkms

%files
%defattr(-,root,root)
%{_kmod_src_root}.dkms

%pre
# Remove any existing openzfs dkms modules
dkms_root=/var/lib/dkms
if [ -d ${dkms_root}/%{module} ]; then
    cd ${dkms_root}/%{module}
    for x in [[:digit:]]*; do
        [ -d "$x" ] || continue
        otherver="$x"
        if [ "$otherver" != %{version} ]; then
            if [ `dkms status -m %{module} -v "$otherver" | grep -c %{module}` -gt 0 ]; then
                echo "Removing old %{module} dkms modules version $otherver from all kernels."
                dkms remove -m %{module} -v "$otherver" --all ||:
            fi
        fi
    done
fi

# Remove previous version when upgrading/installing
if [ `dkms status -m %{module} -v %{version} | grep -c %{module}` -gt 0 ]; then
    echo "Removing %{module} dkms modules version %{version} from all kernels."
    dkms remove -m %{module} -v %{version} --all ||:
fi

%post
echo "Adding %{module} dkms modules version %{version} to dkms."
dkms add -m %{module} -v %{version} --rpm_safe_upgrade ||:

echo "Installing %{module} dkms modules version %{version} for the current kernel."
dkms install --force -m %{module} -v %{version} ||:

%preun
# Do nothing if upgrade
if [ "$1" = "1" -o "$1" = "upgrade" ] ; then
    exit 0
fi

# Remove modules on uninstall
if [ "$1" = "0" -o "$1" = "remove" -o "$1" = "purge" ] ; then
    if [ `dkms status -m %{module} -v %{version} | grep -c %{module}` -gt 0 ]; then
        echo "Removing %{module} dkms modules version %{version} from all kernels."
        dkms remove -m %{module} -v %{version} --all --rpm_safe_upgrade ||:
    fi
fi

%changelog
* Thu Jan 01 2026 Willow Reed <willow@willowidk.dev>
- Initial package
