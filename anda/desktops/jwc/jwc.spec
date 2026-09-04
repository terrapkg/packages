%global commit cbea3595ab35518721de77ed456ded94bcd20777
%global commit_date 20260320
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           jwc
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        A file based wayland compositor
License:        GPL-3.0-or-later
URL:            https://git.sr.ht/~jsnr/jwc
Source0:        %{url}/archive/%{commit}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pkgconfig(wlroots)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(fuse3)

%description
jwc is a file based tiling Wayland compositor. jwc seeks to expose all
of its state through file operations, and allow acting on nodes,
windows and monitors through the plain text utils that you are accustomed to.

Want to move the focused window to workspace 3? echo 3 > $JWC_ROOT/nodes/focused/workspace

jwc is very much in beta, many more features and polish is to come.

%prep
%autosetup -n %{name}-%{commit}

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%{_bindir}/%{name}

%changelog
* Mon Jun 15 2026 Owen-sz <owen@fyralabs.com>
- initial commit
