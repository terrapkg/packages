%global debug_package %{nil}
%global commit 6c9e2569843b08db14a964951f17a3943fd89fa2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20241124
%global ver 1.0.0

Name:          pokeshell
Version:       %{ver}^%{date}git.%{shortcommit}
Release:       4%{?dist}
Summary:       A shell program to show Pokémon sprites in the terminal.
License:       GPL-3.0-or-later
URL:           https://github.com/acxz/pokeshell
Source0:       %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:       HELPER_ALIASES
BuildRequires: sed
Requires:      bash
Requires:      jq
Requires:      ImageMagick
Requires:      python3
Requires:      chafa
Recommends:    timg
BuildArch:     noarch
Packager:      Gilver E. <roachy@fyralabs.com>

%description
A featureful shell program to show Pokémon sprites in the terminal.

%package       helper-scripts
Summary:       This package contains helper scripts for Pokéshell
Requires:      bash
Requires:      %{name}
Requires:      uv
Recommends:    hyperfine
Recommends:    pokeget
Recommends:    pokemon-colorscripts

%description helper-scripts
Generates pokemon identifiers (such as localized names) using PokeAPI that the sprite backends do not support natively.

See included README for what these scripts can do.

%package       bash-completion
Summary:       Bash completion for Pokéshell
Requires:      bash
Requires:      %{name}
Supplements:   (%{name} and bash)

%description   bash-completion
Pokéshell Bash completion.

%package       zsh-completion
Summary:       Zsh completion for Pokéshell
Requires:      %{name}
Requires:      zsh
Supplements:   (%{name} and zsh)

%description   zsh-completion
Basic Zsh completion support for Pokéshell.

%prep
%autosetup -n %{name}-%{commit}
cp %{SOURCE1} .
sed -i 's/MY_DIR=.*/MY_DIR=\/usr\/share\/%{name}/g' bin/pokeshell
sed -i 's/\.\.\/share\///' bin/pokeshell

%build

%install
install -Dm755 bin/pokeshell %{buildroot}%{_bindir}/%{name}
install -Dm755 bin/imageshell/imageshell.sh -t %{buildroot}%{_datadir}/%{name}/imageshell
install -Dm644 share/pokemon_identifiers.json -t %{buildroot}%{_datadir}/%{name}
install -Dm644 scripts/*.py -t %{buildroot}%{_datadir}/%{name}/scripts
install -Dm644 scripts/*.sh -t %{buildroot}%{_datadir}/%{name}/scripts
# Bash and Zsh completion share a single file, Zsh completion is pretty rudimentary
install -Dm644 share/bash-completion/completions/pokeshell -t %{buildroot}%{bash_completions_dir}
install -Dm644 share/bash-completion/completions/pokeshell %{buildroot}%{zsh_completions_dir}/_%{name}
# Make helper scripts directly executable
ln -sf %{_datadir}/%{name}/scripts/create_pokemon_identifiers.py %{buildroot}%{_bindir}/create-pokemon-identifiers
ln -sf %{_datadir}/%{name}/scripts/timing.sh %{buildroot}%{_bindir}/pokeget-timing

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/pokemon_identifiers.json
%dir %{_datadir}/%{name}/imageshell
%{_datadir}/%{name}/imageshell/imageshell.sh

%files helper-scripts
%doc scripts/README.md HELPER_ALIASES
%dir %{_datadir}/%{name}/scripts
%{_datadir}/%{name}/scripts/*
%{_bindir}/create-pokemon-identifiers
%{_bindir}/pokeget-timing

%files bash-completion
%{bash_completions_dir}/%{name}

%files zsh-completion
%{zsh_completions_dir}/_%{name}

%changelog
* Sat Mar 01 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
