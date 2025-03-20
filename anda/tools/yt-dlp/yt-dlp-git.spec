#bcond_without tests
%global oldpkgname yt-dlp-nightly

Name:           yt-dlp-git
Version:        2025.03.16.221236
Release:        1%?dist
Summary:        A command-line program to download videos from online video platforms

License:        Unlicense
URL:            https://github.com/yt-dlp/yt-dlp
# License of the specfile
Source:         https://src.fedoraproject.org/rpms/yt-dlp/raw/rawhide/f/yt-dlp.spec.license

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)

%if %{with tests}
# Needed for %%check
BuildRequires:  %{py3_dist pytest}
%endif

# Needed for docs
BuildRequires:  pandoc
BuildRequires:  make

BuildRequires:  anda-srpm-macros

# ffmpeg-free is now available in Fedora.
Recommends:     /usr/bin/ffmpeg
Recommends:     /usr/bin/ffprobe

Conflicts:      yt-dlp

Suggests:       python3dist(keyring)

Provides:       %{oldpkgname} = 1:0-1%?dist
Obsoletes:      %{oldpkgname} < 0:20250117.git~1643686-2%?dist

%global _description %{expand:
yt-dlp is a command-line program to download videos from many different online
video platforms, such as youtube.com. The project is a fork of youtube-dl with
additional features and fixes.}

%description %{_description} This package is built from the yt-dlp master branch.

%package bash-completion
Summary:        Bash completion for yt-dlp
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

Conflicts:      yt-dlp-bash-completion
Provides:       %{oldpkgname}-bash-completion = 1:0-1%?dist
Obsoletes:      %{oldpkgname}-bash-completion < 0:20250117.git~1643686-2%?dist

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)

Conflicts:      yt-dlp-zsh-completion
Provides:       %{oldpkgname}-zsh-completion = 1:0-1%?dist
Obsoletes:      %{oldpkgname}-zsh-completion < 0:20250117.git~1643686-2%?dist

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       fish
Supplements:    (%{name} and fish)

Conflicts:      yt-dlp-fish-completion
Provides:       %{oldpkgname}-fish-completion = 1:0-1%?dist
Obsoletes:      %{oldpkgname}-fish-completion < 0:20250117.git~1643686-2%?dist

%description fish-completion
Fish command line completion support for %{name}.

%prep
%git_clone %{url} master

# Remove unnecessary shebangs
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
# Relax version constraints
sed -i 's@"\(requests\|urllib3\|websockets\)>=.*"@"\1"@' pyproject.toml

# Update version number
%{python3} devscripts/update-version.py %{version} -c master -r yt-dlp/yt-dlp-master-builds

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
