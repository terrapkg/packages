%global debug_package %{nil}
%global __strip /bin/true

Name:           bazel
Version:        9.2.0
Release:        2%{?dist}
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
Requires:       /bin/bash

Packager:       Cypress Reed <cypress@fyralabs.com>

%global bootstrap 1

%if %{bootstrap} == 0
BuildRequires:  bazel
%endif


%description
%{summary}.

%prep
%setup -q -c -n %{name}-%{version}

# The distribution archive marks documentation executable and includes copies
# for every historical Bazel release.
rm -rf docs/versions
find README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md SECURITY.md LICENSE docs \
    -type f -exec chmod 0644 {} +

%build
%if %{bootstrap} == 0
    echo "Using system Bazel for the build"
    bazel build //src:bazel-bin //scripts:bazel-complete.bash \
        --host_platform=//:default_host_platform \
        --platforms=//:default_host_platform \
        --tool_java_runtime_version=local_jdk \
        --compilation_mode=opt --stamp --embed_label=%{version}
%else
    echo "No system Bazel available; bootstrapping Bazel from the distribution"
    env EXTRA_BAZEL_ARGS="--tool_java_runtime_version=local_jdk --host_platform=//:default_host_platform --platforms=//:default_host_platform" bash ./compile.sh
    rm -rf bazel-bin bazel-out
    ./output/bazel build //src:bazel-bin //scripts:bazel-complete.bash \
        --host_platform=//:default_host_platform \
        --platforms=//:default_host_platform \
        --compilation_mode=opt --stamp --embed_label=%{version}
%endif

%install
unzip -t ./bazel-bin/src/bazel >/dev/null
install -Dpm 0755 ./bazel-bin/src/bazel                    %{buildroot}%{_bindir}/bazel
install -Dpm 0644 ./bazel-bin/scripts/bazel-complete.bash %{buildroot}%{bash_completions_dir}/%{name}.bash
install -Dpm 0644 ./scripts/zsh_completion/_bazel         -t %{buildroot}%{zsh_completions_dir}

%files
%{_bindir}/bazel
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md SECURITY.md docs/*
%license LICENSE

%pkg_completion -zb

%changelog
* Sun Sep 20 2026 Cypress Reed <cypress@fyralabs.com>
- fix installation, make docs non-executable, don't install historical docs

* Mon Sep 07 2026 Cypress Reed <cypress@fyralabs.com>
- Port to Terra from COPR https://github.com/lihaohong6/COPR
