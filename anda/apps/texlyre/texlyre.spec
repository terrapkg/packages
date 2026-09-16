%global npm_name texlyre
%global drawio_ver 31.4.4
%global busytex_ver 1.4.0

Name:           texlyre
Version:        0.12.0
Release:        1%{?dist}
Summary:        Local-first LaTeX and Typst web editor with real-time collaboration and offline support
License:        AGPL-3.0-only
URL:            https://github.com/TeXlyre/texlyre
Source0:        https://github.com/TeXlyre/texlyre/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/TeXlyre/drawio-embed-mirror/archive/refs/tags/v%{drawio_ver}.tar.gz
Source2:        https://github.com/TeXlyre/texlyre-busytex/archive/refs/tags/assets-v%{busytex_ver}.tar.gz
Packager:       Cypress Reed <cypress@fyralabs.com>

BuildRequires:  nodejs
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs-license-checker
BuildRequires:  python3
BuildRequires:  xsel
Requires:       nodejs-serve
Requires:       xsel
BuildArch:      noarch

%description
TeXlyre is a local-first LaTeX and Typst web editor with real-time collaboration and offline support.

%prep
%setup -q -n texlyre-%{version}
%setup -q -T -D -a 1
%setup -q -T -D -a 2

# The asset archives are extracted into versioned directories in the source tree.
mkdir -p public/core
a=$(find . -maxdepth 1 -type d -name 'drawio-embed-mirror-*' | head -n 1)
b=$(find . -maxdepth 1 -type d -name 'texlyre-busytex-*' | head -n 1)
cp -a "$a/drawio-embed" public/core/drawio-embed
cp -a "$b" public/core/busytex

sed -i 's/"version": ".*"/"version": "%{version}"/' package.json
sed -i "s#baseUrl: '/texlyre/'#baseUrl: '/'#" texlyre.config.ts
sed -i 's/await downloadCoreAssets();//' scripts/setup-assets.cjs

%build
%__npm ci
%__npm run generate:configs
%__npm run build

%check
%__npm run test:check

%npm_license -o LICENSE.modules

%install
mkdir -p %{buildroot}%{_datadir}/texlyre %{buildroot}%{_bindir}
cp -a dist/. %{buildroot}%{_datadir}/texlyre/
cat > %{buildroot}%{_bindir}/texlyre <<'EOF'
#!/bin/sh
exec /usr/bin/serve -s /usr/share/texlyre "$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/texlyre

%files
%license LICENSE* LICENSE.modules
%doc README.md
%{_bindir}/texlyre
%{_datadir}/texlyre/

%changelog
* Wed Sep 16 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
