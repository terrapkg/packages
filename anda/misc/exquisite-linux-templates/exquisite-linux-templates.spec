%global commit 4f5ee4e125a5c202c30b620d8df4cb1a1494e8cd
%global shortcommit %{sub %commit 1 7}
%global commit_date 20250516

Name:		exquisite-linux-templates
Version:	0~%{commit_date}git.%shortcommit
Release:	1%?dist
Summary:	A collection of shared file templates for use in $HOME/Templates on Linux systems
License:	MIT
URL:		https://codeberg.org/nathandyer/%name
Source0:	%url/archive/%commit.tar.gz
BuildArch:	noarch

%description
%summary.

Note that this only works with English. You should rename `~/Templates` to the corresponding
string for your user language for the templates to take effect.

%prep
%autosetup -n %name

%install
mkdir -p %buildroot%_sysconfdir/skel/Templates
mv templates %buildroot%_sysconfdir/skel/Templates/%name

%files
%doc README.md
%license LICENSE
%_sysconfdir/skel/Templates
