%global goipath github.com/jesseduffield/lazygit

Name:           lazygit
Version:        0.59.0
Release:        1%?dist
Summary:        Simple terminal UI for git commands
License:        MIT
URL:            https://github.com/jesseduffield/lazygit
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang go-rpm-macros go-md2man
Requires:       git-core
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Simple, pragmatic TUI (Terminal UI) frontend for GIT. Written in Go with the
gocui library.

From the official GIT repository:

Rant time: You've heard it before, git is powerful, but what good is that
power when everything is so damn hard to do? Interactive rebasing requires you
to edit a goddamn TODO file in your editor? Are you kidding me? To stage part
of a file you need to use a command line program to step through each hunk and
if a hunk can't be split down any further but contains code you don't want to
stage, you have to edit an arcane patch file by hand? Are you KIDDING me?!
Sometimes you get asked to stash your changes when switching branches only to
realise that after you switch and unstash that there weren't even any
conflicts and it would have been fine to just checkout the branch directly?
YOU HAVE GOT TO BE KIDDING ME!

If you're a mere mortal like me and you're tired of hearing how powerful git
is when in your daily life it's a powerful pain in your ass, lazygit might be
for you.

%package        doc
Summary:        Documentations for %{name}
Requires:       %{name} = %{evr}
BuildArch:      noarch

%description    doc
%{summary}.

%prep
%autosetup
%goprep

%build
export GO111MODULE=on
%gobuild -o %{gobuilddir}/lazygit
go-md2man -in README.md -out lazygit.1

%install
install -Dm755 %{gobuilddir}/lazygit %{buildroot}%{_bindir}/lazygit
install -Dpm644 lazygit.1 %{buildroot}/%{_mandir}/man1/lazygit.1

%files
%doc README.md
%license LICENSE
%{_bindir}/lazygit
%{_mandir}/man1/lazygit.1.*

%files doc
%doc VISION.md CONTRIBUTING.md CODE-OF-CONDUCT.md docs/

%changelog
* Mon Feb 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
