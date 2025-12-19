%define binary_name jj
%define nushell_completions_dir %_datadir/nushell/vendor/autoload

%global __brp_mangle_shebangs %{nil}

Name:           jujutsu
Version:        0.36.0
Release:        1%?dist
Summary:        Git-compatible DVCS that is both simple and powerful
License:        Apache-2.0
URL:            https://www.jj-vcs.dev/latest/
Source0:        https://github.com/jj-vcs/jj/archive/refs/tags/v%version.tar.gz
BuildRequires:  cargo >= 1.89
BuildRequires:  git-core cargo-rpm-macros binutils gcc mold
BuildRequires:  gnupg
BuildRequires:  gpgme
BuildRequires:  openssh

BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh

Requires:       glibc
Requires:       libgit2
Requires:       libssh2

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Jujutsu is a Git-compatible DVCS. It combines features from Git (data model,
speed), Mercurial (anonymous branching, simple CLI free from "the index",
revsets, powerful history-rewriting), and Pijul/Darcs (first-class conflicts),
with features not found in most of them (working-copy-as-a-commit, undo
functionality, automatic rebase, safe replication via rsync, Dropbox, or
distributed file system).

The command-line tool is called jj for now because it's easy to type and easy
to replace (rare in English). The project is called "Jujutsu" because it
matches "jj".

Jujutsu is relatively young, with lots of work to still be done. If you have
any questions, or want to talk about future plans, please join us on Discord
Discord or start a GitHub Discussion; the developers monitor both channels.

Important
Jujutsu is an experimental version control system. While Git compatibility is
stable, and most developers use it daily for all their needs, there may still
be work-in-progress features, suboptimal UX, and workflow gaps that make it
unusable for your particular use.

%package        doc
Summary:        Documentations for %{name}
BuildArch:      noarch

%description    doc
Documentations for %{name}.

%package        %name-nushell-completion
Summary:        nushell completion files for %name
Requires:       %name = %evr

%description    %name-nushell-completion
nushell completion files for %name.

%dnl %package        %name-bash-completion
%dnl Summary:        bash completion files for %name
%dnl Requires:       %name = %evr

%dnl %description    %name-bash-completion
%dnl bash completion files for %name.

%dnl %package        %name-zsh-completion
%dnl Summary:        zsh completion files for %name
%dnl Requires:       %name = %evr

%dnl %description    %name-zsh-completion
%dnl zsh completion files for %name.

%dnl %package        %name-fish-completion
%dnl Summary:        fish completion files for %name
%dnl Requires:       %name = %evr

%dnl %description    %name-fish-completion
%dnl fish completion files for %name.

%dnl %package        %name-elvish-completion
%dnl Summary:        elvish completion files for %name
%dnl Requires:       %name = %evr

%dnl %description    %name-elvish-completion
%dnl elvish completion files for %name.

%prep
%autosetup -n jj-%version
%cargo_prep_online

%pkg_completion -b %name -n %{binary_name}
%pkg_completion -ezf %name -n %{binary_name}

%build
%cargo_build

%install
install -Dm 0755 target/rpm/%{binary_name} %{buildroot}%{_bindir}/%{binary_name}

mkdir -p %{buildroot}%{bash_completions_dir}/completions/
%{buildroot}/%{_bindir}/%{binary_name} util completion bash > %{buildroot}%{bash_completions_dir}/completions/%{binary_name}.bash

mkdir -p %{buildroot}%{elvish_completions_dir}/
%{buildroot}/%{_bindir}/%{binary_name} util completion elvish > %{buildroot}%{elvish_completions_dir}/%{binary_name}.elv

mkdir -p %{buildroot}%{fish_completions_dir}/
%{buildroot}/%{_bindir}/%{binary_name} util completion fish > %{buildroot}%{fish_completions_dir}/%{binary_name}.fish

mkdir -p %{buildroot}%{nushell_completions_dir}/
%{buildroot}/%{_bindir}/%{binary_name} util completion nushell > %{buildroot}%{nushell_completions_dir}/completions-%{binary_name}.nu

mkdir -p %{buildroot}%{zsh_completions_dir}/
%{buildroot}/%{_bindir}/%{binary_name} util completion zsh > %{buildroot}%{zsh_completions_dir}/_%{binary_name}

mkdir -p %{buildroot}%{_pkgdocdir}
cp -a docs/* %{buildroot}%{_pkgdocdir}/

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md AUTHORS CHANGELOG.md GOVERNANCE.md SECURITY.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/%{binary_name}

%files %{name}-nushell-completion
%{nushell_completions_dir}/completions-%{binary_name}.nu

%dnl %files %{name}-bash-completion
%dnl %{bash_completions_dir}/completions/%{binary_name}.bash

%dnl %files %{name}-zsh-completion
%dnl %{zsh_completions_dir}/_%{binary_name}

%dnl %files %{name}-fish-completion
%dnl %{fish_completions_dir}/%{binary_name}.fish

%dnl %files %{name}-elvish-completion
%dnl %{elvish_completions_dir}/%{binary_name}.elv

%files doc
%doc README.md AUTHORS CHANGELOG.md GOVERNANCE.md SECURITY.md
%license LICENSE
%doc %{_pkgdocdir}

%changelog
* Tue Dec 16 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
