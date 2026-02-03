Name:           gradle-completions
Version:        9.3.1
Release:        1%?dist
Summary:        Gradle tab completion for bash and zsh
License:        MIT
URL:            https://github.com/gradle/gradle-completion
Source0:        %url/archive/refs/tags/v%version.tar.gz
Requires:       gradle-bash-completion = %{evr}
Requires:       gradle-zsh-completion = %{evr}
BuildArch:      noarch

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%package -n gradle-bash-completion
Summary:    Bash completion for Gradle
Recommends: gradle
%description -n gradle-bash-completion
%summary.

%package -n gradle-zsh-completion
Summary:    zsh completion for Gradle
Recommends: gradle
%description -n gradle-zsh-completion
%summary.

%prep
%autosetup -n gradle-completion-%{version}

%build

%install
install -Dm644 gradle-completion.bash       %{buildroot}%{bash_completions_dir}/gradle
install -Dm644 gradle-completion.plugin.zsh %{buildroot}%{zsh_completions_dir}/gradle-completion.plugin.zsh
install -Dm644 _gradle                      %{buildroot}%{zsh_completions_dir}/_gradle

%files
%doc README.md CONTRIBUTING.md
%license LICENSE

%files -n gradle-bash-completion
%license LICENSE
%{bash_completions_dir}/gradle

%files -n gradle-zsh-completion
%license LICENSE
%{zsh_completions_dir}/gradle-completion.plugin.zsh
%{zsh_completions_dir}/_gradle

%changelog
* Mon Feb 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
