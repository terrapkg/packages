Name:		dracut-strip-trigger
Version:	0
Release:	7%?dist
Summary:	Strip initramfs aggressively
License:	GPL-3.0-only
Requires:	dracut installonlypkg(kernel)
Conflicts:  dracut-config-generic
Source0:	LICENSE
Source1:    01-aggressive-strip.conf
BuildArch: noarch

%global _desc %{expand:
Strip initramfs automatically for each kernel update using --hostonly --aggressive-strip.
Do not install this package if you plan to use the system on different devices (e.g.
raw images like Raspberry Pi images).}

%description %_desc

%prep
cat<<EOF > README
%name %_desc
EOF
cp %{S:0} .

%install

mkdir -p %buildroot/usr/lib/dracut/dracut.conf.d/
cat<<EOF > %buildroot/usr/lib/dracut/dracut.conf.d/02-iscsi.conf
add_dracutmodules+=" iscsi "
EOF
cp %{S:1} %buildroot/usr/lib/dracut/dracut.conf.d/

%files
%doc README
%license LICENSE
/usr/lib/dracut/dracut.conf.d/02-iscsi.conf
/usr/lib/dracut/dracut.conf.d/01-aggressive-strip.conf

%post
echo 'Regenerating all initramfs…'
dracut --force --parallel --regenerate-all
echo 'All non-rescue initramfs have been regenerated.'
echo 'If you have problems booting up, use the rescue image, then uninstall `%name`.'

%postun
[ $1 = 0 ] && echo 'Regenerating all initramfs…'
[ $1 = 0 ] && dracut --force --parallel --regenerate-all
