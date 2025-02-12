%global coreutils_ver 9.3
### Temporary solution, will be fixed on newer Oniguruma releases.
%global build_cflags %{__build_flags_lang_c} %{?_distro_extra_cflags} -std=c18 -std=gnu18

Name:		uutils-coreutils-replace
Version:	0.0.29
Release:	2%?dist
Summary:	Cross-platform Rust rewrite of the GNU coreutils
License:	MIT
URL:		https://github.com/uutils/coreutils
Source0:	%url/archive/refs/tags/%version.tar.gz
Patch0:         coreutils-fix-metadata.diff
Patch1:         coreutils-fix-seq-neg-num-tests.diff
BuildRequires:	cargo
BuildRequires:  clang-devel
BuildRequires:	gcc-c++
BuildRequires:  libselinux-devel
BuildRequires:	make
BuildRequires:  rustfmt
BuildRequires:  selinux-policy-devel
Requires:	glibc
Provides:       coreutils
Provides:       coreutils-common
Conflicts:      uutils-coreutils

%description
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

This package replaces the GNU coreutils commands.


%prep
%autosetup -n coreutils-%version -p1

%build
export CARGOFLAGS="-vv --verbose"
%make_build PROFILE=release SELINUX_ENABLED=1 SKIP_UTILS='hostname kill more uptime'

%install
%make_install PROFILE=release MULTICALL=n DESTDIR=%buildroot PREFIX=%_prefix SELINUX_ENABLED=1 SKIP_UTILS='hostname kill more uptime' &
wait
ln -sr hashsum %{buildroot}%{_bindir}/sha1sum
ln -sr hashsum %{buildroot}%{_bindir}/sha224sum
ln -sr hashsum %{buildroot}%{_bindir}/sha256sum
ln -sr hashsum %{buildroot}%{_bindir}/sha384sum
ln -sr hashsum %{buildroot}%{_bindir}/sha512sum
ln -sr hashsum %{buildroot}%{_bindir}/sha3-224sum
ln -sr hashsum %{buildroot}%{_bindir}/sha3-256sum
ln -sr hashsum %{buildroot}%{_bindir}/sha3-384sum
ln -sr hashsum %{buildroot}%{_bindir}/sha3-512sum
ln -sr hashsum %{buildroot}%{_bindir}/sha3sum
ln -sr hashsum %{buildroot}%{_bindir}/shake128sum
ln -sr hashsum %{buildroot}%{_bindir}/shake256sum

%define cmds() $(echo %1{runcon,arch,base{32,64,name,nc},cat,ch{grp,mod,own,root,con},cksum,comm,cp,csplit,cut,date,dd,df,dir{,colors,name},du,echo,env,expand,expr,factor,false,fmt,fold,groups,hashsum,head,host{id},id,install,join,link,ln,logname,ls,mk{dir,fifo,nod,temp},mv,nice,nl,nohup,nproc,numfmt,od,paste,pathchk,pinky,pr,printenv,printf,ptx,pwd,readlink,realpath,rm{,dir},seq,shred,shuf,sleep,sort,split,stat,stdbuf,sum,sync,tac,tail,tee,test,timeout,touch,tr,true,truncate,tsort,tty,uname,un{expand,iq,link},users,vdir,wc,who{,ami},yes}%2)
cat <<EOF > files.txt
%cmds %_bindir/ ""
%_bindir/[
%cmds %_datadir/bash-completion/completions/ ""
%cmds %_datadir/fish/vendor_completions.d/ .fish
%cmds %_mandir/man1/ .1.gz
%cmds %_datadir/zsh/site-functions/_ ""
EOF
sed -i 's@ @\n@g' files.txt

# remove buildroot from paths in files.txt
sed -i "s@%buildroot@/@g" files.txt


echo "=== Files ==="
cat files.txt

%files -f files.txt
%doc README.md
%license LICENSE
%{_bindir}/sha1sum
%{_bindir}/sha224sum
%{_bindir}/sha256sum
%{_bindir}/sha384sum
%{_bindir}/sha512sum
%{_bindir}/sha3-224sum
%{_bindir}/sha3-256sum
%{_bindir}/sha3-384sum
%{_bindir}/sha3-512sum
%{_bindir}/sha3sum
%{_bindir}/shake128sum
%{_bindir}/shake256sum


%changelog
%autochangelog
