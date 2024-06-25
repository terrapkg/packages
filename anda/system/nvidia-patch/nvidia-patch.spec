%global debug_package %{nil}
%global commit 564c0661a942f7163cb2cfa6cb1b14b4bcff3a30
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240218


%global patches %{_datadir}/src/nvidia-patch
Name:           nvidia-patch
Version:        0^%commit_date.%{shortcommit}
Release:        1%{?dist}
Summary:        NVENC and NvFBC patches for NVIDIA drivers

License:        EULA
URL:            https://github.com/keylase/nvidia-patch
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  tar
Requires:       akmod-nvidia

%description
NVENC patch removes restriction on maximum number of simultaneous NVENC video encoding sessions imposed by Nvidia to consumer-grade GPUs.

NvFBC patch allows to use NvFBC on consumer-grade GPUs. It should be applied same way as NVENC patch.sh, except you have to use patch-fbc.sh instead

%prep
%autosetup -n nvidia-patch-%{commit}

rm -rf win/
%build

%install
# install current folder to /usr/share/src/nvidia-patch
mkdir -p %{buildroot}%{patches}
cp -va * %{buildroot}/usr/share/src/nvidia-patch



%post
cd /usr/share/src/nvidia-patch
./patch.sh || :
./patch.sh -f || :
./patch-fbc.sh || :
./patch-fbc.sh -f || :

%preun
cd /usr/share/src/nvidia-patch
./patch.sh -r || :
./patch.sh -f -r || :
./patch-fbc.sh -r || :
./patch-fbc.sh -f -r || :

# on update
%posttrans
if [ $1 -gt 1 ]; then
    cd /usr/share/src/nvidia-patch
    ./patch.sh || :
    ./patch.sh -f || :
    ./patch-fbc.sh || :
    ./patch-fbc.sh -f || :
fi
# trigger for when akmod-nvidia gets installed
%triggerin -- akmod-nvidia
cd /usr/share/src/nvidia-patch
./patch.sh || :
./patch.sh -f || :
./patch-fbc.sh || :
./patch-fbc.sh -f || :

%files
%doc README.md
%dir %{_datadir}/src/nvidia-patch
%{_datadir}/src/nvidia-patch/*


%changelog
* Mon Nov 06 2023 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial package
