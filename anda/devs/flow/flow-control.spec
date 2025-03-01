Name:           flow-control
Epoch:          1
Version:        0.3.3
Release:        1%?dist
Summary:        A programmer's text editor
License:        MIT
URL:            https://github.com/neurocyte/flow
BuildRequires:  zig
BuildRequires:  anda-srpm-macros
Provides:       flow = %epoch:%version-%release
Obsoletes:      flow-control-nightly < 20250212.9999999

%description
%summary.

%prep
%git_clone %url v%version

%build
zig build -Doptimize=ReleaseFast --release=fast

%install
install -Dpm755 zig-out/bin/flow %buildroot%_bindir/flow

%files
%doc README.md help.md
%license LICENSE
%_bindir/flow
