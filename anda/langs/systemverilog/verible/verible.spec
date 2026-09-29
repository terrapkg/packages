%global debug_package %{nil}
%global raw_version 0.0-4296-g0f262651

Name:        verible
Version:     0.0~4296~g0f262651
Release:     1%{?dist}
Summary:     SystemVerilog development tool suite, including a parser, formatter, linter, and language server
License:     Apache
URL:         https://chipsalliance.github.io/verible/
Source0:     https://github.com/chipsalliance/verible/archive/refs/tags/v%{raw_version}.tar.gz

BuildRequires: bazel
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: bison

Recommends:    %{name}-format = %{evr}
Recommends:    %{name}-lint = %{evr}
Recommends:    %{name}-syntax = %{evr}
Recommends:    %{name}-ls = %{evr}
Recommends:    %{name}-diff = %{evr}
Recommends:    %{name}-kythe = %{evr}
Recommends:    %{name}-obfuscate = %{evr}
Recommends:    %{name}-preprocessor = %{evr}
Recommends:    %{name}-project = %{evr}

Packager:      Cypress Reed <cypress@fyralabs.com>

%description
%{summary}.

%package format
Summary:       Verible SystemVerilog formatter
Requires:      %{name} = %{evr}

%description format
Verible tool for formatting SystemVerilog source code.

%package lint
Summary:       Verible SystemVerilog linter
Requires:      %{name} = %{evr}

%description lint
Verible tool for checking SystemVerilog source code against style rules.

%package syntax
Summary:       Verible SystemVerilog syntax parser
Requires:      %{name} = %{evr}

%description syntax
Verible tool for parsing SystemVerilog source code and displaying its syntax
structure.

%package ls
Summary:       Verible SystemVerilog language server
Requires:      %{name} = %{evr}

%description ls
Verible language server implementing the Language Server Protocol for
SystemVerilog.

%package diff
Summary:       Verible SystemVerilog lexical diff tool
Requires:      %{name} = %{evr}

%description diff
Verible tool for comparing SystemVerilog files while ignoring formatting
differences.

%package kythe
Summary:       Verible Kythe source index extractor
Requires:      %{name} = %{evr}

%description kythe
Verible tool for extracting Kythe indexing facts from SystemVerilog source.

%package obfuscate
Summary:       Verible SystemVerilog obfuscator
Requires:      %{name} = %{evr}

%description obfuscate
Verible tool for obfuscating identifiers in SystemVerilog source code.

%package preprocessor
Summary:       Verible SystemVerilog preprocessor
Requires:      %{name} = %{evr}

%description preprocessor
Verible preprocessor-like tool for SystemVerilog source code.

%package project
Summary:       Verible SystemVerilog project tool
Requires:      %{name} = %{evr}

%description project
Verible tool for analyzing and transforming whole SystemVerilog projects.

%prep
%autosetup -C

%build
bazel build --announce_rc --strip=always \
    --//bazel:use_local_flex_bison \
    //verible/verilog/tools/formatter:verible-verilog-format \
    //verible/verilog/tools/lint:verible-verilog-lint \
    //verible/verilog/tools/syntax:verible-verilog-syntax \
    //verible/verilog/tools/ls:verible-verilog-ls \
    //verible/verilog/tools/diff:verible-verilog-diff \
    //verible/verilog/tools/kythe:verible-verilog-kythe-extractor \
    //verible/verilog/tools/obfuscator:verible-verilog-obfuscate \
    //verible/verilog/tools/preprocessor:verible-verilog-preprocessor \
    //verible/verilog/tools/project:verible-verilog-project

%install
install -Dm0755 bazel-bin/verible/verilog/tools/formatter/verible-verilog-format \
    %{buildroot}%{_bindir}/verible-verilog-format
install -Dm0755 bazel-bin/verible/verilog/tools/lint/verible-verilog-lint \
    %{buildroot}%{_bindir}/verible-verilog-lint
install -Dm0755 bazel-bin/verible/verilog/tools/syntax/verible-verilog-syntax \
    %{buildroot}%{_bindir}/verible-verilog-syntax
install -Dm0755 bazel-bin/verible/verilog/tools/ls/verible-verilog-ls \
    %{buildroot}%{_bindir}/verible-verilog-ls
install -Dm0755 bazel-bin/verible/verilog/tools/diff/verible-verilog-diff \
    %{buildroot}%{_bindir}/verible-verilog-diff
install -Dm0755 bazel-bin/verible/verilog/tools/kythe/verible-verilog-kythe-extractor \
    %{buildroot}%{_bindir}/verible-verilog-kythe-extractor
install -Dm0755 bazel-bin/verible/verilog/tools/obfuscator/verible-verilog-obfuscate \
    %{buildroot}%{_bindir}/verible-verilog-obfuscate
install -Dm0755 bazel-bin/verible/verilog/tools/preprocessor/verible-verilog-preprocessor \
    %{buildroot}%{_bindir}/verible-verilog-preprocessor
install -Dm0755 bazel-bin/verible/verilog/tools/project/verible-verilog-project \
    %{buildroot}%{_bindir}/verible-verilog-project

%files
%license LICENSE
%doc README.md CONTRIBUTING.md doc/*

%files format
%{_bindir}/verible-verilog-format

%files lint
%{_bindir}/verible-verilog-lint

%files syntax
%{_bindir}/verible-verilog-syntax

%files ls
%{_bindir}/verible-verilog-ls

%files diff
%{_bindir}/verible-verilog-diff

%files kythe
%{_bindir}/verible-verilog-kythe-extractor

%files obfuscate
%{_bindir}/verible-verilog-obfuscate

%files preprocessor
%{_bindir}/verible-verilog-preprocessor

%files project
%{_bindir}/verible-verilog-project

%changelog
* Tue Sep 29 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
