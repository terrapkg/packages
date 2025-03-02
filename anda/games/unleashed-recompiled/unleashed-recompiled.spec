Name:			unleashed-recompiled
Version:		1.0.0
Release:		1%?dist
Summary:		An unofficial PC port of the Xbox 360 version of Sonic Unleashed created through the process of static recompilation
License:		GPL-3.0-only
URL:			https://github.com/hedge-dev/UnleashedRecomp
%dnl Source0:        %url/archive/refs/tags/v%version.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	anda-srpm-macros cmake

%description
Unleashed Recompiled is an unofficial PC port of the Xbox 360 version of Sonic Unleashed created through the process of static recompilation. The port offers Windows and Linux support with numerous built-in enhancements such as high resolutions, ultrawide support, high frame rates, improved performance and modding.

%prep
%git_clone %url v%version

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license COPYING
