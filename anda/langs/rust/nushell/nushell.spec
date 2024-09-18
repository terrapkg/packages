Name:			nushell
Version:		0.98.0
Release:		1%?dist
Summary:		A new type of shell
License:		MIT
URL:			https://www.nushell.sh/
BuildRequires:	anda-srpm-macros rust-packaging git-core
BuildRequires:  openssl-devel
Requires:		glibc openssl zlib

%description
%summary.

%prep
rm -rf ./*
git clone https://github.com/nushell/nushell -b %version --depth 1 .
%cargo_prep_online

%build
%{cargo_build} --workspace

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
