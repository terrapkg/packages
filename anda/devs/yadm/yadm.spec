Name:			yadm
Version:		3.5.0
Release:		1%{?dist}
Summary:		Yet Another Dotfiles Manager

License:        GPL-3.0-only
URL:            https://yadm.io
Source:         https://github.com/yadm-dev/yadm/archive/refs/tags/%{version}.tar.gz
Packager:       madonuko <mado@fyralabs.com>

BuildArch:		noarch
Requires:		bash git

%description
yadm is a tool for managing a collection of files across multiple computers,
using a shared Git repository. In addition, yadm provides a feature to select
alternate versions of files based on the operation system or host name. Lastly,
yadm supplies the ability to manage a subset of secure files, which are
encrypted before they are included in the repository.


%package bash-completion
Summary:		Bash completion for %{name}
Requires:		%{name} = %{version}-%{release}
Requires: 		bash-completion
Supplements:	(%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:		Fish completion for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		fish
Supplements:	(%{name} and fish)

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:		Zsh completion for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		zsh
Supplements:	(%{name} and zsh)

%description zsh-completion
Zsh command line completion support for %{name}.


%prep
%autosetup

%install
install -Dpm755 yadm	-t %buildroot%_bindir
install -Dpm644 yadm.1	-t %buildroot%_mandir/man1
install -Dpm644 -t %buildroot%bash_completions_dir completion/bash/yadm
install -Dpm644 -t %buildroot%fish_completions_dir completion/fish/yadm.fish
install -Dpm644 -t %buildroot%zsh_completions_dir completion/zsh/_yadm

%files
%doc README.* CHANGES CONTRIBUTORS
%doc contrib
%license LICENSE
%_bindir/yadm
%_mandir/man1/yadm.1.gz

%files bash-completion
%bash_completions_dir/yadm

%files fish-completion
%fish_completions_dir/yadm.fish

%files zsh-completion
%zsh_completions_dir/_yadm

%changelog
* Sun May 05 2024 madonuko <mado@fyralabs.com> - 0.5-1
- Initial package.
