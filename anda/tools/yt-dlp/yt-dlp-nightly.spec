#bcond_without tests
%global commit db50f19d76c6870a5a13d0cab9287d684fd7449a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240602
%global ver 2024.05.27

Name:           yt-dlp-nightly
Version:        %ver^%commit_date.%shortcommit
Release:        1%?dist
Summary:        A command-line program to download videos from online video platforms

License:        Unlicense
URL:            https://github.com/yt-dlp/yt-dlp
Source:         %url/archive/%commit.tar.gz
# License of the specfile
Source:         https://src.fedoraproject.org/rpms/yt-dlp/raw/rawhide/f/yt-dlp.spec.license

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
# Needed for %%check
BuildRequires:  %{py3_dist pytest}
%endif

# Needed for docs
BuildRequires:  pandoc
BuildRequires:  make

# ffmpeg-free is now available in Fedora.
Recommends:     /usr/bin/ffmpeg
Recommends:     /usr/bin/ffprobe

Provides:       yt-dlp
Conflicts:      yt-dlp

Suggests:       python3dist(keyring)

%global _description %{expand:
yt-dlp is a command-line program to download videos from many different online
video platforms, such as youtube.com. The project is a fork of youtube-dl with
additional features and fixes.}

%description %{_description}

%package bash-completion
Summary:        Bash completion for yt-dlp
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

Provides:       yt-dlp-bash-completion
Conflicts:      yt-dlp-bash-completion

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)

Provides:       yt-dlp-zsh-completion
Conflicts:      yt-dlp-zsh-completion

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       fish
Supplements:    (%{name} and fish)

Provides:       yt-dlp-fish-completion
Conflicts:      yt-dlp-fish-completion

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -n yt-dlp-%commit

# Remove unnecessary shebangs
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
# Relax version constraints
sed -i 's@"\(requests\|urllib3\|websockets\)>=.*"@"\1"@' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -r

%build
# Docs and shell completions
make yt-dlp.1 completion-bash completion-zsh completion-fish

# Docs and shell completions are also included in the wheel.
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files yt_dlp

%check
%if %{with tests}
# See https://github.com/yt-dlp/yt-dlp/blob/master/devscripts/run_tests.sh
%pytest -m 'not download'
%endif

%files -f %{pyproject_files}
%{_bindir}/yt-dlp
%{_mandir}/man1/yt-dlp.1*
%doc README.md
%license LICENSE

%files bash-completion
%{bash_completions_dir}/yt-dlp

%files zsh-completion
%{zsh_completions_dir}/_yt-dlp

%files fish-completion
%{fish_completions_dir}/yt-dlp.fish

%changelog
%autochangelog
