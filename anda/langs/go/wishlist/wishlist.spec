%global debug_package %{nil}

%global goipath github.com/charmbracelet/wishlist
Version:        0.15.2

%gometa -f

Name:           wishlist
Release:        1%?dist
Summary:        The SSH directory
URL:            https://github.com/charmbracelet/%{name}
Source0:        https://github.com/charmbracelet/%{name}/archive/refs/tags/v%{version}.tar.gz
License:        MIT

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%summary.

%prep
%goprep -A

%build
%define currentgoldflags -X main.version=%version
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/%{name} ./cmd/%{name}

%install
install -Dm755 %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Thu Dec 11 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
