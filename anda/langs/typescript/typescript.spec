%if 0%{?rhel}
Name:           typescript
Version:        5.7.3
Release:        %autorelease
Summary:        A language for application scale JavaScript development
License:        Apache-2.0
URL:            https://www.typescriptlang.org
Source:         https://registry.npmjs.org/typescript/-/typescript-%{version}.tgz
BuildArch:      noarch

BuildRequires:  nodejs
BuildRequires:  nodejs-packaging

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
TypeScript is a language for application-scale JavaScript. TypeScript adds
optional types to JavaScript that support tools for large-scale JavaScript
applications for any browser, for any host, on any OS. TypeScript compiles to
readable, standards-based JavaScript.

%prep
%autosetup -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/typescript
cp -pr package.json bin/ lib/ %{buildroot}%{nodejs_sitelib}/typescript

mkdir -p %{buildroot}%{_bindir}
ln -s ../lib/node_modules/typescript/bin/tsc %{buildroot}%{_bindir}/tsc
ln -s ../lib/node_modules/typescript/bin/tsserver %{buildroot}%{_bindir}/tsserver

%check
%{__nodejs} -e 'require("./")'


%files
%license LICENSE.txt
%{nodejs_sitelib}/typescript
%{_bindir}/tsc
%{_bindir}/tsserver

%changelog
* Wed Mar 18 2026 Owen Zimmerman <owen@fyralabs.com> - 5.7.3-1
- Port from Fedora EPEL9 spec
%endif
