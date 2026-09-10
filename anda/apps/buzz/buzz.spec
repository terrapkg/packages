%global appid io.github.chidiwilliams.Buzz

Name:           buzz
Version:        1.4.4
Release:        1%{?dist}
Summary:        Buzz transcribes and translates audio offline on your personal computer
License:        MIT
URL:            https://chidiwilliams.github.io/buzz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pybind11
BuildRequires:  python3dist(polib)
BuildRequires:  python3dist(hatchling)
BuildRequires:  glslc
BuildRequires:  cmake gcc gcc-c++
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  desktop-file-utils

ExclusiveArch:  x86_64

%description
Buzz transcribes and translates audio offline on your personal computer. Powered by OpenAI's Whisper.

%prep
%git_clone https://github.com/chidiwilliams/buzz
sed '/^requires-python/s@3\.13@3.15@' -i pyproject.toml

%pyproject_patch_dependency cmake:drop_constraints
%pyproject_patch_dependency flake8:drop_constraints
%pyproject_patch_dependency hydra-colorlog:drop_constraints
%pyproject_patch_dependency numpy:drop_constraints
%pyproject_patch_dependency posthog:drop_constraints
%pyproject_patch_dependency submitit:drop_constraints
%pyproject_patch_dependency torch:drop_constraints
%pyproject_patch_dependency torchaudio:drop_constraints
%pyproject_patch_dependency transformers:drop_constraints
%pyproject_patch_dependency certifi:drop_constraints
%pyproject_patch_dependency coverage:drop_constraints
%pyproject_patch_dependency nltk:drop_constraints
%pyproject_patch_dependency onnx:drop_constraints
%pyproject_patch_dependency onnxruntime:drop_constraints

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files demucs
%pyproject_save_files buzz

desktop-file-install \
    --set-icon="%appid" \
    --set-key=Exec --set-value=%name \
    --dir=%buildroot%_appsdir \
    share/applications/%appid.desktop

%terra_appstream share/metainfo/%{appid}.metainfo.xml
install -Dpm644 share/icons/%{appid}.svg -t %{buildroot}%{_scalableiconsdir}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/buzz
%{_appsdir}/%appid.desktop
%{_metainfodir}/%appid.metainfo.xml
%{_scalableiconsdir}/%appid.svg
%{python3_sitearch}/demucs/
%{python3_sitearch}/ctc_forced_aligner/
%{python3_sitearch}/deepmultilingualpunctuation/
%{python3_sitearch}/whisper_diarization/

%changelog
* Mon May 04 2026 Owen Zimmerman <owen@fyralabs.com> - 1.4.4-1
- Update for 1.4.4

* Thu Jan 01 2026 madonuko <mado@fyralabs.com> - 1.3.3-1
- Initial commit
