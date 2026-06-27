%undefine __brp_mangle_shebangs
%define debug_package %nil
%global         __strip /bin/true

Name:           tracktion-waveform
Version:        13.5.13
Packager:       Cappy Ishihara <cappy@fyralabs.com>
Release:        1%{?dist}
Summary:        Tracktion Waveform DAW
ExclusiveArch:  x86_64 aarch64
%global majver %(echo %{version} | cut -d '.' -f 1)
%global truncated_ver %(echo %{version} | tr -d .)

%ifarch x86_64
%global pkgarch amd64
%endif

%ifarch aarch64
%global pkgarch arm64
%endif

License:        Proprietary
URL:            https://www.tracktion.com/products/waveform-free
Source0:        https://downloads.tracktion.com/w%{majver}/%{truncated_ver}b/waveform%{majver}_%{version}_%{pkgarch}.deb

BuildRequires:  tar
BuildRequires:  binutils

%description
%{summary}

%prep
%autosetup -Tc

ar x %{SOURCE0}
%install
tar xvf data.tar.gz -C %{buildroot}
export QA_RPATHS="[0-7]"

%files
%{_bindir}/Waveform%{majver}
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/waveform13.xml
%{_datadir}/applications/waveform13.desktop
%{_docdir}/Waveform%{majver}/*



%changelog
* Tue Oct 07 2025 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
