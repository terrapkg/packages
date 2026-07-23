%global goipath github.com/HikariKnight/ls-iommu
Version:        2.3.0

%gometa -f

Name:           ls-iommu
Release:        1%?dist
Summary:        A tool to list devices in iommu groups, useful for setting up VFIO

License:        MIT
URL:            https://github.com/HikariKnight/ls-iommu
Source0:        %url/archive/refs/tags/%version.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang gcc go-rpm-macros

%description
%{summary}.

%gopkg

%prep
%goprep

%build
%define gomodulesmode GO111MODULE=on
%gobuild -ldflags="-X github.com/HikariKnight/ls-iommu/internal/version.Version=%version" -o ls-iommu ./cmd

%install
install -Dm 0755 ls-iommu %{buildroot}%{_bindir}/ls-iommu

%files
%license LICENSE
%doc README.md
%{_bindir}/ls-iommu

%changelog
* Sun Dec 21 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
