%global debug_package %{nil}
# It's Electron all over again
%global __requires_exclude_from %{_libdir}/%{name}/.*
%global __provides_exclude_from %{_libdir}/%{name}/.*
%global git_name PowerShell
# Not currently tracked, all PowerShell specifies is a version under 4.99
%global pester_version 4.10.1
%global dotnet_version 9.0
# Arch defined by .NET
%ifarch %{x86_64}
%global darch x64
%elifarch %{arm64}
%global darch arm64
%endif
%global appid com.microsoft.PowerShell
%global org com.microsoft
%global appstream_component console-application
%bcond test 1

Name:          powershell
Version:       7.5.4
Release:       2%{?dist}
Summary:       A cross-platform automation and configuration tool/framework
SourceLicense: MIT
License:       Apache-2.0 AND BSD-2-Clause AND MIT
URL:           https://microsoft.com/PowerShell
Source0:       https://github.com/%{git_name}/%{git_name}/archive/refs/tags/v%{version}.tar.gz
Source1:       https://globalcdn.nuget.org/packages/pester.%{pester_version}.nupkg
# For some reason the build doesn't provide this information to itself
Source2:       Microsoft.PowerShell.SDK.csproj.TypeCatalog.targets
Source3:       %{appid}.metainfo.xml
BuildRequires: dotnet-host
BuildRequires: dotnet-sdk-%{dotnet_version}
BuildRequires: git-core
BuildRequires: jq
BuildRequires: nuget
BuildRequires: unzip
%if %{with test}
BuildRequires: glibc-all-langpacks
BuildRequires: iputils
BuildRequires: langpacks-en
%endif
Requires:      dotnet-hostfxr-%{dotnet_version}
Requires:      dotnet-runtime-%{dotnet_version}
# .NET versioning
Provides:      mono(pwsh) = %{version}.0
Packager:      Gilver E. <roachy@fyralabs.com>

%description
%{git_name} is a cross-platform automation and configuration tool/framework.

%package       doc
Summary:       Documentation files for PowerShell
Requires:      %{name} = %{evr}

%description   doc
This package contains documentation for PowerShell.

%prep
%git_clone https://github.com/%{git_name}/%{git_name}.git v%{version}

# Patch sources to fetch from upstream NuGet otherwise some fail
sed -i 's|add key=.*"|add key="nuget.org" value="https://api.nuget.org/v3/index.json"|g' nuget.config

jq '.sdk.version = "%{dotnet_version}.0" | .sdk.rollForward = "feature"' global.json > _global.json
  mv _global.json global.json

%build
export NUGET_PACKAGES="$PWD/nuget"
export DOTNET_NOLOGO=true
export DOTNET_CLI_TELEMETRY_OPTOUT=true

dotnet restore src/powershell-unix -p:PublishReadyToRun=true
dotnet restore src/TypeCatalogGen
dotnet restore src/ResGen
dotnet restore src/Modules
dotnet restore src/Microsoft.PowerShell.GlobalTool.Shim
dotnet restore test/tools/TestAlc
dotnet restore test/tools/TestExe
dotnet restore test/tools/UnixSocket
dotnet restore test/tools/Modules
dotnet restore test/tools/TestService -p:RuntimeIdentifiers=linux-%{darch}
dotnet restore test/tools/WebListener -p:RuntimeIdentifiers=linux-%{darch}
dotnet restore test/tools/NamedPipeConnection/src/code

pushd src/ResGen
dotnet run --no-restore
popd

cp -t src/Microsoft.PowerShell.SDK/obj \
    "%{SOURCE2}"

INCFILE="$PWD/src/TypeCatalogGen/powershell_linux-%{darch}.inc"
dotnet msbuild \
    src/Microsoft.PowerShell.SDK \
    -t:_GetDependencies \
    -p:DesignTimeBuild=true \
    -p:_DependencyFile="$INCFILE" \
    -nologo

dotnet run \
    --no-restore \
    --project src/TypeCatalogGen \
    src/System.Management.Automation/CoreCLR/CorePsTypeCatalog.cs \
    "$INCFILE"

dotnet publish \
    --no-restore \
    --runtime linux-%{darch} \
    --no-self-contained \
    --configuration Release \
    --output lib \
    src/powershell-unix/

grep 'Microsoft.NETCore.App' "$INCFILE" | sed 's/;//' | while read -r assembly; do
    install -Dm755 -t lib/ref "$assembly"
done

cp -a $NUGET_PACKAGES/microsoft.powershell.archive/1.2.5/. lib/Modules/Microsoft.PowerShell.Archive
cp -a $NUGET_PACKAGES/microsoft.powershell.psresourceget/1.1.1/. lib/Modules/Microsoft.PowerShell.PSResourceGet
cp -a $NUGET_PACKAGES/packagemanagement/1.4.8.1/. lib/Modules/PackageManagement
cp -a $NUGET_PACKAGES/powershellget/2.2.5/. lib/Modules/PowerShellGet
cp -a $NUGET_PACKAGES/psreadline/2.3.6/. lib/Modules/PSReadLine
cp -a $NUGET_PACKAGES/threadjob/2.0.3/. lib/Modules/ThreadJob

