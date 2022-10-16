Name:           camel-1.2
Version:        3.44.4
Release:        %autorelease
Summary:        A generic Messaging Library
License:        LGPLv2+
Source0:        https://github.com/GNOME/evolution-data-server/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake gcc

%description
Camel is a generic messaging library. It supports the standard 
messaging system for receiving and sending messages. It is the 
messaging backend for Evolution.


%prep
%setup -q
# extracted right?
mv src/camel camel
rm -rf src
mv camel/* .


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%doc src/camel/README
%license COPYING


%changelog
* Sun Oct 16 2022 windowsboy111 <windowsboy111@fyralabs.com> - 3.44.4
- Initial package.
