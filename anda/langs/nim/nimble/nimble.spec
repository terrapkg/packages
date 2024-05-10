Name:           nimble
Version:        0.14.2
Release:        1%?dist
Summary:        Package manager for the Nim programming language
License:        BSD
URL:            https://github.com/nim-lang/nimble
Source1:        nimble.1
# We use `nim` to get `nimble`… to build `nimble`
BuildRequires:  nim anda-srpm-macros git-core
Conflicts:      nim

%description
%summary.

%prep
git clone %url .
git checkout v%version

%build
nimble setup -y
nim c %nim_c src/nimble

%install
install -Dpm755 src/nimble %buildroot%_bindir/nimble
install -Dpm644 -t%buildroot%_mandir/man1 %SOURCE1
install -Dpm644 nimble.bash-completion %bash_completions_dir/nimble
install -Dpm644 nimble.zsh-completion %zsh_completions_dir/_nimble.zsh

%files
%doc readme.markdown
%license license.txt
%_bindir/nimble
%_mandir/man1/nimble.1
%bash_completions_dir/nimble
%zsh_completions_dir/_nimble.zsh

%changelog
%autochangelog
