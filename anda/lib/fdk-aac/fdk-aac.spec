Name:           fdk-aac
Version:        2.0.3
Release:        1%{?dist}
Summary:        Fraunhofer FDK Advanced Audio Coding Codec Library
License:        Software License for The Fraunhofer FDK AAC Codec Library for Android
URL:            http://sourceforge.net/projects/opencore-amr/
Source0:        https://github.com/mstorsjo/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Provides:       fdk-aac = %{version}-%{release}
Provides:       fdk-aac%{?_isa} = %{version}-%{release}
Obsoletes:      fdk-aac < %{version}-%{release}
Provides:       fdk-aac-free = %{version}-%{release}
Provides:       fdk-aac-free%{?_isa} = %{version}-%{release}
Obsoletes:      fdk-aac-free < %{version}-%{release}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
Fraunhofer FDK Advanced Audio Coding Codec Library for Android.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       fdk-aac-devel = %{version}-%{release}
Provides:       fdk-aac-devel%{?_isa} = %{version}-%{release}
Obsoletes:      fdk-aac-devel < %{version}-%{release}
Provides:       fdk-aac-free-devel = %{version}-%{release}
Provides:       fdk-aac-free-devel%{?_isa} = %{version}-%{release}
Obsoletes:      fdk-aac-free-devel < %{version}-%{release}

%description    devel
This package contains libraries and header files for developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%files
%license NOTICE
%doc ChangeLog
%{_libdir}/lib%{name}*.so.*

%files devel
%doc documentation/*
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/fdk-aac.pc

%changelog
%autochangelog
