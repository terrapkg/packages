Name:           flow-control
Epoch:          1
Version:        0.3.3
Release:        1%?dist
Summary:        A programmer's text editor
License:        MIT
URL:            https://github.com/neurocyte/flow
Source0:        %url/archive/v%version.tar.gz
BuildRequires:  zig
Provides:       flow = %epoch:%version-%release
Obsoletes:      flow-control-nightly < 20250212.9999999


%description
%summary.

%prep
%autosetup -n flow-%version

%build
zig build -Doptimize=ReleaseFast --release=fast

%install
install -Dpm755 zig-out/bin/flow %buildroot%_bindir/flow

%files
%doc README.md help.md
%license LICENSE
%_bindir/flow
