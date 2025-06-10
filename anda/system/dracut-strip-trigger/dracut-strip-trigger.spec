Name:		dracut-strip-trigger
Version:	0
Release:	1%?dist
Summary:	Strip initramfs aggressively
License:	GPL-3.0-only
Requires(post): dracut
Source0:	LICENSE

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

%files
%doc README
%license LICENSE

%post
echo 'Regenerating all initramfs…'
dracut --force --parallel --regenerate-all --hostonly --strip --aggressive-strip
echo 'All non-rescue initramfs have been regenerated.'
echo 'If you have problems booting up, use the rescue image, then uninstall `%name`.'

%triggerin -- kernel
dracut --force --hostonly --strip --aggressive-strip

%postun
echo 'Regenerating all initramfs…'
[ $1 = 0 ] && dracut --force --parallel --regenerate-all --no-hostonly --strip
