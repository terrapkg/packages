%global npm_name signal-styler

Name:			signal-styler
Version:		1.2.0
Release:		1%{?dist}
Summary:		Apply custom CSS themes to Signal Desktop
SourceLicense:	GPL-3.0-only
License:		GPL-3.0-only AND MIT AND PSF-2.0 AND BlueOak-1.0.0
URL:			https://github.com/m-obeid/signal-styler
Recommends:     signal-desktop
Requires:		nodejs
BuildRequires:	anda-srpm-macros
BuildRequires:	nodejs-npm
BuildRequires:	nodejs-packaging
BuildRequires:	nodejs-license-checker
BuildArch:		noarch

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%npm_prep

%build

%install
%npm_license -o LICENSE.modules
%npm_install
%{__ln_s} -f %{nodejs_sitelib}/%{npm_name}/index.js %{buildroot}%{_bindir}/%{npm_name}

%files
%doc README.md
%license LICENSE LICENSE.modules
%{_bindir}/%{npm_name}
%{nodejs_sitelib}/%{npm_name}/

%changelog
* Thu Oct 15 2026 Its-J <jonah@fyralabs.com> - 1.2.0-1
- Initial commit
