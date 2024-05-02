Name:			nushell
Version:		0.93.0
Release:		1%?dist
Summary:		A new type of shell
License:		MIT
URL:			https://www.nushell.sh/
Source0:		https://github.com/nushell/nushell/archive/refs/tags/%version.tar.gz
BuildRequires:	anda-srpm-macros rust-packaging openssl-devel
Requires:		glibc openssl zlib

%description
%summary.

%prep
%autosetup
%cargo_prep_online

%build
%{cargo_build -f extra,dataframe} --workspace

%install
mkdir -p %buildroot%_bindir
cp target/rpm/nu* %buildroot%_bindir/
rm -rf .cargo

%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/nu" > %{_sysconfdir}/shells
    echo "/bin/nu" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/nu$" %{_sysconfdir}/shells || echo "%{_bindir}/nu" >> %{_sysconfdir}/shells
    grep -q "^/bin/nu$" %{_sysconfdir}/shells || echo "/bin/nu" >> %{_sysconfdir}/shells
  fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/nu$!d' %{_sysconfdir}/shells
  sed -i '\!^/bin/nu$!d' %{_sysconfdir}/shells
fi

%files
%doc README.md
%license LICENSE
%_bindir/nu*

%changelog
%autochangelog
