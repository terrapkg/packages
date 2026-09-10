%global     debug_package %{nil}
%define __os_install_post %{nil}

%global forgeurl https://github.com/KSP-CKAN/CKAN

Name:           CKAN
Version:        1.36.4

Release:        1%{?dist}
Summary:        The Comprehensive Kerbal Archive Network

%forgemeta

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  dotnet-sdk-10.0
BuildRequires:  xorg-x11-server-Xvfb
Requires:       dotnet-runtime-10.0


%description
The CKAN is a metadata repository and associated tools to allow you to find, install, and manage mods for Kerbal Space Program. It provides strong assurances that mods are installed in the way prescribed by their metadata files, for the correct version of Kerbal Space Program, alongside their dependencies, and without any conflicting mods.

%prep
%forgesetup

%build
xvfb-run ./build.sh test --configuration=Release --where="Category!=FlakyNetwork"

%install
export DONT_STRIP=1
install -Dm755 out/linux/Packaging.Linux/Release/payload/%name %buildroot%_bindir/%name


%files
%doc README.md
%license LICENSE
%_bindir/%name


%changelog
* Tue Aug 18 2026 madonuko <mado@fyralabs.com> - 1.36.4-1
- Initial package
