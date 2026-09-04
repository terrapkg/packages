# https://github.com/yorukot/superfile
%global goipath         github.com/yorukot/superfile
Version:                1.6.0

%gometa -f

%global common_description %{expand:
Pretty fancy and modern terminal file manager.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           superfile
Release:        1%{?dist}
Summary:        Pretty fancy and modern terminal file manager

License:        MIT
URL:            https://github.com/yorukot/superfile
Source:         %{gosource}
Packager:       Caio Bruno <cbrunofb@gmail.com>

%description %{common_description}

%gopkg

%prep
%goprep -A

%build
%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/spf %{goipath}

%install
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/spf %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/spf

%changelog
* Thu Jul 30 2026 Caio Bruno <cbrunofb@gmail.com>
- Initial package
