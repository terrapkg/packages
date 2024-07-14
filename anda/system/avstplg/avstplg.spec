%global commit e1176e63ccbee51ab59fdb8afaed2bf5af8427d1
%global commit_date 20240711
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%define __os_install_post %{nil}

Name:           avstplg 
Version:        %commit_date.%shortcommit
Release:        1%?dist

License:        Apache-2.0
Summary:        Set of tools designed to help develop and debug software and firmware on Intel platforms with AudioDSP onboard.
URL:            https://github.com/thesofproject/avsdk
Source0:        https://github.com/thesofproject/avsdk/archive/%commit/avsdk-%commit.tar.gz

Requires:       dotnet-runtime-8.0
BuildRequires:  dotnet-sdk-8.0 make

%description
Set of tools designed to help develop and debug software and firmware on Intel platforms with AudioDSP onboard.

Related to alsa-utils which is also set of utilities but targets AdvancedLinuxSoundArchitecture (ALSA) audience in more general fashion.

%prep
%autosetup -n avsdk-%commit
cd avstplg
sed -i 's/Debug/Release/' Makefile

%build
cd avstplg
%make_build

%install
install -Dm755 avstplg/build/bin/Release/net6.0/publish/avstplg %{buildroot}/%{_bindir}/avstplg
install -Dm755 avstplg/build/bin/Release/net6.0/avstplg.dll %{buildroot}/%{_libdir}/avstplg.dll

%files
%doc README.md
%license LICENSE
%_bindir/avstplg
%_libdir/avstplg.dll

%changelog
* Tue Jan 2 2024 infinitebash <terra@infinitebash.com>
- Initial package.
