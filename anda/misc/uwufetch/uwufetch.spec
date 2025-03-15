Name:          uwufetch
Version:       
Release:       1%?dist
Summary:       A meme system info tool for Linux, based on nyan/uwu trend on r/linuxmasterrace.
License:       GPL-3.0
URL:           https://github.com/ad-oliviero/uwufetch
BuildRequires: make gcc git anda-srpm-macros

%description
A meme system info tool for (almost) all your Linux/Unix-based systems, based on the nyan/UwU trend on r/linuxmasterrace.

%prep
git clone https://github.com/TheDarkBug/uwufetch.git .
git checkout %{version}

%build
%make_build

%install
make install DESTDIR=%{?buildroot}%{_prefix}
mkdir %{?buildroot}%{_libdir}
mv %{?buildroot}%{_prefix}/lib/libfetch.so %{?buildroot}%{_libdir}/libfetch.so
rm -rf %{?buildroot}%{_includedir}

%files
%{_prefix}/lib/uwufetch/*
%{_libdir}/libfetch.so
%{_mandir}/man1/uwufetch.1.gz
%{_bindir}/uwufetch

%changelog
* Thu Jun 22 2023 Alyxia Sother <alyxia@riseup.net>
- Initial package.
