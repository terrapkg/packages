%bcond_without single

%bcond_without replace


%global coreutils_ver 9.3

Name:			uutils-coreutils
Version:		0.0.22
Release:		2%?dist
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

%if %{with replace}

%package replace
Summary:		Cross-platform Rust replacement of the GNU coreutils
Provides:       coreutils = %coreutils_ver
Provides:       coreutils(%arch)
Provides:       coreutils-full
Suggests:       uutils-coreutils-replace-bash-completion = %version-%release

%description replace
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

This package removes the `uu-` prefixes.

%package replace-bash-completion
Summary:		Bash completion for uutils coreutils
Requires:		uutils-coreutils = %version-%release
Provides:       bash-completion

%description replace-bash-completion
Bash completion for uutils coreutils

%endif

%if %{with single}

%package single
Summary:		Cross-platform Rust replacement of the GNU coreutils
Provides:       coreutils = %coreutils_ver
Provides:       coreutils(%arch)
Provides:       coreutils-full
Provides:       coreutils-single
Suggests:       bash-completion

%description single
uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust.
While all programs have been implemented, some options might be missing or different
behavior might be experienced.

This package provides a single binary symlinked to replace all coreutils.

%endif

%prep
%autosetup -n coreutils-%version
%global skip_utils "hostname kill more uptime"
%global cargo_flags "--verbose -F feat_selinux"
%build
export CARGOFLAGS=%cargo_flags
export SKIP_UTILS=%skip_utils
%make_build PROFILE=release SELINUX_ENABLED=1

%install
export CARGOFLAGS=%cargo_flags
export SKIP_UTILS=%skip_utils
sums=( 
    md5sum
    sha1sum
    sha224sum
    sha256sum
    sha384sum
    sha512sum
    b2sum
    b3sum
    sha3sum
    sha3sum
    sha3-224sum
    sha3-256sum
    sha3-384sum
    sha3-512sum
    shake128sum
    shake256sum
)

%define cmds() $(echo %1{runcon,arch,base{32,64,name,nc},cat,ch{grp,mod,own,root,con},cksum,comm,cp,csplit,cut,date,dd,df,dir{,colors,name},du,echo,env,expand,expr,factor,false,fmt,fold,groups,hashsum,head,host{id},id,install,join,link,ln,logname,ls,mk{dir,fifo,nod,temp},mv,nice,nl,nohup,nproc,numfmt,od,paste,pathchk,pinky,pr,printenv,printf,ptx,pwd,readlink,realpath,rm{,dir},seq,shred,shuf,sleep,sort,split,stat,stdbuf,sum,sync,tac,tail,tee,test,timeout,touch,tr,true,truncate,tsort,tty,uname,un{expand,iq,link},users,vdir,wc,who{,ami},yes}%2)


### files-replace

cat <<EOF > files-replace.txt
%cmds %_bindir/ ""
%_bindir/[
%cmds %_datadir/fish/vendor_completions.d/ .fish
%cmds %_mandir/man1/ .1.gz
%cmds %_datadir/zsh/site-functions/_ ""
EOF
sed -i 's@ @\n@g' files-replace.txt

cat <<EOF > files-replace-bash-completion.txt
%cmds %_datadir/bash-completion/completions/ ""
EOF
sed -i "s@%buildroot@/@g" files-replace-bash-completion.txt
sed -i 's@ @\n@g' files-replace-bash-completion.txt



# remove buildroot from paths in files.txt
sed -i "s@%buildroot@/@g" files-replace.txt

for sum in "${sums[@]}"; do
    ln -srvf %_bindir/hashsum "$RPM_BUILD_ROOT/%_bindir/$sum"
    echo "%_bindir/$sum" >> files-replace.txt
done

echo "=== Files (Replace) ==="
cat files-replace.txt





%if %{with single}
%make_install PROFILE=release MULTICALL=y DESTDIR=%buildroot PREFIX=%_prefix SELINUX_ENABLED=1 &
%endif

%if %{with replace}
%make_install PROFILE=release MULTICALL=n DESTDIR=%buildroot PREFIX=%_prefix SELINUX_ENABLED=1 &
%endif

## normal binary
%make_install PROFILE=release MULTICALL=n DESTDIR=%buildroot PREFIX=%_prefix SELINUX_ENABLED=1 PROG_PREFIX=uu- &
%define excludes() $(echo %1{hostname,kill,more,uptime}%2)
cat <<EOF > files.txt
%cmds %_bindir/uu- ""
%_bindir/uu-[
%cmds %_datadir/bash-completion/completions/uu- ""
%cmds %_datadir/fish/vendor_completions.d/uu- .fish
%cmds %_mandir/man1/uu- .1.gz
%cmds %_datadir/zsh/site-functions/_uu- ""
EOF
sed -i 's@ @\n@g' files.txt

# okay, let's symlink some hashsum binaries
for sum in "${sums[@]}"; do
    ln -srv uu-hashsum "$RPM_BUILD_ROOT/%_bindir/$sum"
    echo "%_bindir/$sum" >> files.txt
done

# remove buildroot from paths in files.txt
sed -i "s@%buildroot@/@g" files.txt

echo "=== Files ==="
cat files.txt

####


wait







#echo "=== Removing files ==="

#rm_filelist files-exclude.txt
#rm_filelist files-replace-exclude.txt

%files -f files.txt
%doc README.md
%license LICENSE

%if %{with single}
%files single -f files.txt
%doc README.md
%license LICENSE
%endif

%if %{with replace}
%files replace -f files-replace.txt
%doc README.md
%license LICENSE

%files replace-bash-completion -f files-replace-bash-completion.txt

%endif


%changelog
%autochangelog
