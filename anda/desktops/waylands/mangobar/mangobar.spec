%global commit e5e8e35953c03e07e163a4967feda7af6aba7803
%global commit_date 20260509
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mangobar
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        A suckless-esc bar for mangowc
URL:            https://github.com/Gur0v/mangobar
Source0:        %{url}/archive/%{commit}/mangobar-%{commit}.tar.gz
SourceLicense:  GPL-3.0-or-later
License:        %{sourcelicense} AND (Apache-2.0 OR MIT) AND MIT AND GPL-3.0 AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Unlicense OR MIT)

BuildRequires:  rust
BuildRequires:  cargo-rpm-macros
BuildRequires:  gtk4
BuildRequires:  gtk4-devel
BuildRequires:  gtk4-layer-shell
BuildRequires:  gtk4-layer-shell-devel
BuildRequires:  gdk-pixbuf2
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  wireplumber

Suggests: mangowm
Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n mangobar-%{commit}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm 755 target/rpm/mangobar %{buildroot}%{_bindir}/mangobar
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/mangobar
%license LICENSE
%license LICENSE.dependencies
%doc README.md

%changelog
* Sat May 23 2026 Its-J <jonah@fyralabs.com>
- Package mangobar
