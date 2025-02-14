%global coreutils_ver 9.3
%if 0%{?fedora} >= 42
### Temporary solution, will be fixed on newer Oniguruma releases.
%global build_cflags %{__build_flags_lang_c} %{?_distro_extra_cflags} -std=c18 -std=gnu18
%endif

Name:           uutils-coreutils-replace
Version:        0.0.29
Release:        2%?dist
Summary:        Cross-platform Rust rewrite of the GNU coreutils
License:        MIT
URL:            https://github.com/uutils/coreutils
Source0:        %url/archive/refs/tags/%version.tar.gz
Source1:        https://src.fedoraproject.org/rpms/coreutils/raw/rawhide/f/coreutils-colorls.sh
Source2:        https://src.fedoraproject.org/rpms/coreutils/raw/rawhide/f/coreutils-colorls.csh
Source3:        https://raw.githubusercontent.com/coreutils/coreutils/refs/heads/master/src/dircolors.hin
Patch0:         coreutils-fix-metadata.diff
Patch1:         coreutils-fix-seq-neg-num-tests.diff
Patch3:         https://src.fedoraproject.org/rpms/coreutils/raw/rawhide/f/coreutils-8.32-DIR_COLORS.patch
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo
BuildRequires:  clang-devel
BuildRequires:  gcc-c++
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  rustfmt
BuildRequires:  selinux-policy-devel
Requires:       glibc
Provides:       coreutils
Provides:       coreutils-common
Conflicts:      uutils-coreutils

%description
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

This package replaces the GNU coreutils commands.


%prep
%setup -q -n coreutils-%version
%cargo_prep_online
/usr/bin/cp %{SOURCE3} .
sed dircolors.hin \
        -e 's| 00;36$| 01;36|' \
        > DIR_COLORS
sed dircolors.hin \
        -e 's| 01;31$| 00;31|' \
        -e 's| 01;35$| 00;35|' \
        > DIR_COLORS.lightbgcolor
%autopatch -p1

%build

%install
install -p -c -Dm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/colorls.sh
install -p -c -Dm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/colorls.csh
install -p -c -Dm644 DIR_COLORS{,.lightbgcolor} %{buildroot}%{_sysconfdir}
/usr/bin/rm dircolors.hin DIR_COLORS DIR_COLORS.lightbgcolor
%make_install PROFILE_CMD='--profile=rpm' MULTICALL=n DESTDIR=%buildroot BUILDDIR=target/rpm PREFIX=%_prefix SELINUX_ENABLED=1 SKIP_UTILS='hostname kill more uptime' &
wait
/usr/bin/ln -sf hashsum %{buildroot}%{_bindir}/b2sum
/usr/bin/ln -sf hashsum %{buildroot}%{_bindir}/md5sum
/usr/bin/ln -sf hashsum %{buildroot}%{_bindir}/sha1sum
/usr/bin/ln -sf hashsum %{buildroot}%{_bindir}/sha224sum
/usr/bin/ln -sf hashsum %{buildroot}%{_bindir}/sha256sum
/usr/bin/ln -sf hashsum %{buildroot}%{_bindir}/sha384sum
/usr/bin/ln -sf hashsum %{buildroot}%{_bindir}/sha512sum

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
%{_bindir}/b2sum
%{_bindir}/md5sum
%{_bindir}/sha1sum
%{_bindir}/sha224sum
%{_bindir}/sha256sum
%{_bindir}/sha384sum
%{_bindir}/sha512sum
%config(noreplace) %{_sysconfdir}/DIR_COLORS
%config(noreplace) %{_sysconfdir}/DIR_COLORS.lightbgcolor
%{_sysconfdir}/profile.d/colorls.sh
%{_sysconfdir}/profile.d/colorls.csh



%changelog
%autochangelog
