%global _desc A music player for the desktop. Designed to be powerful and streamlined, putting the user in control of their music collection.

%undefine __brp_mangle_shebangs

Name:			python-tauon
Version:		9.1.2
Release:		1%?dist
Summary:		A music player for the desktop. Designed to be powerful and streamlined
License:		GPL-3.0-or-later
URL:			https://tauonmusicbox.rocks/
Source0:		https://github.com/Taiko2k/Tauon/archive/refs/tags/v%{version}.tar.gz
Patch0:		    remove-reqed-version.patch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  flac-devel
BuildRequires:  mpg123-devel
BuildRequires:  libvorbis-devel
BuildRequires:  opusfile-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libopenmpt-devel
BuildRequires:  wavpack-devel
BuildRequires:  game-music-emu-devel

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-tauon
Summary:        %{summary}
%{?python_provide:%python_provide python3-tauon}

%description -n python3-tauon
%_desc

%prep
%git_clone https://github.com/Taiko2k/Tauon v%{version}
%patch -P0 -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tauon
%find_lang tauon
install -Dm644 extra/tauonmb.desktop %{buildroot}%{_appsdir}/tauonmb.desktop
install -Dm644 extra/tauonmb-symbolic.svg %{buildroot}%{_scalableiconsdir}/tauonmb-symbolic.svg
install -Dm644 extra/tauonmb.svg %{buildroot}%{_scalableiconsdir}/tauonmb.svg
install -Dm755 extra/tauonmb.sh %{buildroot}/opt/tauon/tauonmb.sh

%files -n python3-tauon -f %{pyproject_files} -f tauon.lang
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/tauonmb
%{python3_sitearch}/phazor.cpython-314-*-linux-gnu.so
%{_appsdir}/tauonmb.desktop
%{_scalableiconsdir}/tauonmb-symbolic.svg
%{_scalableiconsdir}/tauonmb.svg
/opt/tauon/tauonmb.sh

%changelog
* Sat Mar 28 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
