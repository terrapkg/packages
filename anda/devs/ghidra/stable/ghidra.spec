%global         debug_package   %{nil}
%global         yajsw_ver       13.18
%global         pydev_ver       9.3.0
%global         cdt_ver         8.6.0
%global         cdt_short_ver   %{expand:%(v=%{cdt_ver}; echo ${v%.*})}
%global         sarif_ver       2.1
# Ghidra pins Z3 4.13.0, whose Linux arm64 release mistakenly contains x86-64
# binaries (https://github.com/Z3Prover/z3/issues/7287). 4.13.2 fixes that,
# 4.13.3 is the first Linux arm64 release to include the Java bindings, and
# 4.13.4 fixes issues in those bindings. Ghidra only stays on 4.13.0 to keep
# building with RHEL 8's pre-C++20 compiler
# (https://github.com/NationalSecurityAgency/ghidra/issues/9464).
# TODO: Drop this override once Ghidra pins Z3 4.13.4 or later.
%global         z3_ver          4.13.4
%global         z3_x64          z3-%{z3_ver}-x64-glibc-2.35
%global         z3_arm64        z3-%{z3_ver}-arm64-glibc-2.34
%ifarch aarch64
%global         z3_source       9
%global         z3_dir          %{z3_arm64}
%global         ghidra_os       linux_arm_64
%else
%global         z3_source       7
%global         z3_dir          %{z3_x64}
%global         ghidra_os       linux_x86_64
%endif

%global         ghidra_dir      ghidra-Ghidra_%{version}_build
%global         dep_dir         %{ghidra_dir}/dependencies
%global         flat_repo_dir   %{dep_dir}/flatRepo
%global         fid_dir         %{dep_dir}/fidb

%global         jre_ver         25

# Do not generate Requires or Provides from the files in docs/, which
# ghidra-docs ships. They include x86-64 GhidraClass exercise programs, and the
# libraries those programs link against are not dependencies of the package.
%global         __requires_exclude_from ^%{_libdir}/ghidra/docs/
%global         __provides_exclude_from %{__requires_exclude_from}

Name:           ghidra
Version:        12.1.4
%global         short_version %{version}
Release:        1%{?dist}
Summary:        a software reverse engineering (SRE) framework
Packager:       Jan200101 <sentrycraft123@gmail.com>

License:        Apache 2.0
URL:            https://ghidra-sre.org/
Source0:        https://github.com/NationalSecurityAgency/ghidra/archive/Ghidra_%{version}_build.tar.gz
Source1:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/android4me/AXMLPrinter2.jar
Source2:        https://sourceforge.net/projects/yajsw/files/yajsw/yajsw-stable-%{yajsw_ver}/yajsw-stable-%{yajsw_ver}.zip
Source3:        https://sourceforge.net/projects/pydev/files/pydev/PyDev%20%{pydev_ver}/PyDev%20%{pydev_ver}.zip#/PyDev-%{pydev_ver}.zip
Source4:        https://archive.eclipse.org/tools/cdt/releases/%{cdt_short_ver}/cdt-%{cdt_ver}.zip
Source5:        https://github.com/NationalSecurityAgency/ghidra-data/raw/Ghidra_%{version}/lib/java-sarif-%{sarif_ver}-modified.jar
Source6:        https://github.com/NationalSecurityAgency/ghidra-data/raw/Ghidra_%{version}/Debugger/dbgmodel.tlb#/dbgmodel_%{version}.tlb
Source7:        https://github.com/Z3Prover/z3/releases/download/z3-%{z3_ver}/%{z3_x64}.zip
Source8:        ghidra.desktop
Source9:        https://github.com/Z3Prover/z3/releases/download/z3-%{z3_ver}/%{z3_arm64}.zip
Patch0:         0001-Enabling-support-for-Python-3.15.patch

Requires:       (java-%{jre_ver}-openjdk-devel or temurin-%{jre_ver}-jdk)
BuildRequires:  java-%{jre_ver}-openjdk-devel
BuildRequires:  java-%{jre_ver}-openjdk-headless
BuildRequires:  gradle
BuildRequires:  gcc gcc-c++
BuildRequires:  bison flex
BuildRequires:  desktop-file-utils
BuildRequires:  python3-pip
BuildRequires:  python3-devel
BuildRequires:  python-wheel0.37-wheel
BuildRequires:  python-setuptools-wheel
BuildRequires:  ImageMagick

ExclusiveArch:  x86_64

%description
Ghidra is a software reverse engineering (SRE) framework developed
by NSA's Research Directorate for NSA's cybersecurity mission. It
helps analyze malicious code and malware like viruses, and can give
cybersecurity professionals a better understanding of potential
vulnerabilities in their networks and systems.

