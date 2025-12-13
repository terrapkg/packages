%global debug_package %{nil}

# The command name is soft but the package and repo are soft-serve.
# The standard use for the tool is `soft serve`.
%global cmd_name soft

Name:           soft-serve
Version:        0.11.1
Release:        1%?dist
Summary:        The mighty, self-hostable Git server for the command line
URL:            https://github.com/charmbracelet/%{name}
Source0:        https://github.com/charmbracelet/%{name}/archive/refs/tags/v%{version}.tar.gz
License:        MIT
BuildRequires:  anda-srpm-macros go

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%summary.

%prep
%autosetup -n %name-%version

%build
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n') -s -w" -buildmode pie -compiler gc -a -x ./cmd/%{cmd_name}

%install
install -Dm755 %{cmd_name} %{buildroot}%{_bindir}/%{cmd_name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{cmd_name}

%changelog
* Fri Dec 12 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
