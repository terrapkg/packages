# The latest version of fcitx5-mozc requires newer
# version of protobuf than we have in Fedora 
# Bundling it for now
%bcond bundle_protobuf  1

# The bundled protobuf is not compatible with abseil-cpp 20250515
%bcond bundle_abslcpp   %{with bundle_protobuf}

# Enabling test also requires gtest, and we have to
# bundle it since the build system is not designed to
# use system gtest, disabling it for now to avoid
# bundlings. 
%bcond run_test         0

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

# as of 2025.1.1, build with gcc failed due to errors 
# with LOG(DFATAL), don't have time to investigate the 
# root cause. Switch to clang for now
%global toolchain clang

%global pkgname fcitx5-mozc
%global server_dir %{_libexecdir}/fcitx5-mozc


# main source 
%global version0  2.30.5618.102
%global forgeurl0 https://github.com/fcitx/mozc
%global commit0   c0ed34eaa1f39d2106554f4811969ebea04c1f0f
%global date0     20250124

%global ken_all_sha512 ed7b041a0d1d95b8be7c1824c3dfd50867080b6284265192ddc5f829c9d6bb0d537db56271764da3ddb8bba65ccf410050dfea276f579c853788e29e56bddaec
%global jigyosyo_sha512 cb47d51511d4021eb025db6575c593f399b70f027c5bf92eec2d1202029abd701b3476672b02da7f3ff3e18ba6824b277753fcc88c50d9015f14d1a8485513eb

# BSD-2-Clause license
# src/third_party/japanese_usage_dictionary
%global forgeurl1 https://github.com/hiroyuki-komatsu/japanese-usage-dictionary
%global commit1   e5b3425575734c323e1d947009dd74709437b684

%if %{with bundle_protobuf}
# BSD-3-Clause
# src/third_party/protobuf
%global forgeurl2 https://github.com/protocolbuffers/protobuf
%global tag2      v3.29.1
%endif

%if %{with run_test}
# src/third_party/gtest
%global forgeurl3 https://github.com/google/googletest
%global tag3      v1.15.2
%endif

%if %{with bundle_abslcpp}
%global forgeurl4 https://github.com/abseil/abseil-cpp
%global tag4      20240722.0
%endif

# Work around https://bugzilla.redhat.com/show_bug.cgi?id=2359090 by only
# handling the first source, by defining necessary macros for the additional
# sources manually, and by overriding the distprefix0 macro to avoid duplicate
# snapshot info in the Version and Release fields.
%global distprefix0 %{nil}
%forgemeta -z0
%global archivename1 japanese-usage-dictionary-%{commit1}
%global forgesource1 %{forgeurl1}/archive/%{commit1}/%{archivename1}.tar.gz
%global archivename2 protobuf-%(echo %{tag2} | sed -r 's/^v//')
%global forgesource2 %{forgeurl2}/archive/%{tag2}/%{archivename2}.tar.gz
%if %{with run_test}
%global archivename3 %(echo %{tag3} | sed -r 's/^v//').tar.gz
%global forgesource3 %{forgeurl3}/archive/%{tag3}/%{archivename3}.tar.gz
%endif
%global archivename4 abseil-cpp-%{tag4}
%global forgesource4 %{forgeurl4}/archive/%{tag4}/%{archivename4}.tar.gz

Name:           terra-fcitx5-mozc
# keep version consistent with mozc version 
# that fcitx5-mozc is based on
# upstream don't tag release, build git snapshot here
# git snapshot should have snapshot date will be taken care
# of by forgemeta after importing to dist-git
Version:        %{forgeversion}
Release:        1%{?dist}
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
Summary:        A wrapper of mozc for fcitx5
# src/data/unicode/ is UCD, but it is not copyrightable https://docs.fedoraproject.org/en-US/legal/license-field/#notcopyrightable
# src/data/dictionary* is NAIST-2003
License:        BSD-3-Clause AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain AND NAIST-2003 AND LGPL-2.0-or-later %{?with_bundle_abslcpp: AND Apache-2.0}
URL:            %{forgeurl}

# main source
Source0:        %{forgesource0} 
Source1:        %{forgesource1} 

%if %{with bundle_protobuf}
# protobuf
Source2:        %{forgesource2} 
%endif

%if %{with run_test}
# gtest
Source3:        %{forgesource3} 
%endif

%if %{with bundle_abslcpp}
# abseil-cpp
Source4:        %{forgesource4}
%endif

# Public Domain
# The original Japan Post URLs are no longer available.
Source5:        https://src.fedoraproject.org/repo/pkgs/rpms/%{pkgname}/ken_all.zip/sha512/%{ken_all_sha512}/ken_all.zip
Source6:        https://src.fedoraproject.org/repo/pkgs/rpms/%{pkgname}/jigyosyo.zip/sha512/%{jigyosyo_sha512}/jigyosyo.zip

# add -v to ninja command, to make verbose output during building
Patch0:         mozc-build-verbosely.patch
# only applied if the bundle_abslcpp bcond is false
Patch1:         0001-use-system-absl.patch

BuildRequires:  python3-devel
BuildRequires:  gettext 
BuildRequires:  gtk2-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  zinnia-devel
BuildRequires:  clang
BuildRequires:  ninja-build
BuildRequires:  gyp >= 0.1-0.4.840svn
BuildRequires:  fcitx5-devel
BuildRequires:  libappstream-glib
BuildRequires:  %{py3_dist six}
# BuildRequires:  gtest-devel
%if %{with bundle_abslcpp}
BuildRequires:  gmock-devel
%endif
BuildRequires:  jsoncpp-devel
BuildRequires:  binutils

