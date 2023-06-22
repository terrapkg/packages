Name:           anda-srpm-macros
Version:        0.1.3
Release:        2%{?dist}
Summary:        SRPM macros for extra Fedora packages

License:        MIT
# URL:
Source0:        macros.cargo_extra
Source1:        macros.caching
Source2:        macros.anda

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



%files
%{_rpmmacrodir}/macros.cargo_extra
%{_rpmmacrodir}/macros.caching
%{_rpmmacrodir}/macros.anda


%changelog
* Mon Sep 26 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.1.1-1
- Initial Build
