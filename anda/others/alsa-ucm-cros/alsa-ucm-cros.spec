Name:			alsa-ucm-cros
Version:		0.3
Release:		1%?dist
Summary:		ALSA Use Case Manager configuration
License:		BSD-3-Clause
URL:			https://github.com/WeirdTreeThing/alsa-ucm-conf-cros/tree/standalone
Source0:		https://github.com/WeirdTreeThing/alsa-ucm-conf-cros/archive/refs/tags/%version.tar.gz

%description
%summary for chromebooks.

%prep
%autosetup -n alsa-ucm-conf-cros-%version

%build

%install
mkdir -p %buildroot%_datadir/alsa
cp ucm2/. %buildroot%_datadir/alsa/
ls -alh ucm2/

%files
%doc README.md
%license LICENSE
%_datadir/alsa/ucm2/*

%changelog
%autochangelog
