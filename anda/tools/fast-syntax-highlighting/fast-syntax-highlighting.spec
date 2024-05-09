Name: fast-syntax-highlighting
Version: 1.67
Release: 1%?dist

Summary: Feature-rich Syntax Highlighting for Zsh
License: BSD-3-Clause
URL:     https://github.com/zdharma-continuum/%name
Source0: %url/archive/refs/tags/v%{version}.tar.gz

BuildArch: noarch

%description
Feature-rich Syntax Highlighting for Zsh.

%prep
%autosetup

%build

%install
install -Dm644 %name.plugin.zsh %buildroot%_datadir/%name/%name.plugin.zsh

%files
%_datadir/%name/%name.plugin.zsh

%changelog
%autochangelog
