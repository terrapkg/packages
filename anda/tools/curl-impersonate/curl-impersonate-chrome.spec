%global build_cxxflags %(echo "%{__build_flags_lang_cxx} %{?_distro_extra_cxxflags}" | sed 's@-Werror=format-security@@')

Name:           curl-impersonate-chrome
Version:        0.7.0
Release:        1%{?dist}
Summary:        A series of patches that make curl requests look like Chrome

License:        MIT
URL:            https://github.com/lexiforest/curl-impersonate
Source0:        %{url}/archive/v%{version}.tar.gz
Patch0:         remove-werror-in-boringssl-build.patch
Patch1:         install-sh-scripts-to-buildroot.patch

Packager:       sadlerm <lerm@chromebooks.lol>

BuildRequires:  autoconf automake make cmake ninja-build
BuildRequires:  gcc gcc-c++ libtool
BuildRequires:  golang
BuildRequires:  unzip
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  zstd libzstd-devel

%global _description %{expand:
A special build of curl that can impersonate Chrome, Edge and Safari. curl-impersonate is able to perform TLS and HTTP handshakes that are identical to that of a real browser.

curl-impersonate can be used either as a command line tool, similar to the regular curl, or as a library that can be integrated instead of the regular libcurl.}

%description %_description


%package libs
Summary:        Shared libraries for %{name}
Provides:       libcurl-impersonate-chrome = %{version}-%{release}

%description libs
%_description

This package provides the libcurl-impersonate-chrome shared object file, which is libcurl compiled with the same changes as the curl-impersonate binary.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
%_description

This package contains the object files necessary to develop %{name}.


%prep
%autosetup -n curl-impersonate-%{version} -p1

%build
%configure
%{__make} chrome-build

%check
%{__make} chrome-checkbuild

%install
%{__make} DESTDIR=%{buildroot} chrome-install 

%files
%license LICENSE
%doc README.md docs/
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_bindir}/curl_*

%files libs
%license LICENSE
%{_prefix}/lib/libcurl-impersonate-chrome.so.4
%{_prefix}/lib/libcurl-impersonate-chrome.so.4.[0-9].[0-9]

%files devel
%{_prefix}/lib/libcurl-impersonate-chrome.a
%{_prefix}/lib/libcurl-impersonate-chrome.so

%changelog
* Sun Feb 23 2025 sadlerm <lerm@chromebooks.lol>
- Initial package
