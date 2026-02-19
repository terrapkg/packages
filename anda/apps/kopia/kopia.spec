%global appid io.kopia.ui
%global appstream_component desktop-application

Name:           kopia
%electronmeta -D
Version:        0.22.3
Release:        1%{?dist}
Summary:        A backup/restore tool that allows you to create encrypted snapshots

License:        Apache-2.0 AND CC0-1.0 AND %{electron_license}
URL:            https://kopia.io/
Source0:        https://github.com/kopia/kopia/archive/v%{version}.tar.gz
Source1:        io.kopia.ui.desktop
Source2:        io.kopia.ui.metainfo.xml
Patch0:         fix-electron-output-dir.patch
ExclusiveArch:  %{golang_arches_future}
Packager:       metcya <metcya@gmail.com>

BuildRequires:  go-rpm-macros
BuildRequires:  terra-appstream-helper

%global gui_name %{name}-ui

%package -n %{gui_name}
Summary:        GUI for %{name}
Requires:       %{name} = %{evr}
ExclusiveArch:  %{electron_arches}

%description
Kopia is a fast and secure open-source backup/restore tool that allows you to
create encrypted snapshots of your data and save the snapshots to remote or
cloud storage of your choice, to network-attached storage or server, or locally
on your machine. Kopia does not 'image' your whole machine. Rather, Kopia
allows you to backup/restore any and all files/directories that you deem are
important or critical.

%description -n %{gui_name}
A graphical user interface for %{name}.

%prep
%autosetup -p1

%build
%global gomodulesmode GO111MODULE=on
%gobuild -o %{name} .

pushd app
%npm_build -B
popd

%install
install -Dm 755 %{name} -t %{buildroot}%{_bindir}

pushd app
%electron_install -b %{gui_name} -d %{gui_name} -s %{gui_name} -I ../icons
popd

# the offical package for kopia-ui includes a bundled copy of the kopia binary
# but we'll just symlink it
mkdir -p %{buildroot}%{_libdir}/%{gui_name}/resources/server
%{__ln_s} %{_bindir}/%{name} %{buildroot}%{_libdir}/%{gui_name}/resources/server/%{name}

%desktop_file_install %{S:1}

%terra_appstream -o %{S:2}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license README.md
%doc LICENSE
%{_bindir}/%{name}

%files -n %{gui_name}
%{_bindir}/%{gui_name}
%{_libdir}/%{gui_name}/
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/*/apps/kopia.png

%changelog
* Thu Jan 22 2026 metcya <metcya@gmail.com> - 0.22.3-1
- Initial package
