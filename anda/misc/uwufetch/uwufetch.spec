%global commit 28b471b813d1c9aab77eeeb61f65304e586fb275
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240423
%global ver 2.1
%global debug_package %{nil}

Name:          uwufetch
Version:       %{ver}^%{commit_date}git.%{shortcommit}
Release:       1%?dist
Summary:       A meme system info tool for Linux, based on nyan/uwu trend on r/linuxmasterrace.
License:       GPL-3.0
URL:           https://github.com/ad-oliviero/uwufetch
BuildRequires: make gcc git anda-srpm-macros
Requires:      freecolor
Requires:      xwininfo
Recommends:    lshw

%description
A meme system info tool for (almost) all your Linux/Unix-based systems, based on the nyan/UwU trend on r/linuxmasterrace.

%package       devel
Summary:       Development files for UwUFetch.
Requires:      %{name}

%description   devel
This package contains delevoplent files for UwUFetch.

%prep
%git_clone %{url} %{commit}

%build
%make_build

%install
%make_install DESTDIR=%{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/libfetch.so %{buildroot}%{_libdir}/libfetch.so

%files
%doc CODE_OF_CONDUCT.md
%doc README.md
%license LICENSE
%license res/COPYRIGHT.md
%dir %{_prefix}/lib/uwufetch
%{_prefix}/lib/uwufetch/*
%{_mandir}/man1/uwufetch.1.gz
%{_bindir}/uwufetch

%files devel
%{_libdir}/libfetch.so
%{_includedir}/fetch.h

%changelog
* Thu Jun 22 2023 Alyxia Sother <alyxia@riseup.net>
- Initial package.