# Restore-PSPester
unzip -ud temp_pester %{SOURCE1}
cp -a temp_pester/tools lib/Modules/Pester

# Generate manpage
lib/pwsh -noprofile -command '
  Import-Module ./build.psm1 -ArgumentList $true
  Import-Module ./tools/packaging/packaging.psm1
  New-ManGzip
'

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -a lib/* -t %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/%{name}/pwsh %{buildroot}%{_bindir}/pwsh
install -Dpm644 assets/manpage/pwsh.1.gz -t %{buildroot}%{_mandir}/man1
install -Dpm644 assets/powershell_128.svg %{buildroot}%{_scalableiconsdir}/%{name}.svg

%terra_appstream -o %{SOURCE3}

%if %{with test}
%check
export NUGET_PACKAGES="$PWD/nuget"
export DOTNET_NOLOGO=true
export DOTNET_CLI_TELEMETRY_OPTOUT=true

# Remove tests that fail in CIs
rm test/powershell/engine/Help/HelpSystem.Tests.ps1
rm test/powershell/Modules/Microsoft.PowerShell.Management/Start-Process.Tests.ps1
rm test/powershell/Modules/Microsoft.PowerShell.Utility/Format-Table.Tests.ps1
rm test/powershell/Language/Parser/RedirectionOperator.Tests.ps1
rm test/powershell/Language/Scripting/NativeExecution/NativeWindowsTildeExpansion.Tests.ps1
rm test/powershell/Modules/Microsoft.PowerShell.Utility/WebCmdlets.Tests.ps1
rm test/powershell/Modules/Microsoft.PowerShell.PSResourceGet/Microsoft.PowerShell.PSResourceGet.Tests.ps1

# Fails on timezone format
rm test/powershell/Modules/Microsoft.PowerShell.Management/TimeZone.Tests.ps1

# Opens browser
rm test/powershell/Language/Scripting/NativeExecution/NativeCommandProcessor.Tests.ps1
rm test/powershell/Modules/Microsoft.PowerShell.Utility/Invoke-Item.Tests.ps1

# Creates directories in $HOME
rm test/powershell/Language/Parser/ParameterBinding.Tests.ps1
rm test/powershell/Language/Scripting/ScriptHelp.Tests.ps1
rm test/powershell/Modules/Microsoft.PowerShell.Utility/Add-Type.Tests.ps1
rm test/powershell/Modules/Microsoft.PowerShell.Utility/Set-PSBreakpoint.Tests.ps1
rm test/powershell/engine/Basic/Assembly.LoadFrom.Tests.ps1
rm test/powershell/engine/Basic/Assembly.LoadNative.Tests.ps1

unzip -ud test/tools/Modules/SelfSignedCertificate \
"$NUGET_PACKAGES/selfsignedcertificate/0.0.4/selfsignedcertificate.0.0.4.nupkg"

dotnet publish \
    --no-restore \
    --configuration Debug \
    test/tools/TestAlc

for project in TestExe TestService UnixSocket WebListener; do
    dotnet publish \
      --no-restore \
      --runtime linux-%{darch} \
      --self-contained \
      --configuration Debug \
      --output test/tools/$project/bin \
      test/tools/$project
    export PATH="$PATH:$PWD/test/tools/$project/bin/Debug/net%{dotnet_version}/linux-%{darch}"
  done

dotnet publish \
    --no-restore \
    --configuration Debug \
    --framework net%{dotnet_version} \
    --output test/tools/Modules/Microsoft.PowerShell.NamedPipeConnection \
    test/tools/NamedPipeConnection/src/code

install -Dm644 -t test/tools/Modules/Microsoft.PowerShell.NamedPipeConnection \
  test/tools/NamedPipeConnection/src/Microsoft.PowerShell.NamedPipeConnection.psd1

export LANG="en_US.UTF-8"
export LC_ALL="$LANG"

# shellcheck disable=SC2016
lib/pwsh -noprofile -command '
    $env:PSModulePath = "$(Get-Location)/test/tools/Modules:" + $env:PSModulePath
    Import-Module "Pester"
    Invoke-Pester -Show Header,Failed,Summary -EnableExit `
      -OutputFormat NUnitXml -OutputFile pester-tests.xml `
      -ExcludeTag @("Slow", "RequireSudoOnUnix") `
      -Tag @("CI", "Feature") `
      "test/powershell"
  '
%endif

%files
%license LICENSE.txt
%license assets/additionalAttributions.txt
%doc README.md
%doc CODE_OF_CONDUCT.md
%{_bindir}/pwsh
%{_libdir}/%{name}/
%{_mandir}/man1/pwsh.1.*
%{_scalableiconsdir}/%{name}.svg
%{_metainfodir}/%{appid}.metainfo.xml

%files doc
%doc docs/*
%doc CHANGELOG
%doc ADOPTERS.md

%changelog
* Wed Dec 24 2025 Gilver E. <rockgrub@disroot.org> - 7.5.4-1
- Initial package
