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

Name:			opencode
Version:		1.18.9
Release:		1%{?dist}
Summary:		Open source AI coding agent for the terminal, IDE, and desktop
License:		MIT
URL:			https://opencode.ai
Source0:		https://github.com/anomalyco/opencode/archive/refs/tags/v%{version}.tar.gz
Source1:		%{appid}.metainfo.xml
Packager:		Caio Bruno <cbrunofb@gmail.com>

BuildRequires:	bun-bin gcc-c++ make python3

%description
opencode is an open source AI coding agent that helps you write code in your
terminal, IDE, or desktop. It supports 75+ LLM providers (including local
models), LSP integration, multi-session workflows, GitHub Copilot and ChatGPT
login, and the Model Context Protocol (MCP).

%pkg_completion -Bfz opencode

%prep
%autosetup -n opencode-%{version}

%build
%__bun install
cd packages/opencode
OPENCODE_VERSION=%{version} OPENCODE_CHANNEL=latest %__bun run script/build.ts --single --skip-install

%install
export HOME=%{_builddir}/oc-home
mkdir -p "$HOME"

BIN=packages/opencode/dist/opencode-linux-%{a}/bin/opencode
install -Dpm755 "$BIN" -t %{buildroot}%{_bindir}

"$BIN" completion bash > opencode.bash
"$BIN" completion zsh  > _opencode
"$BIN" completion fish > opencode.fish
install -Dm644 opencode.bash %{buildroot}%{bash_completions_dir}/opencode
install -Dm644 _opencode     %{buildroot}%{zsh_completions_dir}/_opencode
install -Dm644 opencode.fish %{buildroot}%{fish_completions_dir}/opencode.fish

%terra_appstream -o %{SOURCE1}

%files
%license LICENSE
%{_bindir}/opencode
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Thu Jul 30 2026 Caio Bruno <cbrunofb@gmail.com>
- Build from source instead of the prebuilt binary
* Wed Jul 29 2026 Caio Bruno <cbrunofb@gmail.com>
- Initial package
