%global debug_package %{nil}

Name:           spot
Release:        1%{?dist}
Version:        0.3.0
Summary:        Presenter spotlight overlay for Linux — pure x86_64 assembly
License:        Unlicense
URL:            https://github.com/isene/spot
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  nasm
BuildRequires:  make
Packager:       Owen Zimmerman <owen@fyralabs.com>
ExclusiveArch:  x86_64
Conflicts:      adobe-afdko

%description
Presenter spotlight overlay for Linux — pure x86_64 assembly, ~14 KB.
Click-through, screen-share-safe, follows the pointer via SHAPE.

Presenter overlays for the CHasm desktop suite. Four modes from one
binary: spotlight (dimmed screen, circular hole follows the cursor),
draw (click-drag to annotate), highlight (click-drag a rectangle that
stays bright while the surround stays dim), ocr (drag a rectangle over
any on-screen text — even unselectable GUI text — and get it on the clipboard).
Works on every workspace and over screen-share (Teams, Discord, Meet
capture the composited framebuffer, which includes us).

Single static ~24 KB ELF, no libc, pure x86_64 NASM. X11 wire protocol.

%prep
%autosetup -C

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com> - 0.3.0-1
- Initial commit
