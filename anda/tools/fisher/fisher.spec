Name:           fisher
Version:        4.4.8
Release:        1%{?dist}
Summary:        A plugin manager for the fish shell

License:        MIT
URL:            https://github.com/jorgebucaran/fisher
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Packager:       Caio Bruno <cbrunofb@gmail.com>

BuildArch:      noarch
Requires:       fish curl

%description
fisher is a plugin manager for the fish shell — install plugins, themes,
and functions from the command line with a single command.

%prep
%autosetup -n fisher-%{version}

%build

%install
install -Dm644 functions/fisher.fish    %{buildroot}%{_datadir}/fish/vendor_functions.d/fisher.fish
install -Dm644 completions/fisher.fish  %{buildroot}%{_datadir}/fish/vendor_completions.d/fisher.fish

%files
%license LICENSE.md
%doc README.md
%{fish_functions_dir}/fisher.fish
%{fish_completions_dir}/fisher.fish

%changelog
* Thu Jul 30 2026 Caio Bruno <cbrunofb@gmail.com>
- Initial package
