%global goipath github.com/jesseduffield/lazygit

Name:           lazygit
Version:        0.59.0
Release:        1%?dist
Summary:        Simple terminal UI for git commands
License:        MIT
URL:            https://github.com/jesseduffield/lazygit
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang go-rpm-macros
Requires:       git-core
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
lazygit is a terminal UI for git commmands that helps make common and complex
git operations easy and accessible without requiring expertise with the git
command line.

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
%gobuild -o %{gobuilddir}/%{name}

%install
install -Dm755 %{gobuilddir}/lazygit %{buildroot}%{_bindir}/lazygit

%files
%doc README.md
%license LICENSE
%{_bindir}/lazygit

%files doc
%doc VISION.md CONTRIBUTING.md CODE-OF-CONDUCT.md docs/

%changelog
* Mon Feb 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
