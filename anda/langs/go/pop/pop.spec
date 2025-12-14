%global debug_package %{nil}

%global goipath github.com/charmbracelet/pop
Version:        0.2.0

%gometa -f

Name:           pop
Release:        1%?dist
Summary:        Send emails from your terminal
URL:            https://github.com/charmbracelet/%{name}
Source0:        https://github.com/charmbracelet/%{name}/archive/refs/tags/v%{version}.tar.gz
License:        MIT

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%summary.

%gopkg

%prep
%goprep -A

%build
%define currentgoldflags -X main.version=%version
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/%{name} .

%install
install -Dm755 %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}

%changelog
* Fri Dec 12 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
