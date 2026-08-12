%global appid dev.edfloreshz.Tasks

Name:           cosmic-ext-tasks
Version:        0.3.1
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND GPL-3.0-only AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        A simple task management application for the COSMIC desktop
URL:            https://github.com/cosmic-utils/tasks
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-osd
Requires:       hicolor-icon-theme
Provides:       cosmic-tasks
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/tasks                                %{buildroot}%{_bindir}/tasks
install -Dm0644 res/%{appid}.desktop                            %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 res/%{appid}.metainfo.xml                       %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 res/icons/hicolor/scalable/apps/%{appid}.svg    %{buildroot}%{_scalableiconsdir}/%{appid}.svg

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/tasks
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Sun Aug 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