%package server
Summary:        Ghidra Server
Requires:       %{name}%{?_isa} = %{version}

%description server
Ghidra Server

%package docs
Summary:        Ghidra Documentation
Requires:       %{name}%{?_isa} = %{version}

%description docs
Ghidra Documentation

%prep
%setup -q -c %{name}-%{version} -a 3 -a %{z3_source}

pushd %{ghidra_dir}
%patch -P0 -p1
popd

mkdir -p %{dep_dir}/{GhidraDev,GhidraServer,Debugger-agent-dbgeng} %{flat_repo_dir} %{fid_dir}
mkdir -p %{dep_dir}/SymbolicSummaryZ3/os/%{ghidra_os}

cp "%{SOURCE1}" "%{flat_repo_dir}"
cp "%{SOURCE2}" "%{dep_dir}/GhidraServer"
cp "%{SOURCE3}" "%{dep_dir}/GhidraDev"
cp "%{SOURCE4}" "%{dep_dir}/GhidraDev"
cp "%{SOURCE5}" "%{flat_repo_dir}"
cp "%{SOURCE6}" "%{dep_dir}/Debugger-agent-dbgeng/dbgmodel.tlb"
cp %{z3_dir}/bin/*.jar "%{flat_repo_dir}"
cp %{z3_dir}/bin/libz3*.so "%{dep_dir}/SymbolicSummaryZ3/os/%{ghidra_os}"

mkdir -p "%{dep_dir}/Debugger-rmi-trace"
cp %{python_wheel_dir}/setuptools-*-py3-none-any.whl "%{dep_dir}/Debugger-rmi-trace"
cp %{python_wheel_dir}/wheel-*-none-any.whl "%{dep_dir}/Debugger-rmi-trace"

%build
cd %{ghidra_dir}
gradle --no-daemon --parallel \
    buildGhidra \
    -x buildPyPackage

%install
mkdir -p %{buildroot}/%{_libdir}/%{name}/ %{buildroot}/%{_bindir}/

unzip %{ghidra_dir}/build/dist/ghidra_%{short_version}_DEV_%{lua: print(os.date("%Y%m%d"))}_linux*.zip
cp -r ghidra_%{short_version}_DEV/* %{buildroot}/%{_libdir}/%{name}

# Ghidra 12.1 installs the Linux-amd64, Windows and macOS builds of
# 7-Zip-JBinding on every architecture. Remove the builds that cannot load on
# the target architecture; there is no aarch64 build.
# TODO: Drop this when updating to Ghidra 12.2, which removes sevenzipjbinding (GP-7095).
pushd %{buildroot}/%{_libdir}/%{name}/Ghidra/Features/FileFormats/data/sevenzipnativelibs
rm -r Windows-amd64 Mac-x86_64
%ifnarch x86_64
rm -r Linux-amd64
%endif
popd

ln -s %{_libdir}/%{name}/ghidraRun %{buildroot}/%{_bindir}/%{name}

ln -s %{_libdir}/%{name}/server/ghidraSvr %{buildroot}/%{_bindir}/%{name}-server
ln -s %{_libdir}/%{name}/server/svrAdmin %{buildroot}/%{_bindir}/%{name}-server-admin
ln -s %{_libdir}/%{name}/server/svrInstall %{buildroot}/%{_bindir}/%{name}-server-install
ln -s %{_libdir}/%{name}/server/svrUninstall %{buildroot}/%{_bindir}/%{name}-server-uninstall

for size in 16 24 32 48 64 128 256; do
    mkdir -p "%{buildroot}/%{_hicolordir}/${size}x${size}/apps"

    magick \
        "%{ghidra_dir}/Ghidra/RuntimeScripts/Windows/support/ghidra.ico" \
        -thumbnail ${size}x${size} \
        -alpha on \
        -background none \
        -flatten \
        "%{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps/ghidra.png"
done

%desktop_file_install %{SOURCE8}

%files
%{_bindir}/%{name}
%{_libdir}/%{name}/
%exclude %{_libdir}/%{name}/docs/
%exclude %{_libdir}/%{name}/server/
%{_appsdir}/ghidra.desktop
%{_hicolordir}/*/apps/ghidra.png

%license %{ghidra_dir}/LICENSE

%files server
%{_bindir}/%{name}-server
%{_bindir}/%{name}-server-admin
%{_bindir}/%{name}-server-install
%{_bindir}/%{name}-server-uninstall
%{_libdir}/%{name}/server/

%files docs
%{_libdir}/%{name}/docs/

%changelog
* Sat Aug 22 2026 Jan200101 <sentrycraft123@gmail.com> - 12.1.3-2
- fix application icons

* Sun Jun 28 2026 Jan200101 <sentrycraft123@gmail.com>
- Initial package