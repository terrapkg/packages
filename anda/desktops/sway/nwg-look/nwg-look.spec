%dnl %define debug_package %{nil}

%global goipath github.com/nwg-piotr/nwg-look
Version:        1.0.6

%gometa -f

Name:           nwg-look
Release:        1%?dist
Summary:        GTK3 settings editor adapted to work in the wlroots environment

License:        MIT
URL:            https://github.com/nwg-piotr/nwg-look
Source0:        https://github.com/nwg-piotr/nwg-look/archive/refs/tags/v%version.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
Requires:       glibc

%description
%{summary}.

%gopkg

%prep
%autosetup -n %{name}-%{version}

%build
%make_build
%make_build build
ls -la
%dnl %define gomodulesmode GO111MODULE=on
# export CGO_CPPFLAGS="${CPPFLAGS}"
# export CGO_CFLAGS="${CFLAGS}"
# export CGO_CXXFLAGS="${CXXFLAGS}"
# export CGO_LDFLAGS="${LDFLAGS}"
# export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
%dnl %gobuild -o %{gobuilddir}/nwg-look %{goipath}/nwg-look

%install
%make_install
%dnl install -Dm 0755 %{gobuilddir}/cmd/nwg-look %{buildroot}%{_bindir}/nwg-look

%files
%license LICENSE
%doc README.md
%{_bindir}/nwg-look

%changelog
* Fri Dec 05 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
