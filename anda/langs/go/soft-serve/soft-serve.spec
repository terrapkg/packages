%global debug_package %{nil}

# The command name is soft but the package and repo are soft-serve.
# The standard use for the tool is `soft serve`.
%global cmd_name soft

%global goipath github.com/charmbracelet/soft-serve
Version:        0.11.2

%gometa -f

Name:           soft-serve
Release:        1%?dist
Summary:        The mighty, self-hostable Git server for the command line
URL:            https://github.com/charmbracelet/%{name}
Source0:        https://github.com/charmbracelet/%{name}/archive/refs/tags/v%{version}.tar.gz
License:        MIT

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%{summary}.

%gopkg

%prep
%goprep -A

%build
%define currentgoldflags -X main.version=%version
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/%{cmd_name} ./cmd/%{cmd_name}

%install
install -Dm755 %{gobuilddir}/bin/%{cmd_name} %{buildroot}%{_bindir}/%{cmd_name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{cmd_name}

%changelog
* Sat Dec 13 2025 arbormoss <arbormoss@woodsprite.dev>
- Refactor to use go rpm macros

* Fri Dec 12 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
