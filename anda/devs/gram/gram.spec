%bcond clang 1

%if %{with clang}
%global toolchain clang
%endif

%undefine __brp_mangle_shebangs
%global appid app.liten.Gram

Name:          gram
Version:       3.3.0
Release:       1%{?dist}
Summary:       The Gram Code Editor
SourceLicense: Apache-2.0 AND CC-BY-SA-4.0 AND MIT AND OFL
License:       FIXME
URL:           https://gram-editor.com
Source0:       https://codeberg.org/GramEditor/gram/archive/%{version}.tar.gz
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros
BuildRequires: cmake
BuildRequires: desktop-file-utils
%if %{with clang}
BuildRequires: clang
%else
BuildRequires: gcc
BuildRequires: gcc-c++
%endif
BuildRequires: gettext-envsubst
BuildRequires: libappstream-glib
BuildRequires: libxkbcommon-x11-devel
BuildRequires: mold
BuildRequires: openssl-devel
Packager:      Gilver E. <roachy@fyralabs.com>

%description
A hard fork of Zed that removes LLM integration, tries to fix issues, and tries to improve upon the original.

For more information, see Gram's mission statement: https://codeberg.org/GramEditor/gram/src/branch/main/docs/mission.md

%package       doc
Summary:       Documentation for the Gram editor

%description   doc
Documentation files for the Gram editor for users and contributors.

%prep
%autosetup -n %{name} -p1
%cargo_prep_online

export DO_STARTUP_NOTIFY="true"
export APP_ID="%{appid}"
export APP_ICON="%{appid}"
export APP_NAME="Gram"
export APP_CLI="gram"
export APP="%{_libexecdir}/gram-editor"
export APP_ARGS="%U"
export GRAM_UPDATE_EXPLANATION="Run dnf up to update Gram from Terra."
export GRAM_RELEASE_CHANNEL="stable"
export BRANDING_LIGHT="#e9aa6a"
export BRANDING_DARK="#1a5fb4"

envsubst < "crates/gram/resources/gram.desktop.in" > %{appid}.desktop
sed -i "s|@release_info@||g" "crates/gram/resources/flatpak/gram.metainfo.xml.in"

envsubst < "crates/gram/resources/flatpak/gram.metainfo.xml.in" > %{appid}.metainfo.xml

%build
export GRAM_UPDATE_EXPLANATION="Run dnf up to update Gram from Terra."
echo "stable" > crates/gram/RELEASE_CHANNEL

%cargo_build -- --package gram --package cli
ALLOW_MISSING_LICENSES=1 script/generate-licenses

%install
install -Dm755 target/rpm/gram %{buildroot}%{_libexecdir}/gram-editor
install -Dm755 target/rpm/cli %{buildroot}%{_bindir}/gram

%{__cargo} clean

%desktop_file_install %{appid}.desktop
install -Dm644 crates/gram/resources/%{appid}.svg -t %{buildroot}%{_scalableiconsdir}
install -Dm644 %{appid}.metainfo.xml -t %{buildroot}%{_metainfodir}

# Funny Zed license solution
%{__cargo} tree                                                             \
    -Z avoid-dev-deps                                                       \
    --workspace                                                             \
    --edges no-build,no-dev,no-proc-macro                                   \
    --target all                                                            \
    %{__cargo_parse_opts %{-n} %{-a} %{-f:-f%{-f*}}}                        \
    --prefix none                                                           \
    --format "{l}: {p}"                                                     \
    | sed -e "s: ($(pwd)[^)]*)::g" -e "s: / :/:g" -e "/\/.*:/{s/\// OR /}"  \
    | sed -e '/.*(\*).*/d' -e '/^: pet/ s/./MIT&/'                          \
    | sort -u                                                               \
> LICENSE.dependencies

# All of these are currently commented because they affect the NEXT release of Gram, afterwards they have to be added. For now the commands below it are correct.

#cp assets/icons/LICENSE LICENSE.icons

# We love actual proper attribution, but holy hell is it a lot of licenses.
#for folder in assets/fonts/*; do
#  font=$(basename $folder)
#  cp $folder/LICENSE ./LICENSE.$font
#done

#for folder in assets/themes/*; do
#  theme=$(basename $folder)
#  cp $folder/LICENSE ./LICENSE.$theme
#done

# Remove next release.
cp assets/icons/LICENSES ./LICENSE.icons
cp assets/themes/LICENSES ./LICENSE.themes
cp assets/fonts/fira-sans/OFL.txt ./LICENSE.fira-sans
cp assets/fonts/myna/LICENSE ./LICENSE.myna

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license LICENSE*
%doc README.md
%doc CODE_OF_CONDUCT.md
%doc SECURITY.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}-editor

%files doc
%doc docs/*

%changelog
* Sun Sep 27 2026 Gilver E. <roachy@fyralabs.com> - 3.3.0-1
- Initial package
