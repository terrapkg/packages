%global goipath github.com/bmf-san/ggc/v8
Version:        8.7.2

%gometa -f

Name:           ggc
Release:        1%{?dist}
Summary:        A modern Git CLI tool with both traditional command-line and interactive incremental-search UI

License:        MIT
URL:            https://github.com/bmf-san/ggc
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
Requires:       glibc

%description
%{summary}.

%gopkg

%pkg_completion -bfz

%prep
%autosetup

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/cmd/ %{goipath}

%install
install -Dm755 %{gobuilddir}/cmd/ggc    %{buildroot}%{_bindir}/ggc
install -Dm644 cmd/completions/ggc.bash %{buildroot}%{bash_completions_dir}/ggc.bash
install -Dm644 cmd/completions/ggc.fish %{buildroot}%{fish_completions_dir}/ggc.fish
install -Dm644 cmd/completions/ggc.zsh  %{buildroot}%{zsh_completions_dir}/_ggc

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/ggc

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
