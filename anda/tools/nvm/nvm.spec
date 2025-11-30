Name:     nvm
Version:  0.40.3
Release:  1%{?dist}
Summary:  Node Version Manager
License:  MIT
URL:      https://github.com/nvm-sh/nvm
Source0:  %{url}/archive/refs/tags/v%{version}.tar.gz
# Only works with POSIX compliant shells
Requires:  (bash or dash or ksh or zsh)
BuildArch: noarch

%description
POSIX-compliant script to manage multiple active Node.js versions.

%pkg_completion -b

%prep
%autosetup -n %{name}-%{version}

%build
# Anyone home?

%install
# Works exactly the same as rustup-init
install -Dm744 install.sh %{buildroot}%{_bindir}/%{name}-init

# Also based on Fedora's Rustup, these files are installed so that when this is a system package they are available globally
install -Dm644 bash_completion %{buildroot}%{bash_completions_dir}/%{name}.bash

install -Dm644 %{name}.sh -t %{buildroot}%{_sysconfdir}/profile.d

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}-init
%{_sysconfdir}/profile.d/%{name}.sh
