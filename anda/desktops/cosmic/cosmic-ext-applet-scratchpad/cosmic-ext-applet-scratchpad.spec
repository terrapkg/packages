%global appid io.github.hasmolam.cosmic-ext-applet-scratchpad

Name:           cosmic-ext-applet-scratchpad
Version:        0.1.0
Release:        1%{?dist}
SourceLicense:  GPL-3.0-only
License:        %{sourcelicense} AND Apache-2.0 AND (0BSD OR MIT OR Apache-2.0) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT) AND MIT AND CC0-1.0 AND Unlicense AND BSD-2-Clause AND (Apache-2.0 OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND BSL-1.0 AND (MIT OR LGPL-3.0-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND Zlib AND MPL-2.0 AND Unicode-3.0 AND ISC AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Apache-2.0 OR GPL-2.0-only) AND BSD-3-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND GPL-3.0-or-later
Summary:        Minimalist quick notes and scratchpad applet for the COSMIC Desktop
URL:            https://github.com/Hasmolam/cosmic-ext-applet-scratchpad
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{appid}.metainfo.xml
BuildRequires:  cargo-rpm-macros
BuildRequires:  anda-srpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  terra-appstream-helper
Packager:       Leo Douglas <douglarek@gmail.com>

%description
Minimalist quick notes and scratchpad applet for the COSMIC desktop. It
provides immediate access to three separate scratchpads (Notes, Snippets,
Scratch) from the COSMIC panel. Notes are stored as plain Markdown files
under $XDG_DATA_HOME/cosmic-scratchpad/ with atomic writes, debounced
auto-save, one-click copy, a non-destructive clear with undo, and word and
character counters.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm0755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm0644 data/%{appid}.desktop %{buildroot}%{_appsdir}/%{appid}.desktop
install -Dm0644 data/icons/scalable/apps/%{appid}-symbolic.svg %{buildroot}%{_scalableiconsdir}/%{appid}-symbolic.svg
%terra_appstream %{S:1}

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}-symbolic.svg

%changelog
* Sat Sep 26 2026 Leo Douglas <douglarek@gmail.com> - 0.1.0-1
- Initial package
