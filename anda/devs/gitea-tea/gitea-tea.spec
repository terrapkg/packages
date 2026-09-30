#
# spec file for package gitea-tea
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%global goipath         gitea.dev/tea

Name:           gitea-tea
Version:        0.16.0
Release:        1%{?dist}
Summary:        A command line tool to interact with Gitea servers
License:        MIT
URL:            https://gitea.com/gitea/tea
Source0:        %{url}/archive/v%{version}.tar.gz
Packager:       Leo Douglas <douglarek@gmail.com>

BuildRequires:  anda-srpm-macros
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  go-rpm-macros
BuildRequires:  golang >= 1.26.0
BuildRequires:  zsh
Conflicts:      tea
Requires:       git-core

%description
Tea can be used to manage most entities on one or multiple Gitea
instances and provides local helpers like 'tea pr checkout'.

It tries to make use of context provided by the repository in $PWD
if available. And works best in a upstream/fork workflow, when the
local main branch tracks the upstream repo. It also assumes that
local git state is published on the remote before doing operations.
Configuration lives in $XDG_CONFIG_HOME/tea.

%pkg_completion -Bfz tea

%prep
%autosetup -n tea
export GOTOOLCHAIN=local
go mod download

%build
export GOTOOLCHAIN=local
sdkversion=$(awk '$1 == "gitea.dev/sdk" { print substr($2, 2); exit }' go.mod)
test -n "$sdkversion"

%global gomodulesmode GO111MODULE=on
%global currentgoldflags %{?currentgoldflags} -X %{goipath}/modules/version.Version=%{version} -X %{goipath}/modules/version.SDK=${sdkversion}
%gobuild -o tea .
%gobuild -o tea-docs ./docs
./tea-docs --out docs/CLI.md

%install
install -v -m 0755 -D -t %{buildroot}%{_bindir} tea

./tea completion bash > contrib/autocomplete.sh
sed -i '1d' contrib/autocomplete.sh
install -v -m 0644 -D contrib/autocomplete.sh \
    %{buildroot}%{bash_completions_dir}/tea

./tea completion zsh > contrib/autocomplete.zsh
install -v -m 0644 -D contrib/autocomplete.zsh \
    %{buildroot}%{zsh_completions_dir}/_tea

./tea completion fish > contrib/autocomplete.fish
install -v -m 0644 -D contrib/autocomplete.fish \
    %{buildroot}%{fish_completions_dir}/tea.fish

%files
%license LICENSE
%doc CHANGELOG.md docs/CLI.md CONTRIBUTING.md README.md
%{_bindir}/tea

%changelog
%autochangelog
