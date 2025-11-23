Name:           butler
Version:        15.24.0
Release:        1%?dist
Summary:        Command-line itch.io helper.
URL:            https://itch.io/docs/butler
Source0:        https://broth.itch.ovh/butler/linux-amd64/LATEST/archive/default
Source1:        https://raw.githubusercontent.com/itchio/butler/refs/heads/master/LICENSE
Source2:	https://raw.githubusercontent.com/itchio/butler/refs/heads/master/README.md
License:        MIT
BuildRequires:  anda-srpm-macros mold
Provides:  	itchio-butler
Provides: 	itch-butler

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%summary.

%prep
curl -L -o butler.zip https://broth.itch.ovh/butler/linux-amd64/LATEST/archive/default
unzip butler.zip

%build

%install
install -Dm755 butler %{buildroot}%{_bindir}/butler
install -Dm644 %{S:1} %{buildroot}%{_defaultlicensedir}/butler/LICENSE
install -Dm644 %{S:2} %{buildroot}%{_docdir}/butler/README.md

%files
%doc README.md
%license LICENSE
%{_bindir}/butler

%changelog
* Sat Nov 22 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
