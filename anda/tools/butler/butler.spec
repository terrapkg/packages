Name:           butler
Version:        15.24.0
Release:        1%?dist
Summary:        Command-line itch.io helper.
URL:            https://itch.io/docs/butler/
Source0:        https://broth.itch.zone/${name}/linux-amd64/${version}/signature/default
License:        MIT
BuildRequires:  golang 7zip
Provides: itchio-butler
Provides: itch-butler

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%summary.

%prep
curl -L -o ${name}.zip %{SOURCE0}
unzip ${name}.zip

%build

%install
install -Dm755 target/rpm/${name} %{buildroot}%{_bindir}/${name}

%files
%doc README.md
%license LICENSE
%{_bindir}/${name}

%changelog
* Sat Nov 22 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
