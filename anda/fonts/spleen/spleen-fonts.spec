%global debug_package %nil
%global __make bmake
%global _make_output_sync %nil

Name:			spleen-fonts
Version:		2.1.0
Release:		1%?dist
Summary:		Monospaced bitmap fonts
License:		BSD-2-Clause
URL:			https://www.cambus.net/spleen-monospaced-bitmap-fonts/
Source0:		https://github.com/fcambus/spleen/archive/refs/tags/%version.zip
#Patch0:			https://github.com/fcambus/spleen/pull/42.patch
BuildRequires:	bmake fontforge
BuildRequires:	bdf2sfd
BuildArch:		noarch

%description
%summary.

%prep
%autosetup -n spleen-%version

%build
%make_build sfd
%make_build otf

%install
install -Dm644 fonts.alias *.otf -t %buildroot%_fontbasedir/%name/

%files
%license LICENSE
%doc FAQ ChangeLog AUTHORS README.md
%_fontbasedir/%name/
