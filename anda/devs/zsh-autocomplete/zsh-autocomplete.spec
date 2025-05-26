%define debug_package %nil

Name:           zsh-autocomplete
Version:        25.03.19
Release:        1%?dist
Summary:        Real-time type-ahead completion for Zsh
License:        MIT
URL:            https://github.com/marlonrichert/zsh-autocomplete
Source0:        %url/archive/refs/tags/%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>

%description
This plugin for Zsh adds real-time type-ahead autocompletion to your command
line, similar to what you find desktop apps. While you type on the command
line, available completions are listed automatically; no need to press any
keyboard shortcuts. Press Tab to insert the top completion or ↓ to select a
different one.

%prep
%autosetup

%build

%install
install -Dpm644 zsh-autocomplete.plugin.zsh -t %buildroot%_datadir/zsh-autocomplete/
mv Completions Functions %buildroot%_datadir/zsh-autocomplete/

%files
%doc README.md
%license LICENSE
%_datadir/zsh-autocomplete/
