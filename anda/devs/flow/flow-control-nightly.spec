%global commit 447b735c0b18fcd0abc451b39a071b2ebe6a9026
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240903

Name:           flow-control-nightly
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        A programmer's text editor 
License:        MIT
URL:            https://github.com/neurocyte/flow
Source0:        %url/archive/%commit.tar.gz
BuildRequires:  zig
Provides:       flow = %version-%release

%description
%summary.

%prep
%autosetup -n flow-%commit

%build
zig build -Doptimize=ReleaseFast --release=fast

%install
install -Dpm755 zig-out/bin/flow %buildroot%_bindir/flow

%files
%doc README.md help.md
%license LICENSE
%_bindir/flow
