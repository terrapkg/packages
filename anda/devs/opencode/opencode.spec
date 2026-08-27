# opencode ships a Bun-compiled standalone binary; stripping corrupts its
# embedded app data, so disable debuginfo/strip.
%define debug_package %{nil}
%global __strip /bin/true

%ifarch x86_64
%global a x64
%elifarch aarch64
%global a arm64
%endif

ExclusiveArch:  x86_64 aarch64

%global appid ai.opencode.opencode

Name:			opencode-cli
Version:		1.18.23
Release:		1%{?dist}
Summary:		Open source AI coding agent for the terminal, IDE, and desktop
License:		MIT
URL:			https://opencode.ai
Source0:		https://github.com/anomalyco/opencode/archive/refs/tags/v%{version}.tar.gz
Source1:		%{appid}.metainfo.xml
Packager:		Caio Bruno <cbrunofb@gmail.com>
Obsoletes:  opencode <= 1.18.18-1

BuildRequires:	bun-bin gcc-c++ make python3 python-unversioned-command nodejs-npm

%description
opencode is an open source AI coding agent that helps you write code in your
terminal, IDE, or desktop. It supports 75+ LLM providers (including local
models), LSP integration, multi-session workflows, GitHub Copilot and ChatGPT
login, and the Model Context Protocol (MCP).

%pkg_completion -Bfz opencode

%prep
%autosetup -n opencode-%{version}

%build
# Provide node-gyp for native modules (tree-sitter-*) when no prebuilt matches.
export npm_config_prefix=%{_builddir}/.npm-global
%__npm install -g node-gyp
export PATH=%{_builddir}/.npm-global/bin:$PATH

%__bun install
cd packages/opencode
OPENCODE_VERSION=%{version} OPENCODE_CHANNEL=latest %__bun run script/build.ts --single --skip-install

%install
export HOME=%{_builddir}/oc-home
mkdir -p "$HOME"

BIN=packages/opencode/dist/opencode-linux-%{a}/bin/opencode
install -Dpm755 "$BIN" %{buildroot}%{_bindir}/opencode

"$BIN" completion bash > opencode.bash
"$BIN" completion zsh  > _opencode
"$BIN" completion fish > opencode.fish
install -Dm644 opencode.bash %{buildroot}%{bash_completions_dir}/opencode
install -Dm644 _opencode     %{buildroot}%{zsh_completions_dir}/_opencode
install -Dm644 opencode.fish %{buildroot}%{fish_completions_dir}/opencode.fish

%terra_appstream -o %{SOURCE1}

%files
%license LICENSE
%doc README.md
%lang(ar) %doc README.ar.md
%lang(bn) %doc README.bn.md
%lang(pt_BR) %doc README.br.md
%lang(bs) %doc README.bs.md
%lang(da) %doc README.da.md
%lang(de) %doc README.de.md
%lang(es) %doc README.es.md
%lang(fr) %doc README.fr.md
%lang(el) %doc README.gr.md
%lang(it) %doc README.it.md
%lang(ja) %doc README.ja.md
%lang(ko) %doc README.ko.md
%lang(nb) %doc README.no.md
%lang(pl) %doc README.pl.md
%lang(ru) %doc README.ru.md
%lang(th) %doc README.th.md
%lang(tr) %doc README.tr.md
%lang(uk) %doc README.uk.md
%lang(vi) %doc README.vi.md
%lang(zh_CN) %doc README.zh.md
%lang(zh_TW) %doc README.zht.md
%{_bindir}/opencode
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Thu Jul 30 2026 Caio Bruno <cbrunofb@gmail.com>
- Build from source
