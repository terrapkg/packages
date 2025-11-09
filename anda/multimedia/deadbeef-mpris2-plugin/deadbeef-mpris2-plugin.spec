#? https://github.com/rpmfusion/deadbeef-mpris2-plugin/

Name:           deadbeef-mpris2-plugin
Version:        1.16
Release:        1%{?dist}
Summary:        MPRISv2 plugin for the DeaDBeeF music player

License:        GPLv2+
URL:            https://github.com/DeaDBeeF-Player/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Build for armv7hl failed
# https://github.com/DeaDBeeF-Player/deadbeef/issues/2538
ExcludeArch:    armv7hl

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib2-devel
BuildRequires:  deadbeef-devel

Requires:       deadbeef%{?_isa}

%description
This plugin aims to implement the MPRISv2 for DeaDBeeF.

The original MPRIS plugin for DeaDBeef does not work anymore and seems
to be orphaned. The original plugin supported MPRISv1 AND MPRISv2. This plugin
will only support version two.

%prep
%autosetup
autoreconf -fiv


%build
%configure \
 --disable-silent-rules \
 --disable-static
%{make_build}


%install
%{make_install}
rm %{buildroot}%{_libdir}/deadbeef/mpris.*a


%files
%doc README
%license LICENSE
%{_libdir}/deadbeef/mpris.*
