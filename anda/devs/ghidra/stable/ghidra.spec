%global         debug_package   %{nil}
%global         yajsw_ver       13.18
%global         pydev_ver       9.3.0
%global         cdt_ver         8.6.0
%global         cdt_short_ver   %{expand:%(v=%{cdt_ver}; echo ${v%.*})}
%global         sarif_ver       2.1
%global         z3_ver          4.13.0
%global         z3_glibc        2.31

%global         ghidra_dir      ghidra-Ghidra_%{version}_build
%global         dep_dir         %{ghidra_dir}/dependencies
%global         flat_repo_dir   %{dep_dir}/flatRepo
%global         fid_dir         %{dep_dir}/fidb

%global         jre_ver         25

Name:           ghidra
Version:        12.1.2
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
Source7:        https://github.com/Z3Prover/z3/releases/download/z3-%{z3_ver}/z3-%{z3_ver}-x64-glibc-%{z3_glibc}.zip
Source8:        ghidra.desktop
Patch0:         0001-Enabling-support-for-Python-3.15.patch

Requires:       (java-%{jre_ver}-openjdk or temurin-%{jre_ver}-jdk)
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
%setup -q -c %{name}-%{version} -a 3 -a 7

pushd %{ghidra_dir}
%patch -P0 -p1
popd

mkdir -p %{dep_dir}/{GhidraDev,GhidraServer,Debugger-agent-dbgeng} %{flat_repo_dir} %{fid_dir}
mkdir -p %{dep_dir}/SymbolicSummaryZ3/os/linux_x86_64

cp "%{SOURCE1}" "%{flat_repo_dir}"
cp "%{SOURCE2}" "%{dep_dir}/GhidraServer"
cp "%{SOURCE3}" "%{dep_dir}/GhidraDev"
cp "%{SOURCE4}" "%{dep_dir}/GhidraDev"
cp "%{SOURCE5}" "%{flat_repo_dir}"
cp "%{SOURCE6}" "%{dep_dir}/Debugger-agent-dbgeng/dbgmodel.tlb"
cp z3-%{z3_ver}-x64-glibc-%{z3_glibc}/bin/*.jar "%{flat_repo_dir}"
cp z3-%{z3_ver}-x64-glibc-%{z3_glibc}/bin/libz3*.so "%{dep_dir}/SymbolicSummaryZ3/os/linux_x86_64"

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

ln -s %{_libdir}/%{name}/ghidraRun %{buildroot}/%{_bindir}/%{name}

ln -s %{_libdir}/%{name}/server/ghidraSvr %{buildroot}/%{_bindir}/%{name}-server
ln -s %{_libdir}/%{name}/server/svrAdmin %{buildroot}/%{_bindir}/%{name}-server-admin
ln -s %{_libdir}/%{name}/server/svrInstall %{buildroot}/%{_bindir}/%{name}-server-install
ln -s %{_libdir}/%{name}/server/svrUninstall %{buildroot}/%{_bindir}/%{name}-server-uninstall

for size in 16 24 32 48 64 128 256; do
    mkdir -p "%{buildroot}/%{_hicolordir}/${size}x${size}/apps"

    convert \
        "%{ghidra_dir}/Ghidra/RuntimeScripts/Windows/support/ghidra.ico" \
        -thumbnail 256x256 \
        -alpha on \
        -background none \
        -flatten \
        "%{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps/ghidra.png"
done

%desktop_file_install %{SOURCE8}

%files
%{_bindir}/%{name}
%{_libdir}/%{name}/
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
* Sun Jun 28 2026 Jan200101 <sentrycraft123@gmail.com>
- Initial package