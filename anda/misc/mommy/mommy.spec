Name:           mommy
Version:        1.8.0
Release:        2%?dist
Summary:        mommy's here to support you, in any shell, on any system~ ❤️ 
URL:            https://github.com/fwdekker/mommy
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
License:        Unlicense
BuildArch:      noarch

%description
mommy's here to support you! mommy will compliment you if things go well, and will encourage you if things are not going so well~

%prep
%autosetup

%install
install -Dm 755 src/main/sh/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 644 src/main/man/man1/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm 644 src/main/completions/fish/%{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dm 644 src/main/completions/zsh/_%{name} %{buildroot}%{zsh_completions_dir}/_%{name}

%files
%license LICENSE
%doc README.md SECURITY.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%pkg_completion -zf

%changelog
* Wed Dec 3 2025 metcya <metcya@gmail.com>
- package mommy~ ❤️
