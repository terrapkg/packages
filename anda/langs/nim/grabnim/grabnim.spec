%global commit 923731e4325dcd2ce38648f456873128b97ac395
%global commit_date 20250629
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
