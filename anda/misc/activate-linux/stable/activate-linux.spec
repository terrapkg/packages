Name:           activate-linux
Summary:        The "Activate Windows" watermark ported to Linux
Version:        1.2.0
License:        GPL-3.0-only
Release:        3%{?dist}
URL:            https://github.com/MrGlockenspiel/activate-linux
Patch0:         0001-Install-manpage-to-correct-location.patch
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  clang 
BuildRequires:  pkgconfig(pango)
BuildRequires:  libconfig-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
Packager:       Olivia <git@olivia.sh>

%description
The "Activate Windows" watermark ported to Linux with Xlib and cairo in C

"Science isn't about WHY. It's about WHY NOT. Why is so much of our science dangerous? Why not marry safe science if you love it so much. In fact, why not invent a special safety door that won't hit you on the butt on the way out, because you are fired."

Maintained by MrGlockenspiel.

%prep
%autosetup

%build
%make_build

%install
%make_install PREFIX=%{_usr}

%files
%{_bindir}/activate-linux
%{_mandir}/man1/activate-linux.1.*
%license LICENSE.md
%doc ARGS.md README.md

%changelog
* Sun Jul 19 2026 Olivia <git@olivia.sh> - 1.2.0-3
- Update packager

* Sun Jul 19 2026 Olivia <git@olivia.sh> - 1.2.0-2
- Add stable channel

* Sun Nov 2 2025 Olivia <git@olivia.sh>
- Package activate-linux
