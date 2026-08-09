%global _build_id_links none

# Exclude bundled/private Electron libraries.
%global __requires_exclude ^lib(EGL|GLESv2|ffmpeg|vk_swiftshader|vulkan)\.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\.so

%ifarch x86_64
%define archsuffix %{nil}
%elifarch aarch64
%define archsuffix -arm64
%endif

Name:           obsidian
Version:        1.13.4
Release:        1%?dist
Summary:        A markdown-based note-taking app

License:        Proprietary
URL:            https://obsidian.md
Source0:        https://github.com/obsidianmd/obsidian-releases/releases/download/v%{version}/obsidian-%{version}%{archsuffix}.tar.gz
Source1:        obsidian.desktop
Source2:        https://obsidian.md/license.html

Packager:       Utkarsh Verma <hi@utkarshverma.com>
BuildRequires:  desktop-file-utils
BuildRequires:  file

%electronmeta -D

%description
A powerful knowledge base that works on top of a local folder of plain text
Markdown files.

%prep
%autosetup -n %{name}-%{version}%{archsuffix}

%build
# Nothing to build.

%install
# Install the application payload.
install -dm0755 %{buildroot}%{_datadir}/%{name}
cp -a . %{buildroot}%{_datadir}/%{name}/

# Upstream's arm64 tarball currently ships a few x86_64 native Node addons
# (e.g. btime/get-fonts binding.node). Drop wrong-arch ELF files so RPM
# autodeps do not require x86_64-only GLIBC symbol versions on aarch64.
%ifarch aarch64
find %{buildroot}%{_datadir}/%{name} -type f \( -name '*.node' -o -name '*.so' \) \
    -exec sh -c 'file -b "$1" | grep -q x86-64 && rm -f "$1"' _ {} \;
%endif

# Add binaries to path.
install -dm0755 %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
ln -s %{_datadir}/%{name}/%{name}-cli %{buildroot}%{_bindir}/%{name}-cli

# Install the icon.
install -Dm644 resources/icon.png \
    %{buildroot}%{_hicolordir}/512x512/apps/%{name}.png

# Install the desktop file.
%desktop_file_install %{SOURCE1}

# Install the license.
cp %{SOURCE2} -t .

%check
%desktop_file_validate %{buildroot}%{_appsdir}/obsidian.desktop

%files
%license license.html
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_appsdir}/obsidian.desktop
%{_hicolordir}/512x512/apps/obsidian.png

%changelog
* Sat Aug 08 2026 Utkarsh Verma <hi@utkarshverma.com> - 1.13.4-1
- Initial package
