%global forgeurl https://github.com/jhawthorn/fzy
Version:        1.1
%forgemeta

Name:           fzy
Release:        2%{?dist}
Summary:        A fast, simple fuzzy text selector for the terminal

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

Packager:       Olivia <git@olivia.sh>

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
* Sun Jul 19 2026 Olivia <git@olivia.sh> - 1.1-2
- Update packager

* Mon Mar 23 2026 Olivia <git@olivia.sh>
- Initial package
