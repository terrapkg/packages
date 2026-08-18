%define debug_package %nil
%global gem_name colorls

Name:           colorls
Version:        1.5.0
Release:        1%?dist
Summary:        A Ruby gem that beautifies the terminal's ls command, with color and font-awesome icons
License:        MIT
URL:            https://github.com/athityakumar/colorls
Source0:        https://rubygems.org/downloads/colorls-1.5.0.gem
BuildRequires:  rubygems-devel

%description
A Ruby script that colorizes the ls output with color and icons.

%pkg_completion -z

%prep
%autosetup

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
install -Dm755 exe/colorls -t %buildroot%_bindir
install -Dm644 man/colorls.1 -t %buildroot%_mandir/man1
install -Dm755 zsh/_colorls -t %buildroot%zsh_completions_dir

%files
%_bindir/colorls
%_mandir/man1/colorls.1.*
