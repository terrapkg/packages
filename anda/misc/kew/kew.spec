Name:           kew
Version:        4.1.5
Release:        1%{?dist}
Summary:        Music for the Shell
URL:            https://codeberg.org/ravachol/kew
Source0:        %{url}/archive/v%{version}.tar.gz
License:        GPL-2.0-or-later
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(chafa)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(ogg)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%git_clone https://codeberg.org/ravachol/kew.git v%{version}

%build
%make_build CC="%__cc %build_cflags" CXX="%__cxx %build_cxxflags" SYMBOLS=1

%install
%make_install PREFIX=/usr

%find_lang kew

%files -f kew.lang
%license LICENSE
%doc README.md
%lang(zh_CN) %doc README_zh_CN.md
%{_bindir}/kew
%{_datadir}/kew/
%{_mandir}/man1/kew.1.*
%{_appsdir}/kew.desktop
%{_hicolordir}/*/apps/kew.png

%changelog
* Thu Apr 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
