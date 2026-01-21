%define binary_name jj
%define nushell_completions_dir %_datadir/nushell/vendor/autoload

%global __brp_mangle_shebangs %{nil}

Name:           jujutsu
Version:        0.37.0
Release:        1%?dist
Summary:        Git-compatible DVCS that is both simple and powerful
License:        Apache-2.0 AND CC-BY-4.0
URL:            https://www.jj-vcs.dev/latest/
Source0:        https://github.com/jj-vcs/jj/archive/refs/tags/v%version.tar.gz
BuildRequires:  cargo >= 1.89
BuildRequires:  git-core cargo-rpm-macros binutils gcc mold
BuildRequires:  gnupg
BuildRequires:  gpgme
BuildRequires:  openssh
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

%package        nushell-completion
Summary:        nushell completion for %name
Requires:       %name = %evr

%description    nushell-completion
nushell command line completion support for %name.

%prep
%autosetup -n jj-%version
%cargo_prep_online

%pkg_completion -bezf %{binary_name}

%build
%cargo_build

%install

# Install the binary
install -Dm 0755 target/rpm/%{binary_name}                         %{buildroot}%{_bindir}/%{binary_name}

# Install the icons
install -Dm644 docs/images/jj-logo.svg                             %{buildroot}%{_scalableiconsdir}/jj-logo.svg
install -Dm644 docs/images/favicon-96x96.png                       %{buildroot}%{_hicolordir}/96x96/apps/jj-logo.png

# Create and install the shell completions
mkdir -p %{buildroot}%{bash_completions_dir}/completions/
%{buildroot}/%{_bindir}/%{binary_name} util completion bash >      %{buildroot}%{bash_completions_dir}/%{binary_name}.bash

mkdir -p %{buildroot}%{elvish_completions_dir}/
%{buildroot}/%{_bindir}/%{binary_name} util completion elvish >    %{buildroot}%{elvish_completions_dir}/%{binary_name}.elv

mkdir -p %{buildroot}%{fish_completions_dir}/
%{buildroot}/%{_bindir}/%{binary_name} util completion fish >      %{buildroot}%{fish_completions_dir}/%{binary_name}.fish

mkdir -p %{buildroot}%{nushell_completions_dir}/
%{buildroot}/%{_bindir}/%{binary_name} util completion nushell >   %{buildroot}%{nushell_completions_dir}/completions-%{binary_name}.nu

mkdir -p %{buildroot}%{zsh_completions_dir}/
%{buildroot}/%{_bindir}/%{binary_name} util completion zsh >       %{buildroot}%{zsh_completions_dir}/_%{binary_name}

# Install the documentation and properly handle the license file
mkdir -p %{buildroot}%{_pkgdocdir}
mv docs/images/LICENSE LICENSE.icons
cp -a docs/* %{buildroot}%{_pkgdocdir}/
rm -rf %{buildroot}%{_pkgdocdir}/images

# Create deps license
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md AUTHORS CHANGELOG.md GOVERNANCE.md SECURITY.md
%license LICENSE
%license LICENSE.dependencies
%license LICENSE.icons
%{_scalableiconsdir}/jj-logo.svg
%{_hicolordir}/96x96/apps/jj-logo.png
%{_bindir}/%{binary_name}

%files nushell-completion
%{nushell_completions_dir}/completions-%{binary_name}.nu

%files doc
%license LICENSE
%doc %{_pkgdocdir}

%changelog
* Tue Dec 16 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
