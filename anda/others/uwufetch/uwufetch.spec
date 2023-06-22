%define debug_package %nil

Name:			uwufetch
Version:		2.1
Release:		1%?dist
Summary:		A meme system info tool for Linux, based on nyan/uwu trend on r/linuxmasterrace. 
License:		GPL-3.0
URL:			https://github.com/TheDarkBug/uwufetch
BuildRequires:	make gcc git anda-srpm-macros
ExclusiveArch:	x86_64

%description
A meme system info tool for (almost) all your Linux/Unix-based systems, based on the nyan/UwU trend on r/linuxmasterrace.

%prep
git clone https://github.com/TheDarkBug/uwufetch.git .
git checkout %{version}

%build
%make_build

%install
make install DESTDIR=%{?buildroot}/usr
mkdir %{?buildroot}/usr/lib64
mv %{?buildroot}/usr/lib/libfetch.so %{?buildroot}/usr/lib64/libfetch.so
rm -rf %{?buildroot}/usr/include

%files
/usr/lib/uwufetch/*
%_libdir/libfetch.so
/usr/share/man/man1/uwufetch.1.gz
/usr/bin/uwufetch

%changelog
* Thu Jun 22 2023 Alyxia Sother <alyxia@riseup.net>
- Initial package.