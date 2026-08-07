Name:           pixi
Version:        0.76.1
Release:        1%{?dist}
Summary:        A cross-platform, multi-language package manager
License:        BSD-3-Clause AND bzip2-1.0.6 AND MPL-2.0 AND Unicode-3.0 AND (Zlib OR Apache-2.0 OR MIT) AND Zlib AND (Unlicense OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (MIT OR LGPL-3.0-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND CDLA-Permissive-2.0 AND (LGPL-3.0-or-later OR MPL-2.0) AND (ISC AND (Apache-2.0 OR ISC) AND OpenSSL) AND (ISC AND (Apache-2.0 OR ISC)) AND ISC AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (CC0-1.0 OR MIT-0) AND BSL-1.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND (MIT OR Apache-2.0) AND Unicode-3.0 AND 0BSD AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (Apache-2.0 OR BSD-2-Clause) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 WITH LLVM-exception) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT)

URL:            https://pixi.sh
Source:         https://github.com/prefix-dev/pixi/archive/refs/tags/v%{version}.tar.gz
Packager:       Olivia <git@olivia.sh>

BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  mold

%pkg_completion -BefNz

%description
pixi is a cross-platform, multi-language package manager and workflow tool
built on the foundation of the conda ecosystem. It provides developers with an
exceptional experience similar to popular package managers like cargo or npm,
but for any language.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
for shell in bash elvish fish nushell zsh; do
    target/rpm/%{name} completion --shell $shell > completions.$shell
done

%install
install -Dm 755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 644 completions.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dm 644 completions.elvish %{buildroot}%{elvish_completions_dir}/%{name}.elv
install -Dm 644 completions.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dm 644 completions.nushell %{buildroot}%{nushell_completions_dir}/%{name}.nu
install -Dm 644 completions.zsh %{buildroot}%{zsh_completions_dir}/_%{name}

%{__cargo} tree                                                             \
    -Z avoid-dev-deps                                                       \
    --workspace                                                             \
    --edges no-build,no-dev,no-proc-macro                                   \
    --target all                                                            \
    %{__cargo_parse_opts %{-n} %{-a} %{-f:-f%{-f*}}}                        \
    --prefix none                                                           \
    --format "{l}: {p}"                                                     \
    | sed -e "s: ($(pwd)[^)]*)::g" -e "s: / :/:g" -e "/\/.*:/{s/\// OR /}"  \
    | sed -e '/.*(\*).*/d'.                                                 \
    | sort -u                                                               \
> LICENSE.dependencies

%files
%doc README.md CHANGELOG.md
%license LICENSE LICENSE.dependencies
%{_bindir}/%{name}

%changelog
* Thu Jul 23 2026 Owen Zimmerman <owen@fyralabs.com> - 0.66.0-1
- Add dependency licenses, add nushell completions

* Sun Jul 19 2026 Olivia <git@olivia.sh> - 0.73.0-2
- Update packager

* Wed Dec 17 2025 Olivia <git@olivia.sh> - 0.62.0
- Initial package
