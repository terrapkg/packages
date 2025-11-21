%global commit eefaa6b0fbf911877d0aa8a863fd08fc8cd1a1a2
%global commit_date 20251121
%global shortcommit %{sub %commit 1 7}

Name:			grabnim
Version:		0~%{commit_date}git.%{shortcommit}
Release:		1%?dist
Summary:		Simple tool to install and manage multiple nim compiler versions
License:		MIT
URL:			https://codeberg.org/janAkali/grabnim
Source0:		%url/archive/%commit.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	nim

%description
GrabNim is a simple tool to install, manage and switch between different versions of the Nim compiler.

%prep
%autosetup -n %name

%build
%nim_c %name

%install
install -Dm755 %name -t %buildroot%_bindir

%files
%doc README.md
%license LICENSE
%_bindir/%name
