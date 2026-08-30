%global debug_package %{nil}

Name:           tidal-hifi
Version:        8.1.3
Release:        2%?dist
Summary:        The web version of Tidal running in electron with hifi support thanks to widevine
%electronmeta
License:        MIT AND %electron_license
URL:            https://github.com/Mastermindzh/tidal-hifi
Source0:        %url/archive/refs/tags/%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>

BuildRequires:  nodejs-packaging

%description
The web version of TIDAL running in electron with Hi-Fi (High & Max) support thanks to widevine.

%prep
%autosetup

%build
%npm_build -r compile -BC ./build/electron-builder.base.yml

%install
%electron_install
%desktop_file_install packaging/aur/%{name}.desktop

# Do not ship an absolute symlink from /usr/bin.
rm -f %{buildroot}%{_bindir}/%{name}
ln -s ../%{_lib}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_appsdir}/%{name}.desktop
%{_bindir}/%{name}
%{_libdir}/%{name}

%changelog
* Sun Aug 30 2026 ammix <maxim@ammix.dev>
- Add desktop file

* Mon Aug 17 2026 madonuko <mado@fyralabs.com>
- Initial package
