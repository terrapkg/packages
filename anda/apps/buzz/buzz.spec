%global appid io.github.chidiwilliams.Buzz

Name:           buzz
Version:        1.3.3
Release:        1%?dist
Summary:        Buzz transcribes and translates audio offline on your personal computer
License:        MIT
URL:            https://chidiwilliams.github.io/buzz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3dist(polib)
BuildRequires:  python3dist(hatchling)
BuildRequires:  glslc
BuildRequires:  cmake gcc gcc-c++
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  desktop-file-utils

%description
Buzz transcribes and translates audio offline on your personal computer. Powered by OpenAI's Whisper.

%prep
%git_clone https://github.com/chidiwilliams/buzz
sed '/^requires-python/s@3\.13@3.15@' -i pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files buzz

desktop-file-install \
    --set-icon="%appid" \
    --set-key=Exec --set-value=%name \
    --dir=%buildroot%_appsdir \
    share/applications/%appid.desktop

%terra_appstream share/metainfo/%appid.metainfo.xml
install -Dpm644 share/icons/%appid.svg -t %buildroot%_scalableiconsdir

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%_appsdir/%appid.desktop
%_metainfodir/%appid.metainfo.xml
%_scalableiconsdir/%appid.svg

%changelog
* Thu Jan 01 2026 madonuko <mado@fyralabs.com> - 1.3.3-1
- Initial commit
