%global debug_package %{nil}

Name:           bazel
Version:        9.2.0
Release:        1%{?dist}
Summary:        Build and test software of any size, quickly and reliably
License:        Apache-2.0
URL:            https://bazel.build/
Source:         https://github.com/bazelbuild/bazel/releases/download/%{version}/bazel-%{version}-dist.zip
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zip
BuildRequires:  unzip
BuildRequires:  java-21-openjdk-devel
BuildRequires:  python

Packager:       Cypress Reed <cypress@fyralabs.com>

%bcond bootstrap 1
%if %{without bootstrap}
BuildRequires:  bazel
%endif


%description
%{summary}.

%prep
%setup -q -c -n %{name}-%{version}

%build
%if %{without bootstrap}
    echo "Using system Bazel for the build"
    bazel build //src:bazel //scripts:bazel-complete.bash \
        --tool_java_runtime_version=local_jdk \
        --compilation_mode=opt --stamp --embed_label=%{version}
%else
    echo "No system Bazel available; bootstrapping Bazel from the distribution"
    env EXTRA_BAZEL_ARGS="--tool_java_runtime_version=local_jdk" bash ./compile.sh
    ./output/bazel build //src:bazel //scripts:bazel-complete.bash \
        --compilation_mode=opt --stamp --embed_label=%{version}
%endif

%install
install -Dpm 0755 ./bazel-bin/src/bazel                   -t %{buildroot}%{_bindir}
install -Dpm 0644 ./bazel-bin/scripts/bazel-complete.bash    %{buildroot}%{bash_completions_dir}/%{name}.bash
install -Dpm 0644 ./scripts/zsh_completion/_bazel         -t %{buildroot}%{zsh_completions_dir}

%files
%{_bindir}/bazel
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md SECURITY.md docs/*
%license LICENSE

%pkg_completion -zb

%changelog
* Mon Sep 07 2026 Cypress Reed <cypress@fyralabs.com>
- Port to Terra from COPR https://github.com/lihaohong6/COPR
