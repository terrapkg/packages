%global     debug_package %{nil}

%global long_name git-credential-manager

%global forgeurl https://github.com/GitCredentialManager/git-credential-manager

Name:           gcm-core
Version:        2.0.935
%forgemeta -i
Release:        1%{?dist}
Summary:        Secure, cross-platform Git credential storage

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

Provides:       %{long_name} = %{version}-%{release}
Provides:       %{long_name}-core = %{version}-%{release}

BuildRequires:  dotnet-sdk-6.0
# Require DPKG, so that we can use the `dpkg-architecture` command. which makes the build script happy.
# TODO: Better solution: Patch out the debian-specific packaging code.
BuildRequires:  dpkg-dev
Requires:       dotnet-runtime-6.0


%description
Secure, cross-platform Git credential storage with authentication to GitHub, Azure Repos, and other popular Git hosting services.

%prep
%forgesetup

%build
dotnet build -c LinuxRelease

%install
ls out/linux/Packaging.Linux/Release/payload -alh
install -Dm755 out/linux/Packaging.Linux/Release/payload/%{long_name} %{buildroot}%{_bindir}/%{long_name}


%files
%license LICENSE
/usr/bin/git-credential-manager


%changelog
* Tue Dec 06 2022 root - Packaging variables read or set by %%forgemeta
- new version

* Sat Oct 22 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- 