Requires:       hicolor-icon-theme
Requires:       fcitx5
Requires:       fcitx5-data

Provides:       %{pkgname} = %{version}-%{release}
Provides:       %{pkgname}%{?_isa} = %{version}-%{release}
Conflicts:      %{pkgname}

%if %{with bundle_protobuf}
Provides:       bundled(protobuf) = %{tag2}
%else
BuildRequires:  protobuf-devel 
BuildRequires:  protobuf-c
%endif

%if %{with bundle_abslcpp}
Provides:       bundled(abseil-cpp) = %{tag4}
%else
BuildRequires:  abseil-cpp-devel
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1419949
# we are using mostly exact mozc server, same problem
# may occur here, adding ExcludeArch like ibus-mozc
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    ppc ppc64 sparcv9 sparc64 s390x %{ix86}

%description
A wrapper of mozc for fcitx5.

%prep
%setup -q -n %{archivename0} -a 5 -a 6
rm -rf src/third_party/*

%setup -q -n %{archivename0} -T -D -a 1
mv %{archivename1} src/third_party/japanese_usage_dictionary

%if %{with bundle_protobuf}
%setup -q -n %{archivename0} -T -D -a 2
mv %{archivename2} src/third_party/protobuf
rm src/third_party/protobuf/src/google/protobuf/lazy_repeated_field.cc
rm src/third_party/protobuf/src/google/protobuf/lazy_repeated_field_heavy.cc
%endif

%if %{with run_test}
%setup -q -n %{archivename0} -T -D -a 3
mv %{archivename3} src/third_party/gtest
%endif

%if %{with bundle_abslcpp}
%setup -q -n %{archivename0} -T -D -a 4
mv %{archivename4} src/third_party/abseil-cpp
%endif



%patch 0 -p1

%if %{without bundle_abslcpp}
%patch 1 -p1
%endif

(cd src/data/dictionary_oss;
PYTHONPATH="${PYTHONPATH}:../../" python3 ../../dictionary/gen_zip_code_seed.py \
    --zip_code=../../../KEN_ALL.CSV --jigyosyo=../../../JIGYOSYO.CSV >> dictionary09.txt;
)
# Don't build for fcitx4
rm src/unix/fcitx/fcitx.gyp
# preserve install time stamp
sed "s/ -m/ -pm/g" -i scripts/install_fcitx5 scripts/install_fcitx5_icons

%build
%set_build_flags
pushd src
# specify an another path for those mozc server files
# to enable this to co-exist with ibus-mozc
QTDIR=%{_prefix} \
GYP_DEFINES="document_dir=%{_datadir}/licenses/%{name} \
    qt_ver=6 \
    use_libzinnia=1 %{!?with_bundle_abslcpp:use_system_abseil_cpp=1} \
    %{?with_bundle_protobuf:use_libprotobuf=0} %{!?with_bundle_protobuf:use_libprotobuf=1} \
    zinnia_model_file=%{_datadir}/zinnia/model/tomoe/handwriting-ja.model" \
python3 build_mozc.py gyp --gypdir=%{_bindir} --server_dir=%{server_dir} --target_platform=Linux

# some race condition that the build system can fail due to genproto_commands_proto
# not finished before its dependents, so build it separately
python3 build_mozc.py build -c Release  protocol/protocol.gyp:genproto_commands_proto
python3 build_mozc.py build -c Release  server/server.gyp:mozc_server \
                                        gui/gui.gyp:mozc_tool \
                                        unix/fcitx5/fcitx5.gyp:fcitx5-mozc
popd

%install
pushd src
export _bldtype=Release
install -D -pm 755 "out_linux/${_bldtype}/mozc_server" "%{buildroot}%{server_dir}/mozc_server"
install -D -pm 755 "out_linux/${_bldtype}/mozc_tool"   "%{buildroot}%{server_dir}/mozc_tool"
sed "s|\${PREFIX}/share/metainfo|%{buildroot}%{_metainfodir}|g" -i  ../scripts/install_fcitx5 ../scripts/install_fcitx5_data
sed "s|\${PREFIX}/share|%{buildroot}%{_datadir}|g"              -i  ../scripts/install_fcitx5 ../scripts/install_fcitx5_icons ../scripts/install_fcitx5_data
sed "s|\${PREFIX}/lib|%{buildroot}%{_libdir}|g"                 -i  ../scripts/install_fcitx5
../scripts/install_fcitx5 
popd

%find_lang %{pkgname}

%if %{with run_test}
%check
pushd src
python3 build_mozc.py runtests -c Release
%endif

%files -f %{pkgname}.lang
%license LICENSE 
%doc README.md src/data/installer/*.html
%{server_dir}
%{_datadir}/fcitx5/*/mozc.conf
%{_datadir}/icons/hicolor/*/apps/*
%{_libdir}/fcitx5/fcitx5-mozc.so
%{_metainfodir}/org.fcitx.Fcitx5.Addon.Mozc.metainfo.xml

%changelog
* Tue Oct 20 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 2.30.5618.102^20250124gitc0ed34e-1
- Initial package with Qt 6 support
