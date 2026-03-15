Name:     nvm
Version:  0.40.4
Release:  1%?dist
Summary:  Node Version Manager
License:  MIT
URL:      https://github.com/nvm-sh/nvm
Source0:  %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:  binscript
# Make sure NVM always chooses "$HOME/.nvm" as the directory for local files unless explicitly set otherwise
Patch0:   nvm-always-use-default-dir.patch
# Only works with POSIX compliant shells
Requires: bash
BuildArch: noarch
Packager:  Gilver E. <roachy@fyralabs.com>

%description
POSIX-compliant script to manage multiple active Node.js versions.

%pkg_completion -bz

%prep
%autosetup -n %{name}-%{version} -p1

%build
# Anyone home?

%install
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# Give nvm-exec the correct search directory
sed -i 's|DIR=.*|DIR="%{_sysconfdir}/profile.d"|g' nvm-exec
install -Dm755 nvm-exec -t %{buildroot}%{_bindir}

install -Dm644 bash_completion %{buildroot}%{bash_completions_dir}/%{name}.bash
# Another cursed script that uses bashcompinit to use one file for Bash and Zsh completions
install -Dm644 bash_completion %{buildroot}%{zsh_completions_dir}/_%{name}

# Make NVM expect nvm-exec in the bindir
sed -i 's|${NVM_DIR}/nvm-exec|%{_bindir}/nvm-exec|g' %{name}.sh
install -Dm644 %{name}.sh -t %{buildroot}%{_sysconfdir}/profile.d

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-exec
%{_sysconfdir}/profile.d/%{name}.sh

%changelog
* Sun Nov 30 2025 Gilver E. <rockgrub@disroot.org> - 0.40.3-1
- Initial package
