%define debug_package %nil
%define __strip /bin/true
%global commit 5aadc307cb9bf4479f0a12364a253b07a77ace22

Name:			arrpc
Version:		3.5.0
Release:		1%?dist
Summary:		Open Discord RPC server for atypical setups
License:		MIT
URL:			https://arrpc.openasar.dev
Source0:		https://github.com/OpenAsar/arrpc/archive/%commit.tar.gz
Source1:		arrpc.service
Patch0:			0001-fix-support-esbuild.patch
Requires:		glibc
BuildRequires:	nodejs-npm systemd-rpm-macros

%description
arRPC is an open source implementation of Discord's half-documented local RPC servers for their desktop client.
This open source implementation purely in NodeJS allows it to be used in many places where it is otherwise
impossible to do: Discord web and alternative clients like ArmCord/etc. It opens a simple bridge WebSocket
server which messages the JSON of exactly what to dispatch with in the client with no extra processing needed,
allowing small and simple mods or plugins. arRPC is experimental and a work in progress, so expect bugs, etc.

%prep
%autosetup -n arrpc-%commit -p1
# patch for using esbuild
sed -i -E 's@const server[^\n]+;@async function main() {\0@' src/index.js
sed -i -E 's@server\.on[^\n]+;@\0}\nmain();@' src/index.js

%build
npm i esbuild @yao-pkg/pkg
npx esbuild --bundle --platform=node --target=node20 --outdir=dist ./src/index.js
npx pkg -t node20-linux-x64 -o arrpc ./dist/index.js

%install
install -D -m755 arrpc %buildroot%_bindir/arrpc
install -D -m644 %SOURCE1 %buildroot%_userunitdir/arrpc.service

%post
%systemd_user_post arrpc.service

%preun
%systemd_user_preun arrpc.service

%postun
%systemd_user_postun_with_restart arrpc.service

%files
%doc README.md
%license LICENSE
%_bindir/arrpc
%_userunitdir/arrpc.service

%changelog
%autochangelog
