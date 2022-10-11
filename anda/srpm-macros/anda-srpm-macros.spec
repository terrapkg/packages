Name:           anda-srpm-macros
Version:        0.1.2
Release:        2%{?dist}
Summary:        SRPM macros for extra Fedora packages

License:        MIT
# URL:
Source0:        macros.cargo_extra
Source1:        macros.caching

Recommends:     rust-packaging
Obsoletes:      fyra-srpm-macros < 0.1.1-1
Provides:       fyra-srpm-macros
BuildArch:      noarch
%description
%{summary}

%prep


%build

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE0}
install -D -p -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE1}



%files
%{_rpmmacrodir}/macros.cargo_extra
%{_rpmmacrodir}/macros.caching


%changelog
* Mon Sep 26 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Build
