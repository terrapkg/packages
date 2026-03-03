%global forgeurl https://github.com/skeeto/u-config
Version:        0.34.0
%forgemeta

Name:           u-config
Release:        1%{?dist}
Summary:        A smaller, simpler, portable pkg-config clone 

License:        Unlicense
URL:            %{forgeurl}
Source0:        %{forgesource}

Packager:       metcya <metcya@gmail.com>

BuildRequires:  gcc

%description
u-config ("micro-config") is a small, highly portable pkg-config and pkgconf
clone. It was written primarily for w64devkit and Windows, but can also serve
as a reliable drop-in replacement on other platforms. Notable features:

%prep
%forgeautosetup

%build
%__cc $CFLAGS \
      $CPPFLAGS \
      -DPKG_CONFIG_LIBDIR="\"%{_libdir}/pkgconfig\"" \
      $LDFLAGS \
      -o u-config \
      main_posix.c

%install
install -Dm 755 u-config %{buildroot}%{_bindir}/u-config
install -Dm 655 u-config.1 %{buildroot}%{_mandir}/man1/u-config.1

%files
%license UNLICENSE
%doc README.md
%{_bindir}/u-config
%{_mandir}/man1/u-config.1.*

%changelog
* Tue Mar 03 2026 metcya <metcya@gmail.com>
- Initial package
