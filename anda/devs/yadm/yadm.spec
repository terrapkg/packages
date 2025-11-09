Name:			yadm
Version:		3.5.0
Release:		2%{?dist}
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


%pkg_completion -Bfz


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

%changelog
* Sun May 05 2024 madonuko <mado@fyralabs.com> - 0.5-1
- Initial package.
