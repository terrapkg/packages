Name:           anda-srpm-macros
Version:        0.1.8
Release:        1%?dist
Summary:        SRPM macros for extra Fedora packages

License:        MIT
URL:            https://github.com/terrapkg/srpm-macros
Source0:        %url/archive/refs/tags/v%{version}.tar.gz

Recommends:     rust-packaging
Requires:       git-core
Obsoletes:      fyra-srpm-macros < 0.1.1-1
Provides:       fyra-srpm-macros = %{version}-%{release}
BuildArch:      noarch

%description
%{summary}

%prep
%autosetup -n srpm-macros-%version

%build

%install
for file in ./macros.*; do
    install -Dpm644 -t %buildroot%_rpmmacrodir $file
done

%files
%{_rpmmacrodir}/macros.anda
%{_rpmmacrodir}/macros.caching
%{_rpmmacrodir}/macros.cargo_extra
%{_rpmmacrodir}/macros.go_extra
%{_rpmmacrodir}/macros.nim_extra


%changelog
* Wed Aug 14 2024 madonuko <mado@fyralabs.com> - 0.1.7-2
- Move sources outside of packages repo

* Wed Mar 13 2024 madonuko <mado@fyralabs.com> - 0.1.6-1
- Add nim_c, nim_tflags and nim_lflags

* Thu Aug 3 2023 madonuko <mado@fyralabs.com> - 0.1.4-1
- Add go_build_online and go_prep_online

* Mon Sep 26 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.1.1-1
- Initial Build
