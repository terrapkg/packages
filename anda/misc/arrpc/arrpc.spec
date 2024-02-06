%global commit c6e23e7eb733ad396d3eebc328404cc656fed581

Name:			arrpc
Version:		3.3.0
Release:		1%?dist
Summary:		Open Discord RPC server for atypical setups
License:		MIT
URL:			https://arrpc.openasar.dev
Source0:		https://github.com/OpenAsar/arrpc/archive/%commit.tar.gz
Source1:		arrpc.service
Requires:		gcc-libs glibc
BuildRequires:	nodejs-npm systemd-rpm-macros

%description
arRPC is an open source implementation of Discord's half-documented local RPC servers for their desktop client.
This open source implementation purely in NodeJS allows it to be used in many places where it is otherwise
impossible to do: Discord web and alternative clients like ArmCord/etc. It opens a simple bridge WebSocket
server which messages the JSON of exactly what to dispatch with in the client with no extra processing needed,
allowing small and simple mods or plugins. arRPC is experimental and a work in progress, so expect bugs, etc.

%prep
%autosetup -n arrpc-%commit
# patch for using esbuild
sed -i -E 's@const server[^\n]+;@async function main() {\0@' src/index.js
sed -i -E 's@server\.on[^\n]+;@\0}\nmain();@' src/index.js

%build
npm i esbuild pkg
npx esbuild --bundle --platform=node --target=node18 --outdir=dist ./src/index.js
npx pkg -t node18-linux-x64 -o arrpc  ./dist/index.js

%install
install -D -m755 arrpc %buildroot%_bindir/arrpc
install -D -m644 %SOURCE1 %buildroot%_userunitdir/arrpc.service

%files
%doc README.md
%license LICENSE
%_bindir/arrpc
%_userunitdir/arrpc.service

%changelog
%autochangelog
