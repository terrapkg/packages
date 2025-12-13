%define debug_package %{nil}

Name:           newsraft
Version:        0.34
Release:        1%?dist
Summary:        Newsraft is a feed reader with text-based user interface.

# It's hosted on codeberg but updates are easier from the github mirror.
URL:            https://codeberg.org/newsraft/%{name}
Source0:        https://github.com/newsraft/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
License:        ISC

# The Requires and BuildRequires are duplicated because they are used both
# at build and runtime.
BuildRequires:  anda-srpm-macros gcc make
BuildRequires:  sqlite-devel
BuildRequires:  gumbo-parser-devel
BuildRequires:  expat-devel
BuildRequires:  libcurl-devel
BuildRequires:  scdoc %dnl This is just for man pages.

Requires:       sqlite-devel
Requires:       gumbo-parser-devel
Requires:       expat-devel
Requires:       libcurl-devel

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%summary.
It's greatly inspired by Newsboat and tries to be its lightweight counterpart.

%prep
# The source just has an ugly dir name.
%autosetup -n %name-%name-%version

%build
%{make_build}
%{make_build} man

%install
mkdir -p %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
mkdir -p %{buildroot}%{_datadir}/applications/

install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/
install -Dm644 doc/%{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
install -Dm644 doc/%{name}.desktop %{buildroot}%{_datadir}/applications/

%files
%doc README.md
%license doc/license.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

%changelog
* Wed Dec 10 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
