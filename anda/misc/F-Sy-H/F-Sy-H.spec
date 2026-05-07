Name:           F-Sy-H
Version:        1.67
Release:        2%?dist
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

mkdir -p %{buildroot}%{zsh_completions_dir}/chroma
mkdir -p %{buildroot}%{zsh_completions_dir}/functions
mkdir -p %{buildroot}%{zsh_completions_dir}/share
mkdir -p %{buildroot}%{zsh_completions_dir}/share/parse
mkdir -p %{buildroot}%{zsh_completions_dir}/themes

install -Dm644 F-Sy-H.plugin.zsh %{buildroot}%{zsh_completions_dir}/F-Sy-H.plugin.zsh
install -Dm644 chroma/*          %{buildroot}%{zsh_completions_dir}/chroma/
install -Dm644 functions/*       %{buildroot}%{zsh_completions_dir}/functions/
install -Dm644 share/*.zsh       %{buildroot}%{zsh_completions_dir}/share/
install -Dm644 share/parse/*     %{buildroot}%{zsh_completions_dir}/share/parse/
install -Dm644 themes/*          %{buildroot}%{zsh_completions_dir}/themes/

%files
%doc docs/*.md
%license LICENSE
%{zsh_completions_dir}/F-Sy-H.plugin.zsh
%{zsh_completions_dir}/chroma/*
%{zsh_completions_dir}/functions/*
%{zsh_completions_dir}/share/*.zsh
%{zsh_completions_dir}/share/parse/*
%{zsh_completions_dir}/themes/*

%changelog
* Tue Oct 07 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
