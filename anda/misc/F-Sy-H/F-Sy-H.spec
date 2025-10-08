%define _zshfuncdir %{_datadir}/zsh/site-functions

Name:           F-Sy-H
Version:        1.67
Release:        1%?dist
Summary:        Feature-rich Syntax Highlighting for Zsh
License:        BSD-3-Clause
URL:            https://github.com/z-shell/F-Sy-H
Source0:        %url/archive/refs/tags/v%version.tar.gz
Requires:       zsh
BuildArch:      noarch
Provides:       f-sy-h
Provides:       zsh-F-Sy-H
Provides:       zsh-f-sy-h
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n F-Sy-H-%{version}

%build

%install

mkdir -p %{buildroot}%{_zshfuncdir}/chroma
mkdir -p %{buildroot}%{_zshfuncdir}/functions
mkdir -p %{buildroot}%{_zshfuncdir}/share
mkdir -p %{buildroot}%{_zshfuncdir}/share/parse
mkdir -p %{buildroot}%{_zshfuncdir}/themes

install -Dm644 F-Sy-H.plugin.zsh %{buildroot}%{_zshfuncdir}/F-Sy-H.plugin.zsh
install -Dm644 chroma/*          %{buildroot}%{_zshfuncdir}/chroma/
install -Dm644 functions/*       %{buildroot}%{_zshfuncdir}/functions/
install -Dm644 share/*.zsh       %{buildroot}%{_zshfuncdir}/share/
install -Dm644 share/parse/*     %{buildroot}%{_zshfuncdir}/share/parse/
install -Dm644 themes/*          %{buildroot}%{_zshfuncdir}/themes/

%files
%doc docs/*.md
%license LICENSE
%{_zshfuncdir}/F-Sy-H.plugin.zsh
%{_zshfuncdir}/chroma/*
%{_zshfuncdir}/functions/*
%{_zshfuncdir}/share/*.zsh
%{_zshfuncdir}/share/parse/*
%{_zshfuncdir}/themes/*

%changelog
* Tue Oct 07 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
