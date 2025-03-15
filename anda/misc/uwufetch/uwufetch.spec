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
Source0:       %{url}/archive/%{commit}.tar.gz
BuildRequires: make gcc git anda-srpm-macros

%description
A meme system info tool for (almost) all your Linux/Unix-based systems, based on the nyan/UwU trend on r/linuxmasterrace.

%prep
%autosetup -n %{name)-%{commit}

%build
%make_build

%install
%make_install

%files
%{_libdir}/uwufetch/*
%{_libdir}/libfetch.so
%{_mandir}/man1/uwufetch.1.gz
%{_bindir}/uwufetch

%changelog
* Thu Jun 22 2023 Alyxia Sother <alyxia@riseup.net>
- Initial package.
