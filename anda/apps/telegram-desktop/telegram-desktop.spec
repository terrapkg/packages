Name:			telegram-desktop
Version:		6.2.3
Release:		1%?dist
Summary:		Telegram Desktop messaging app
License:		GPL-3.0-or-later WITH OpenSSL-exception
URL:			https://desktop.telegram.org
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	boost-regex
BuildRequires:	cmake
BuildRequires:	cmake(ada)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(OpenAL)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(opus)

%description
%summary.

%prep
%git_clone https://github.com/telegramdesktop/tdesktop v%version

%build
%cmake -DTD_E2E_ONLY=ON -DDESKTOP_APP_DISABLE_AUTOUPDATE=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md changelog.txt
%license LICENSE LEGAL
