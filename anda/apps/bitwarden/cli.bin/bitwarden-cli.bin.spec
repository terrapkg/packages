Name:           bitwarden-cli.bin
Version:        2026.1.0
Release:        1%?dist
Summary:        Bitwarden command-line client
License:        GPL-3.0-only
URL:            https://bitwarden.com
Source0:        https://github.com/bitwarden/clients/releases/download/cli-v%version/bw-oss-linux-%version.zip

Packager:       madonuko <mado@fyralabs.com>
Provides:       bw
ExclusiveArch:  x86_64

BuildRequires:  unzip

%description
%summary.

%prep
unzip %{S:0}

%install
install -Dpm755 bw -t %buildroot%_bindir

%files
%_bindir/bw
