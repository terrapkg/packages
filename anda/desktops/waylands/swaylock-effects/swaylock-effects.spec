%global commit 496059a8565c2d5eed672c2e5bc5e1edd14b3de8
%global shortcommit %{sub %{commit} 1 7}

Name:           swaylock-effects
Version:        1.7.0.0^1.%{shortcommit}
Release:        1%{?dist}
Summary:        Swaylock, with fancy effects

License:        MIT
URL:            https://github.com/jirutka/swaylock-effects
Source0:        %{url}/archive/%{commit}.tar.gz

Packager:       sadlerm <lerm@chromebooks.lol>

BuildRequires:  meson gcc
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc

Recommends:     %{name}-bash-completion

Conflicts:      swaylock

%define binary_name swaylock

%description
swaylock-effects is a fork of swaylock which adds built-in screenshots and image manipulation effects like blurring.


%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Bash command-line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)

%description zsh-completion
Zsh command-line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       fish
Supplements:    (%{name} and fish)

%description fish-completion
Fish command-line completion support for %{name}.


%prep
%autosetup -n %{name}-%{commit}


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{binary_name}
%{_mandir}/man1/%{binary_name}.1.gz
%config(noreplace) %{_sysconfdir}/pam.d/%{binary_name}

%files bash-completion
%{bash_completions_dir}/%{binary_name}

%files zsh-completion
%{zsh_completions_dir}/_%{binary_name}

%files fish-completion
%{fish_completions_dir}/%{binary_name}.fish


%changelog
* Tue Feb 04 2025 sadlerm <lerm@chromebooks.lol>
- Initial package
