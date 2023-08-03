Name:           anda-srpm-macros
Version:        0.1.4
Release:        1%{?dist}
Summary:        SRPM macros for extra Fedora packages

License:        MIT
# URL:
Source0:        macros.cargo_extra
Source1:        macros.caching
Source2:        macros.anda
Source3:        macros.go_extra

Recommends:     rust-packaging
Requires:       git-core
Obsoletes:      fyra-srpm-macros < 0.1.1-1
Provides:       fyra-srpm-macros = %{version}-%{release}
BuildArch:      noarch

%description
%{summary}

%prep

%build

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE0}
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE1}
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE2}
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE3}

%files
%{_rpmmacrodir}/macros.cargo_extra
%{_rpmmacrodir}/macros.caching
%{_rpmmacrodir}/macros.anda
%{_rpmmacrodir}/macros.go_extra


%changelog
* Thu Aug 3 2023 madonuko <mado@fyralabs.com> - 0.1.4-1
- Add go_build_online and go_prep_online

* Mon Sep 26 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.1.1-1
- Initial Build
