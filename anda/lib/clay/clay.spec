%global debug_package %{nil}

Name:           clay-devel
Version:        0.14
Release:        1%?dist
License:        Zlib
URL:            https://www.nicbarker.com/clay
Source:         https://github.com/nicbarker/clay/archive/refs/tags/v%version.tar.gz
Summary:        High performance UI layout library in C
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Clay (short for C Layout) is a high performance 2D UI layout library.
Major Features:

- Microsecond layout performance
- Flex-box like layout model for complex, responsive layouts including text wrapping, scrolling containers and aspect ratio scaling
- Single ~4k LOC clay.h file with zero dependencies (including no standard library)
- Wasm support: compile with clang to a 15kb uncompressed .wasm file for use in the browser
- Static arena based memory use with no malloc / free, and low total memory overhead (e.g. ~3.5mb for 8192 layout elements).
- React-like nested declarative syntax
- Renderer agnostic: outputs a sorted list of rendering primitives that can be easily composited in any 3D engine, and even compiled to HTML (examples provided)

%prep
%autosetup -n clay-%{version}

%build

%install
install -Dm644 clay.h %{buildroot}%{_includedir}/clay.h

%files
%license LICENSE.md
%doc README.md
%{_includedir}/clay.h

%changelog
* Wed Dec 31 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
