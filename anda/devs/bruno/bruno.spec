# the bundled node_modules ship scripts with all kinds of shebangs
%undefine __brp_mangle_shebangs

Name:           bruno
%electronmeta -D
Version:        4.1.0
Release:        1%{?dist}
Summary:        Open source API client for exploring and testing APIs
License:        MIT AND %{electron_license}
URL:            https://www.usebruno.com
Source0:        https://github.com/usebruno/%{name}/archive/refs/tags/v%{version}.tar.gz

# Electron dlopens this for safeStorage, so it is not picked up automatically
Requires:       libsecret

%description
Bruno is a fast and Git-friendly API client. Collections are stored as plain
files inside a directory of your choosing, so requests can be versioned
alongside the code they test instead of living in a cloud account.

%prep
%autosetup

# husky only works inside a Git work tree, and we build from a tarball
%{__sed} -i 's/"prepare": "husky"/"prepare": "true"/' package.json

# RPM does the packaging, so stop Electron Builder at the unpacked directory
%{__sed} -i 's/--linux AppImage/--linux dir/' packages/bruno-electron/package.json

%build
export HOME=%{rpmbuilddir}
# upstream installs over the workspace's peer dependency conflicts, see contributing.md
export NPM_CONFIG_LEGACY_PEER_DEPS=true
export NODE_OPTIONS="--max-old-space-size=4096"

%{__npm} install

# build order taken from scripts/setup.js
%{__npm} run build:graphql-docs
%{__npm} run build:bruno-query
%{__npm} run build:bruno-common
%{__npm} run build:bruno-converters
%{__npm} run build:bruno-requests
%{__npm} run build:schema-types
%{__npm} run build:bruno-filestore
%{__npm} run sandbox:bundle-libraries --workspace=packages/bruno-js

%{__npm} run build:web
%{__npm} run build:electron:linux

%install
install -dm755 %{buildroot}%{_libdir}/%{name}
cp -pr packages/bruno-electron/out/linux*-unpacked/. %{buildroot}%{_libdir}/%{name}/
chmod 4755 %{buildroot}%{_libdir}/%{name}/chrome-sandbox

install -dm755 %{buildroot}%{_bindir}
ln -sf %{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

for size in 16 24 32 48 64 128 256 512 1024; do
	install -Dm644 packages/bruno-electron/resources/icons/png/${size}x${size}.png \
		%{buildroot}%{_hicolordir}/${size}x${size}/apps/%{name}.png
done

cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=Bruno
Comment=%{summary}
Exec=%{name} --ozone-platform-hint=auto %U
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;WebDevelopment;
Keywords=api;rest;graphql;grpc;http;client;
StartupWMClass=Bruno
MimeType=x-scheme-handler/bruno;
EOF

%desktop_file_install %{name}.desktop

%files
%doc readme.md
%license license.md
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_appsdir}/%{name}.desktop
%{_hicolordir}/*/apps/%{name}.png

%changelog
* Thu Jul 30 2026 NichSchlagen <tim-rosenhagen@web.de>
- Initial package, based on the work in #1253
