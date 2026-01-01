# uxn stable has no update script because this version
# is permanently frozen. A nightly will be added once the
# sourcehut versioning script is done.

%global debug_package %{nil}

Name:           uxn
Version:        1.0
Release:        1%?dist
Summary:        An emulator for the Varvara virtual machine
URL:            https://100r.ca/site/%{name}.html
Source0:        https://git.sr.ht/~rabbits/%{name}/archive/%{version}.tar.gz
License:        MIT
BuildRequires:  anda-srpm-macros SDL2-devel gcc libubsan libasan

Packager:       arbormoss <arbormoss@woodsprite.dev>

%description
%summary.

%prep
%autosetup -n %name-%version

%build
./build.sh

%install
install -Dm755 bin/%{name}asm %{buildroot}%{_bindir}/%{name}asm
install -Dm755 bin/%{name}cli %{buildroot}%{_bindir}/%{name}cli
install -Dm755 bin/%{name}emu %{buildroot}%{_bindir}/%{name}emu

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}asm
%{_bindir}/%{name}cli
%{_bindir}/%{name}emu

%changelog
* Sun Dec 21 2025 arbormoss <arbormoss@woodsprite.dev>
- Intial Commit
