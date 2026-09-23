Name:           ocaml-ppx-module-timer
Version:        0.17.0
Release:        1%{?dist}
Summary:        instrumentation to record ppx startup time

License:        MIT
URL:            https://github.com/janestreet/ppx_module_timer
Source:         %{url}/archive/v%{version}/ppx_module_timer-%{version}.tar.gz

BuildSystem:    dune
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-time-now-devel
BuildRequires:  ocaml-stdio-devel
BuildRequires:  ocaml-ppx-base-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Modules using ppx_module_timer (included in ppx_jane_kernel)
now have instrumentation to record their startup time.
If the environment variable PPX_MODULE_TIMER is set (to anything),
each module records its startup time, and before exiting the
process prints out all of the module times in the order they occurred.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{evr}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -C

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.17.0-1
- Initial commit
