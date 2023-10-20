Name:			uutils-coreutils
Version:		0.0.22
Release:		1%?dist
Summary:		Cross-platform Rust rewrite of the GNU coreutils
License:		MIT
URL:			https://github.com/uutils/coreutils
Source0:		%url/archive/refs/tags/%version.tar.gz
Requires:		glibc gcc-devel
BuildRequires:	cargo make gcc-c++
#Conflicts:		coreutils
#Provides:		coreutils
BuildRequires:  libselinux-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  clang-devel

%description
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

%prep
%autosetup -n coreutils-%version

%build
%make_build PROFILE=release SELINUX_ENABLED=1

%install
%make_install PROFILE=release MULTICALL=y PROG_PREFIX=uu- DESTDIR=%buildroot PREFIX=%_prefix SELINUX_ENABLED=1

%define cmds() $(echo %1{arch,base{32,64,name,nc},cat,ch{grp,mod,own,root},cksum,comm,coreutils,cp,csplit,cut,date,dd,df,dir{,colors,name},du,echo,env,expand,expr,factor,false,fmt,fold,groups,hashsum,head,host{id,name},id,install,join,kill,link,ln,logname,ls,mk{dir,fifo,nod,temp},more,mv,nice,nl,nohup,nproc,numfmt,od,paste,pathchk,pinky,pr,printenv,printf,ptx,pwd,readlink,realpath,rm{,dir},seq,shred,shuf,sleep,sort,split,stat,stdbuf,sum,sync,tac,tail,tee,test,timeout,touch,tr,true,truncate,tsort,tty,uname,un{expand,iq,link},uptime,users,vdir,wc,who{,ami},yes}%2)
cat <<EOF > files.txt
%cmds %_bindir/uu- ""
"%_bindir/uu-["
%cmds %_datadir/bash-completion/completions/uu- ""
%cmds %_datadir/fish/vendor_completions.d/uu- .fish
%dnl %cmds %_mandir/man1/uu- .1
%cmds %_datadir/zsh/site-functions/_uu- ""
EOF
sed -i 's@ @\n@g' files.txt
# remove buildroot from paths in files.txt
sed -i "s@%buildroot@/@g" files.txt
cat files.txt

%files -f files.txt
%doc README.md
%license LICENSE

%changelog
%autochangelog
