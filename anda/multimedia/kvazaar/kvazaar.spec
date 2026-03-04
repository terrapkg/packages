Name:           kvazaar
Version:        2.3.1
Release:        2%{?dist}
Summary:        An open-source HEVC encoder
License:        BSD and ISC
URL:            https://ultravideo.fi/kvazaar.html

Source0:        https://github.com/ultravideo/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  yasm

%description
Kvazaar is the leading academic open-source HEVC encoder developed from scratch
in C. This package contains the application for encoding videos.

%package        libs
Summary:        HEVC encoder %{name} libraries

%description    libs
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}. This package contains the shared libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure --enable-static=no
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

# Pick up docs in the files section
rm -fr %{buildroot}%{_docdir}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%files libs
%license LICENSE*
%doc README.md CREDITS
%{_libdir}/lib%{name}.so.7
%{_libdir}/lib%{name}.so.7.4.0

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
