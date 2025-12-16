%define binary_name jj

Name:           jujutsu
Version:        0.36.0
Release:        1%?dist
Summary:        Git-compatible DVCS that is both simple and powerful
License:        Apache-2.0
URL:            https://www.jj-vcs.dev/latest/
Source0:        https://github.com/jj-vcs/jj/archive/refs/tags/v%version.tar.gz
BuildRequires:  cargo >= 1.89
%dnl BuildRequires:  cargo-packaging
BuildRequires:  git-core cargo-rpm-macros binutils gcc mold
BuildRequires:  gnupg
BuildRequires:  gpgme
BuildRequires:  openssh
# dependencies for completion subpackages
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh

Packager:       Owen Zimmerman <owen@fyralabs.com>

ExcludeArch:    i586 s390x armv7hl armv7l armv7l:armv6l:armv5tel armv6hl

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

%package doc
Summary:	Documentations for %{name}
Requires:   %{name} = %evr
BuildArch:	noarch
%description doc
Documentations for %{name}.

%prep
%autosetup -n jj-%version
%cargo_prep_online

%pkg_completion -Bezf %{binary_name}

%build
%dnl %cargo_build
ls -la
%cargo_build
ls -la target

%install
%dnl mkdir -p %{buildroot}%{_bindir}
%dnl install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{binary_name} %{buildroot}%{_bindir}/%{binary_name}

# If nushell ever adds completion files, we can probably install the .nu jujutsu completion file to /usr/share/nushell/completions
%dnl install -Dm644 %{binary_name}.nu %{buildroot}/usr/share/nushell/completions/%{binary_name}.nu"

cp -a docs/* %{buildroot}%{_pkgdocdir}

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md AUTHORS CHANGELOG.md GOVERNANCE.md SECURITY.md
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/%{binary_name}

%files doc
%doc %{_pkgdocdir}

%changelog
* Tue Dec 16 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
