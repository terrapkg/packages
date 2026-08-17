%global commit 5802ff67520be2ff6117a0abc78a08501f6252ad
%global commit_date 20241018
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          pokemon-colorscripts
Version:       0^%{commit_date}git.%{shortcommit}
Release:       2%{?dist}
License:       MIT
Summary:       CLI utility to print out images of Pokémon to the terminal
URL:           https://gitlab.com/phoneybadger/%{name}
Source0:       %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:     noarch
Requires:      python3
Packager:      Gilver E. <roachy@fyralabs.com>

%description
A utility that prints unicode sprites of images of Pokémon to the terminal.

%prep
%autosetup -n %{name}-%{commit}

%build

%install
install -Dm644 colorscripts/small/regular/* -t "%{buildroot}%{_datadir}/%{name}/colorscripts/small/regular"
install -Dm644 colorscripts/small/shiny/* -t "%{buildroot}%{_datadir}/%{name}/colorscripts/small/shiny"
install -Dm644 colorscripts/large/regular/* -t "%{buildroot}%{_datadir}/%{name}/colorscripts/large/regular"
install -Dm644 colorscripts/large/shiny/* -t "%{buildroot}%{_datadir}/%{name}/colorscripts/large/shiny"
install -Dm644 pokemon.json "%{buildroot}%{_datadir}/%{name}/pokemon.json"
install -Dm755 pokemon-colorscripts.py "%{buildroot}%{_datadir}/%{name}/pokemon-colorscripts.py"
install -Dm644 pokemon-colorscripts.1 "%{buildroot}%{_mandir}/man1/pokemon-colorscripts.1"
# Make name executable
mkdir -p %{buildroot}%{_bindir}
ln -sf "%{_datadir}/%{name}/pokemon-colorscripts.py" "%{buildroot}%{_bindir}/pokemon-colorscripts"

%files
%license LICENSE.txt
%doc README.md
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_bindir}/pokemon-colorscripts
%{_mandir}/man1/pokemon-colorscripts.1.gz

%changelog
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
