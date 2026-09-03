%global ver 0.1.0
%global commitdate 20260723
%global commit 0ba27cc2caac19acb7a8d98747f8b65058dab877
%global shortcommit %{sub %{commit} 0 7}
%global appid com.cosmic.ext.Storage

Name:           cosmic-ext-applet-sysinfo
Version:        %{ver}^%{commitdate}.git%{shortcommit}
Release:        1%{?dist}
Summary:        A Disk Utility for the Comsic Desktop

SourceLicense:  GPL-3.0-only
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND LGPL-2.1 AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)

URL:            https://github.com/cosmic-utils/cosmic-ext-storage
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  clang-devel
BuildRequires:  gcc-c++
BuildRequires:  libbtrfsutil
Requires:       udisks2
Recommends:     exfatprogs
Recommends:     dosfstools
Suggests:       rclone
Suggests:       e2fsprogs
Suggests:       xfsprogs
Suggests:       btrfs-prog
Suggests:       exfatprogs
Suggests:       ntfsprogs

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online
%cargo_license_summary_online

%build
export VERGEN_GIT_SHA=%{commit}
export VERGEN_GIT_COMMIT_DATE=%{commitdate}
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/cosmic-ext-storage                                       %{buildroot}%{_bindir}/cosmic-ext-storage
install -Dm0644 resources/app.desktop                                               %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 resources/app.metainfo.xml                                          %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
install -Dm0644 resources/icons/hicolor/scalable/apps/com.cosmic.ext.Storage.svg    %{buildroot}%{_scaleableiconsdir}/%{appid}.svg

%files
%license LICENSE LICENSE.dependencies
%doc README.md docs/*
%{_bindir}/cosmic-ext-storage
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scaleableiconsdir}/%{appid}.svg

%changelog
* Wed Sep 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
