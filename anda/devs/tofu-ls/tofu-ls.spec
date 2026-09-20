# https://github.com/opentofu/tofu-ls
%global goipath         github.com/opentofu/tofu-ls
Version:                0.5.3

%gometa -f

%global common_description %{expand:
OpenTofu language server, providing IDE features for OpenTofu files.}

%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md

Name:           tofu-ls
Release:        1%{?dist}
Summary:        Terraform language server
URL:            %{gourl}
Source:         %{gosource}
License:        MPL-2.0
BuildRequires:  go-rpm-macros
BuildRequires:  go-srpm-macros

Packager:       Cypress Reed <cypress@fyralabs.com>

%description %{common_description}

%gopkg

%prep
%autosetup -C
%goprep_online -A

%build
%gobuild -o %{gobuilddir}/bin/%{name} .

%install
%gopkginstall
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md CHANGELOG.md docs/
%{_bindir}/%{name}

%gopkgfiles

%changelog
* Fri Sep 18 2026 Cypress Reed <cypress@fyralabs.com>
- initial package
