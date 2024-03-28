%global commit 4f5a96a359e0917ace6ae3778618a46d5e88c45a
%global commit_date 20240322
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}
%define __os_install_post %{nil}

Name:           chromebook-wireplumber-config
Version:        %commit_date.%shortcommit
Release:        1%?dist

License:        Apache-2.0
Summary:        Chromebook wireplumber configs
URL:            https://github.com/WeirdTreeThing/chromebook-linux-audio
Source0:        https://github.com/WeirdTreeThing/chromebook-linux-audio/archive/%commit/chromebook-linux-audio-%commit.tar.gz

Requires:       wireplumber

%description
WeirdTreeThing's wireplumber configs for chromebooks.

%prep
%autosetup -n chromebook-linux-audio-%commit

%install
mkdir -p %buildroot/etc/wireplumber/main.lua.d
cp conf/avs/51-avs-dmic.lua %buildroot/etc/wireplumber/main.lua.d/
cp conf/common/51-increase-headroom.lua %buildroot/etc/wireplumber/main.lua.d/

%files
%doc README.md
%license LICENSE
/etc/wireplumber/main.lua.d/*.lua

%changelog
* Thu Mar 28 2024 june-fish <terra@june.fish>
- Initial package.
