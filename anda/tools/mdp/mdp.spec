Name:           mdp
Version:        1.0.18
Release:        1%{?dist}
Summary:        A command-line based markdown presentation tool. 
Packager:       Jan200101 <sentrycraft123@gmail.com>

License:        GPL-3.0-only
URL:            https://github.com/visit1985/mdp
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  ncurses-devel

%description
A command-line based markdown presentation tool. 

%prep
%autosetup


%build
%{set_build_flags}
%make_build


%install
%make_install PREFIX="%{_prefix}"


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%license COPYING

%changelog
* Sun Jul 05 2026 Jan200101 <sentrycraft123@gmail.com> - 1.0.18-1
- Package mdp
