%undefine __brp_add_determinism

Name:           amdgpu_top
Version:        0.11.2
Release:        1%?dist
Summary:        Tool to display AMDGPU usage
License:        MIT
Packager:       veuxit <erroor234@gmail.com>
URL:            https://github.com/Umio-Yasuno/amdgpu_top

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  libdrm-devel
BuildRequires:  cargo cargo-rpm-macros anda-srpm-macros

%description
%summary.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%{cargo_build} --locked

%install

install -Dm755 target/release/amdgpu_top %{buildroot}%{_bindir}/amdgpu_top

install -Dm644 assets/amdgpu_top.desktop %{buildroot}%{_appsdir}/amdgpu_top.desktop

install -Dm644 assets/amdgpu_top-tui.desktop %{buildroot}%{_appsdir}/amdgpu_top-tui.desktop

install -Dpm644 assets/io.github.umio_yasuno.amdgpu_top.metainfo.xml %{buildroot}%{_metainfodir}/io.github.umio_yasuno.amdgpu_top.metainfo.xml

install -Dm644 "docs/amdgpu_top.1" "%{buildroot}%{_mandir}/man1/amdgpu_top.1"

%check
%desktop_file_validate %{buildroot}%{_appsdir}/amdgpu_top.desktop
%desktop_file_validate %{buildroot}%{_appsdir}/amdgpu_top-tui.desktop

%files
%doc README.md
%doc CHANGELOG.md
%doc AUTHORS
%license LICENSE
%{_bindir}/amdgpu_top
%{_datadir}/applications/amdgpu_top.desktop
%{_datadir}/applications/amdgpu_top-tui.desktop
%{_metainfodir}/io.github.umio_yasuno.amdgpu_top.metainfo.xml
%{_mandir}/man1/amdgpu_top.1.gz

%changelog
* Thu Mar 5 2026 veuxit <erroor234@gmail.com> - 0.11.2
- Initial package release