%global debug_package %{nil}

Name:           avs-tplg-conf
Version:        2024.02
Release:        1%?dist

License:        Apache-2.0
Summary:        Configuration files for Intel AudioVoiceSpeech (AVS) driver
URL:            https://github.com/thesofproject/avs-topology-xml
Source0:        https://github.com/thesofproject/avs-topology-xml/releases/download/v%version/avs-topology_%version.tar.gz

Conflicts:      alsa-sof-firmware

%description
Configuration files for Intel AudioVoiceSpeech (AVS) driver. Each configuration file represents an audio stream topology i.e.: connections of AudioDSP pipelines and processing modules that provide rich user experience with the Intel AVS stack. The avs-driver is part of the Linux kernel sound subsystem, sound/soc/intel/avs.

%prep
%autosetup -n avs-topology
rm lib/firmware/intel/avs/max98357a-tplg.bin # according to tree this might blow up speakers, so let's not include it

%build
xz -z lib/firmware/intel/avs/*.bin

%install
mkdir -p %buildroot/lib/firmware/intel/avs
cp lib/firmware/intel/avs/*.bin.xz %buildroot/lib/firmware/intel/avs/

%files
%license LICENSE
/lib/firmware/intel/avs/*

%changelog
%autochangelog
