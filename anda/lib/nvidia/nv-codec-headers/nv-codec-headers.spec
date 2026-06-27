Name:           nv-codec-headers
Version:        13.0.19.0
Release:        1%?dist
Summary:        FFmpeg version of Nvidia Codec SDK headers
License:        MIT
URL:            https://github.com/FFmpeg/nv-codec-headers
BuildArch:      noarch
       
Source0:        %url/archive/n%{version}/%{name}-n%{version}.tar.gz

BuildRequires:  make

%description
FFmpeg version of headers required to interface with Nvidias codec APIs.

%prep
%autosetup -n %{name}-n%{version}
sed -i -e 's@/include@/include/ffnvcodec@g' ffnvcodec.pc.in

# Extract license
sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE
sed -i '1,22s/^.\{,3\}//' LICENSE

%build
%make_build PREFIX=%{_prefix} LIBDIR=/share

%install
%make_install PREFIX=%{_prefix} LIBDIR=/share

%files
%doc README
%license LICENSE
%{_includedir}/ffnvcodec/
%{_datadir}/pkgconfig/ffnvcodec.pc

%changelog
%autochangelog
