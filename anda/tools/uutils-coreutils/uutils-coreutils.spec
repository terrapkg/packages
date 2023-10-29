%global coreutils_ver 9.3

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
Provides:       coreutils = %coreutils_ver
Provides:       coreutils(%arch)
Provides:       coreutils-full

%description replace
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

This package removes the `uu-` prefixes.

%package single
Summary:		uutils-coreutils single binary
%description single
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

This package provides a single binary with all commands.

%package single-replace
Summary:		uutils-coreutils single binary, replaces coreutils
Provides:       coreutils-single = %coreutils_ver
Provides:       coreutils-single(%arch)

%description single-replace
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

This package provides a single binary with all commands, and replaces the GNU coreutils.

%prep
%autosetup -n coreutils-%version

%build
export CARGOFLAGS="-vv --verbose"
%make_build PROFILE=release SELINUX_ENABLED=1

%install
%make_install PROFILE=release MULTICALL=y DESTDIR=%buildroot PREFIX=%_prefix SELINUX_ENABLED=1 PROG_PREFIX=uu- &
%make_install PROFILE=release MULTICALL=y DESTDIR=%buildroot PREFIX=%_prefix SELINUX_ENABLED=1 &
wait

%define cmds() $(echo %1{runcon,arch,base{32,64,name,nc},cat,ch{grp,mod,own,root,con},cksum,comm,cp,csplit,cut,date,dd,df,dir{,colors,name},du,echo,env,expand,expr,factor,false,fmt,fold,groups,hashsum,head,host{id},id,install,join,link,ln,logname,ls,mk{dir,fifo,nod,temp},mv,nice,nl,nohup,nproc,numfmt,od,paste,pathchk,pinky,pr,printenv,printf,ptx,pwd,readlink,realpath,rm{,dir},seq,shred,shuf,sleep,sort,split,stat,stdbuf,sum,sync,tac,tail,tee,test,timeout,touch,tr,true,truncate,tsort,tty,uname,un{expand,iq,link},users,vdir,wc,who{,ami},yes}%2)
%define excludes() $(echo %exclude %1{hostname,kill,more,uptime}%2)
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

cat <<EOF > files-exclude.txt
%excludes %_datadir/bash-completion/completions/uu- ""
%excludes %_datadir/fish/vendor_completions.d/uu- .fish
%excludes %_mandir/man1/uu- .1.gz
%excludes %_datadir/zsh/site-functions/_uu- ""
EOF
sed -i 's@ @\n@g' files-exclude.txt
# remove the excluded files

for i in $(cat files-exclude.txt); do
    ls $i
    rm -vf $i
done


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

cat <<EOF > files-remove-replace.txt
%excludes %_datadir/bash-completion/completions/ ""
%excludes %_datadir/fish/vendor_completions.d/ .fish
%excludes %_mandir/man1/ .1.gz
%excludes %_datadir/zsh/site-functions/_ ""
EOF
sed -i 's@ @\n@g' files-remove-replace.txt
# remove the excluded files
for i in $(cat files-remove-replace.txt); do
    ls $i
    rm -vf $i
done


%files -f files.txt
%doc README.md
%license LICENSE

%files replace -f files-replace.txt
%doc README.md
%license LICENSE

%files single
%_bindir/uu-coreutils
%doc README.md
%license LICENSE

%files single-replace
%_bindir/coreutils
%doc README.md

%changelog
%autochangelog
