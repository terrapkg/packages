Name:           mommy
Version:        1.8.0
Release:        4%?dist
Summary:        mommy's here to support you, in any shell, on any system~ ❤️ 
URL:            https://github.com/fwdekker/mommy
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Patch0:         fix-makefile.patch
License:        Unlicense
BuildArch:      noarch
BuildRequires:  make
Packager:       Olivia <git@olivia.sh>

%description
mommy's here to support you! mommy will compliment you if things go well, and will encourage you if things are not going so well~

%prep
%autosetup -p1

sed GNUmakefile -i \
        -e 's|bin_prefix = .*|bin_prefix = %buildroot%_bindir|g' \
        -e 's|man_prefix = .*|man_prefix = %buildroot%_mandir|g' \
        -e 's|fish_prefix = .*|fish_prefix = %buildroot%fish_completions_dir|g' \
        -e 's|zsh_prefix = .*|zsh_prefix = %buildroot%zsh_completions_dir|g'

%install
%make_install

%files
%license LICENSE
%doc README.md SECURITY.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%pkg_completion -zf

%changelog
* Sun Jul 19 2026 Olivia <git@olivia.sh> - 1.8.0-4
- Update packager

* Sun Dec 6 2025 Olivia <git@olivia.sh> - 1.8.0
- use make

* Wed Dec 3 2025 Olivia <git@olivia.sh>
- package mommy~ ❤️
