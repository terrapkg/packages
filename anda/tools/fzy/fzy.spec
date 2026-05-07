%global forgeurl https://github.com/jhawthorn/fzy
Version:        1.1
%forgemeta

Name:           fzy
Release:        1%{?dist}
Summary:        A fast, simple fuzzy text selector for the terminal

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

Packager:       metcya <metcya@gmail.com>

BuildRequires:  gcc
BuildRequires:  make

%description
fzy is a fast, simple fuzzy text selector for the terminal with an advanced
scoring algorithm.

%prep
%forgeautosetup

%build
%make_build

%install
%make_install BINDIR="%{_bindir}" MANDIR="%{_mandir}"

%files
%license LICENSE
%doc README.md ALGORITHM.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Mon Mar 23 2026 metcya <metcya@gmail.com>
- Initial package
