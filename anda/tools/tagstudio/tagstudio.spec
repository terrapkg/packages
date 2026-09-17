Name:           tagstudio
Version:        9.6.3
Release:        4%{?dist}
Summary:        User-focused photo and file management system
License:        GPL-3.0-only
URL:            https://github.com/TagStudioDev/TagStudio
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-hatchling
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme

# TagStudio's media preview and playback support uses these external tools.
Requires:       ffmpeg
Requires:       hicolor-icon-theme
Recommends:     ripgrep

BuildArch:      noarch

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
TagStudio is a user-focused photo and file management system. It organizes
existing files with a flexible tag-based system without moving files or
requiring sidecar metadata files.

%prep
%autosetup -C

# Fedora 44 ships Python 3.14. The current upstream branch has raised this
# upper bound, while the v9.6.3 release metadata still stops at Python 3.13.
sed -i 's/>=3.12,<3.14/>=3.12,<3.15/' pyproject.toml

%pyproject_patch_dependency chardet:drop_constraints
%pyproject_patch_dependency pillow:drop_constraints
%pyproject_patch_dependency pillow-heif:drop_constraints
%pyproject_patch_dependency pyside6:drop_constraints
%pyproject_patch_dependency requests:drop_constraints
%pyproject_patch_dependency structlog:drop_constraints
%pyproject_patch_dependency opencv-python:drop_constraints
%pyproject_patch_dependency py7zr:drop_constraints

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tagstudio

install -Dm644 src/tagstudio/resources/tagstudio.desktop \
    %{buildroot}%{_datadir}/applications/tagstudio.desktop
install -Dm644 src/tagstudio/resources/icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/tagstudio.png

%check
%desktop_file_validate %{buildroot}%{_datadir}/applications/tagstudio.desktop

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/tagstudio
%{_datadir}/applications/tagstudio.desktop
%{_datadir}/icons/hicolor/512x512/apps/tagstudio.png

%changelog
* Wed Sep 16 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
