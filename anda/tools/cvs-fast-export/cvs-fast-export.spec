Name:           cvs-fast-export
Version:        2.3
Release:        1%{?dist}
Summary:        Export an RCS or CVS history as a fast-import stream

License:        GPL-2.0-or-later
URL:            https://gitlab.com/esr/cvs-fast-export
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Packager:       Olivia <git@olivia.sh>

BuildRequires:  make
BuildRequires:  asciidoctor
BuildRequires:  go-rpm-macros

ExclusiveArch:  %{golang_arches_future}

%description
This program analyzes a collection of RCS files in a CVS repository
(or outside of one) and, when possible, emits an equivalent history in
the form of a fast-import stream.  Not all possible histories can be
rendered this way; the program tries to emit useful warnings when it
can’t.  The program can also produce a visualization of the resulting
commit DAG in the DOT format handled by the graphviz suite.

%prep
%autosetup

%build
%make_build all BINDIR=%{_bindir} DATADIR=%{_datadir} MANDIR=%{_mandir}

%install
%{__install} -d %{buildroot}%{_mandir}/man1
%make_install BINDIR=%{_bindir} DATADIR=%{_datadir} MANDIR=%{_mandir}

%files
%license COPYING
%doc README.adoc TODO.adoc
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Fri Jul 10 2026 Olivia <git@olivia.sh> - 2.3-1
- Add cvs-fast-export
