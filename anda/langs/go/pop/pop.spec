%global debug_package %{nil}

Name:           pop
Version:        0.2.0
Release:        1%?dist
Summary:        Send emails from your terminal
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
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n') -s -w" -buildmode pie -compiler gc -a -x .

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}

%changelog
* Fri Dec 12 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
