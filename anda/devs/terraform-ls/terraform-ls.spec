# https://github.com/hashicorp/terraform-ls
%global goipath         github.com/hashicorp/terraform-ls
Version:                0.39.0

%gometa -f

%global common_description %{expand:
Terraform language server, providing IDE features for Terraform files.}

%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md

Name:           terraform-ls
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
