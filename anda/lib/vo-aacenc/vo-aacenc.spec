Name:           vo-aacenc
Version:        0.1.3
Release:        1%{?dist}
Summary:        VisualOn AAC encoder library
License:        ASL 2.0
URL:            http://sourceforge.net/projects/opencore-amr/
Source0:        http://downloads.sourceforge.net/opencore-amr/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc

%description
This library contains an encoder implementation of the Advanced Audio
Coding (AAC) audio codec. The library is based on a codec implementation
by VisualOn as part of the Stagefright framework from the Google
Android project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING NOTICE
%doc ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/vo-aacenc.pc


%changelog
%autochangelog
