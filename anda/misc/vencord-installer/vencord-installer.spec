
%global debug_package %{nil}

%bcond_without openasar

%global appstream_component addon
# https://github.com/vencord/installer
%global goipath         github.com/Vencord/Installer
Version:                1.4.0
%global commit          8bd9dfd8de2926bb55cf7709b8c31f0704372cec

%global appid           dev.vencord.Installer

%gometa -L -f

%global common_description %{expand:
A cross platform gui/cli app for installing Vencord.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           vencord-installer
Release:        1%{?dist}
Provides:       golang-github-vencord-installer = %{version}-%{release}
Summary:        A cross platform gui/cli app for installing Vencord
Packager:       Cappy Ishihara <cappy@fyralabs.com>
License:        GPL-3.0-only
URL:            %{gourl}
Source:         %{gosource}
Source1:        %appid.metainfo.xml
BuildRequires:  go-rpm-macros
BuildRequires:  go-srpm-macros
BuildRequires:  anda-srpm-macros
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  libGL-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  wayland-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  extra-cmake-modules

%description %{common_description}

%package cli
Summary:        CLI version of %{name}
%description cli %{common_description} (CLI version)


%package discord-stable
Summary:        Automatic Discord integration for %{name} (stable)
Requires:       %{name}-cli
Requires(posttrans): %{name}-cli
%description discord-stable
discord-stable Automatic Discord integration for %{name} (stable branch).

%package discord-canary
Summary:        Automatic Discord integration for %{name} (canary)
Requires:       %{name}-cli
Requires(posttrans): %{name}-cli
%description discord-canary
discord-canary Automatic Discord integration for %{name} (canary branch).

%package discord-ptb
Summary:        Automatic Discord integration for %{name} (ptb)
Requires:       %{name}-cli
Requires(posttrans): %{name}-cli
%description discord-ptb
Automatic Discord integration for %{name} (ptb branch).

%if %{with openasar}
%package discord-stable+openasar
Summary:        Automatic Discord integration for %{name} (stable, OpenAsar)
Requires:       %{name}-cli
Requires(posttrans): %{name}-cli
Conflicts:      %{name}-discord-stable
Conflicts:      discord-openasar
%description discord-stable+openasar
discord-stable+openasar Automatic Discord integration for %{name} (stable branch, OpenAsar).

%package discord-canary+openasar
Summary:        Automatic Discord integration for %{name} (canary, OpenAsar)
Requires:       %{name}-cli
Requires(posttrans): %{name}-cli
Conflicts:      %{name}-discord-canary
Conflicts:      discord-canary-openasar
%description discord-canary+openasar
discord-canary+openasar Automatic Discord integration for %{name} (canary branch, OpenAsar).

%package discord-ptb+openasar
Summary:        Automatic Discord integration for %{name} (ptb, OpenAsar)
Requires:       %{name}-cli
Requires(posttrans): %{name}-cli
Conflicts:      %{name}-discord-ptb
Conflicts:      discord-ptb-openasar
%description discord-ptb+openasar
Automatic Discord integration for %{name} (ptb branch, OpenAsar).
%endif

%gopkg

%prep
%goprep_online -A


%build
%define gomodulesmode GO111MODULE=on
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
%gobuild -o %{gobuilddir}/bin/vencord-installer
%gobuild -o %{gobuilddir}/bin/vencord-installer-cli -tags cli


%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%terra_appstream -o %{SOURCE1}

%files
%license LICENSE
%doc README.md
%{_bindir}/vencord-installer
%{_datadir}/metainfo/%appid.metainfo.xml

%files cli
%license LICENSE
%doc README.md
%{_bindir}/vencord-installer-cli

%files discord-stable
%license LICENSE
%doc README.md

%files discord-canary
%license LICENSE
%doc README.md

%files discord-ptb
%license LICENSE
%doc README.md

%if %{with openasar}
%files discord-stable+openasar
%license LICENSE
%doc README.md

%files discord-canary+openasar
%license LICENSE
%doc README.md

%files discord-ptb+openasar
%license LICENSE
%doc README.md
%endif

%gopkgfiles


%transfiletriggerin -n %{name}-discord-stable -- /usr/share/discord
%{_bindir}/vencord-installer-cli -install -location /usr/share/discord

%transfiletriggerin -n %{name}-discord-canary -- /usr/share/discord-canary
%{_bindir}/vencord-installer-cli -install -location /usr/share/discord-canary

%transfiletriggerin -n %{name}-discord-ptb -- /usr/share/discord-ptb
%{_bindir}/vencord-installer-cli -install -location /usr/share/discord-ptb

%if %{with openasar}
%transfiletriggerin -n %{name}-discord-stable+openasar -- /usr/share/discord
%{_bindir}/vencord-installer-cli -install -install-openasar -location /usr/share/discord

%transfiletriggerin -n %{name}-discord-canary+openasar -- /usr/share/discord-canary
%{_bindir}/vencord-installer-cli -install -install-openasar -location /usr/share/discord-canary

%transfiletriggerin -n %{name}-discord-ptb+openasar -- /usr/share/discord-ptb
%{_bindir}/vencord-installer-cli -install -install-openasar -location /usr/share/discord-ptb
%endif

%changelog
%autochangelog
