Name:			uutils-coreutils
Version:		0.0.22
Release:		1%?dist
Summary:		Cross-platform Rust rewrite of the GNU coreutils
License:		MIT
URL:			https://github.com/uutils/coreutils
Source0:		%url/archive/refs/tags/%version.tar.gz
Requires:		glibc
BuildRequires:	cargo make gcc-c++
Conflicts:		uutils-coreutils-replace
BuildRequires:  libselinux-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  clang-devel

%description
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

%package replace
Summary:		Cross-platform Rust replacement of the GNU coreutils
Conflicts:		coreutils
Provides:       coreutils
Provides:       coreutils(%arch)
Provides:       coreutils-full
Provides:       coreutils-single

%description replace
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

This package removes the `uu-` prefixes.

%prep
%autosetup -n coreutils-%version

%build
%make_build PROFILE=release SELINUX_ENABLED=1

%install
%make_install PROFILE=release MULTICALL=y DESTDIR=%buildroot PREFIX=%_prefix SELINUX_ENABLED=1 PROG_PREFIX=uu-
%make_install PROFILE=release MULTICALL=y DESTDIR=%buildroot PREFIX=%_prefix SELINUX_ENABLED=1

%define cmds() $(echo %1{runcon,arch,base{32,64,name,nc},cat,ch{grp,mod,own,root,con},cksum,comm,coreutils,cp,csplit,cut,date,dd,df,dir{,colors,name},du,echo,env,expand,expr,factor,false,fmt,fold,groups,hashsum,head,host{id,name},id,install,join,kill,link,ln,logname,ls,mk{dir,fifo,nod,temp},more,mv,nice,nl,nohup,nproc,numfmt,od,paste,pathchk,pinky,pr,printenv,printf,ptx,pwd,readlink,realpath,rm{,dir},seq,shred,shuf,sleep,sort,split,stat,stdbuf,sum,sync,tac,tail,tee,test,timeout,touch,tr,true,truncate,tsort,tty,uname,un{expand,iq,link},uptime,users,vdir,wc,who{,ami},yes}%2)
cat <<EOF > files.txt
%cmds %_bindir/uu- ""
%_bindir/uu-[
%cmds %_datadir/bash-completion/completions/uu- ""
%cmds %_datadir/fish/vendor_completions.d/uu- .fish
%cmds %_mandir/man1/uu- .1.gz
%cmds %_datadir/zsh/site-functions/_uu- ""
EOF
sed -i 's@ @\n@g' files.txt
# remove buildroot from paths in files.txt
sed -i "s@%buildroot@/@g" files.txt

cat <<EOF > files-replace.txt
%cmds %_bindir/ ""
%_bindir/[
%cmds %_datadir/bash-completion/completions/ ""
%cmds %_datadir/fish/vendor_completions.d/ .fish
%cmds %_mandir/man1/ .1.gz
%cmds %_datadir/zsh/site-functions/_ ""
EOF
sed -i 's@ @\n@g' files-replace.txt
# remove buildroot from paths in files.txt
sed -i "s@%buildroot@/@g" files-replace.txt

ln -r -s %buildroot/%_bindir/chroot %buildroot/usr/sbin/chroot


%files -f files.txt
/usr/sbin/chroot
%doc README.md
%license LICENSE

%files replace -f files-replace.txt
%doc README.md
%license LICENSE

%changelog
%autochangelog
