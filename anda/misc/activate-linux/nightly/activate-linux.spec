%global commit a3e2346a56a6ddab771e5971e71641913944dd54
%global date 20260719
%global short %(c=%{commit}; echo ${c:0:7})
%global ver 1.2.0

Name:           activate-linux-nightly
Summary:        The "Activate Windows" watermark ported to Linux
Version:        %{ver}^%{date}git.%{short}
License:        GPL-3.0-only
Release:        2%{?dist}
URL:            https://github.com/MrGlockenspiel/activate-linux
Patch0:         0001-Install-manpage-to-correct-location.patch
Source0:        %{url}/archive/%{commit}.tar.gz
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
Packager:       Metcya <metcya@gmail.com>

%description
The "Activate Windows" watermark ported to Linux with Xlib and cairo in C

"Science isn't about WHY. It's about WHY NOT. Why is so much of our science dangerous? Why not marry safe science if you love it so much. In fact, why not invent a special safety door that won't hit you on the butt on the way out, because you are fired."

Maintained by MrGlockenspiel.

%prep
%autosetup -n activate-linux-%{commit}

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
* Sun Jul 19 2026 Olivia <git@olivia.sh> - 1.2.0^20260719git.a3e2346-2
- Change to nightly

* Sun Nov 2 2025 Metcya <metcya@gmail.com>
- Package activate-linux
