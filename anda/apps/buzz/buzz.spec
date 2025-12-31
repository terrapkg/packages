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

%description
Buzz transcribes and translates audio offline on your personal computer. Powered by OpenAI's Whisper.

%prep
%git_clone https://github.com/chidiwilliams/buzz

%build
%pyproject_wheel --ignore-requires-python

%install
%pyproject_install
%pyproject_save_files buzz

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_appsdir}/buzz.desktop

%changelog
* Thu Jan 01 2026 madonuko <mado@fyralabs.com> - 1.3.3-1
- Initial commit
