%global commit 9a34cc93c817f07be9b3540faa5d146c2a891e64
%global commit_date 20260915
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global appid com.system76.CosmicReader

Name:           cosmic-reader
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        %{sourcelicense} AND (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND AGPL-3.0 AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (MIT OR Apache-2.0 OR CC0-1.0) AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (MIT OR LGPL-3.0-or-later) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Summary:        WIP COSMIC PDF reader
URL:            https://github.com/pop-os/cosmic-reader
Source0:        %{url}/archive/%{commit}/server-%{commit}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  clang-libs
BuildRequires:  clang-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(gumbo)
BuildRequires:  pkgconfig(jbig2dec)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(lept)
BuildRequires:  pkgconfig(tesseract)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online
%cargo_license_summary_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm 755 target/rpm/%{name}                            %{buildroot}%{_bindir}/%{name}
install -Dm 644 res/icons/hicolor/128x128/apps/%{appid}.svg   %{buildroot}%{_scalableiconsdir}/%{appid}.svg
install -Dm 644 res/%{appid}.thumbnailer                      %{buildroot}%{_datadir}/thumbnailers/%{appid}.thumbnailer
%desktop_file_install res/%{appid}.desktop

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/%{appid}.svg
%{_datadir}/thumbnailers/%{appid}.thumbnailer

%changelog
* Sun Oct 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
