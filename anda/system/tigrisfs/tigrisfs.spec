%global goipath github.com/tigrisdata/tigrisfs
Version:        1.2.4

%gometa -f

Name:           tigrisfs
Release:        1%{?dist}
Summary:        High performance FUSE filesystem for AI workloads with S3 compatible backends

License:        Apache-2.0
URL:            https://github.com/tigrisdata/tigrisfs
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros

%description
%{summary}.

%gopkg

%prep
%autosetup -C

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/ %{goipath}/

%install
install -Dm755 %{gobuilddir}/tigrisfs       %{buildroot}%{_bindir}/tigrisfs
install -Dm644 pkg/tigrisfs@.service        %{buildroot}%{_unitdir}/tigrisfs@.service
install -Dm644 pkg/tigrisfs_user@.service   %{buildroot}%{_userunitdir}/tigrisfs_user@.service
install -Dm644 pkg/defaults                 %{buildroot}%{_sysconfdir}/default/tigrisfs

%post
%systemd_post tigrisfs@.service
%systemd_user_post tigrisfs_user@.service

%preun
%systemd_preun tigrisfs@.service
%systemd_user_preun tigrisfs_user@.service

%postun
%systemd_postun_with_restart tigrisfs@.service
%systemd_user_postun_with_restart tigrisfs_user@.service

%files
%license LICENSE Apache-2.0.txt LICENSE.geesefs
%doc README.md README-azure.md
%config(noreplace) %{_sysconfdir}/default/tigrisfs
%{_bindir}/tigrisfs
%{_unitdir}/tigrisfs@.service
%{_userunitdir}/tigrisfs_user@.service

%changelog
* Sat Oct 03 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
