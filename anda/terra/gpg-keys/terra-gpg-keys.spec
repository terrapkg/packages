%undefine dist

Name:           terra-gpg-keys
Version:        %{?fedora:%{fedora}}%{?rhel:%{rhel}}
Release:        3%?dist
Summary:        GPG keys for Terra
Requires:       filesystem >= 3.18-6

License:        MIT
URL:            https://terra.fyralabs.com
# We aren't pulling keys from the origin URLs, since they shouldn't change and this is easier to audit.
Source0:        RPM-GPG-KEY-terrarawhide
Source1:        RPM-GPG-KEY-terrarawhide-extras
Source2:        RPM-GPG-KEY-terrarawhide-extras-source
Source3:        RPM-GPG-KEY-terrarawhide-mesa
Source4:        RPM-GPG-KEY-terrarawhide-mesa-source
Source5:        RPM-GPG-KEY-terrarawhide-multimedia
Source6:        RPM-GPG-KEY-terrarawhide-multimedia-source
Source7:        RPM-GPG-KEY-terrarawhide-nvidia
Source8:        RPM-GPG-KEY-terrarawhide-nvidia-source
Source9:        RPM-GPG-KEY-terrarawhide-source
Source10:       RPM-GPG-KEY-terra42
Source11:       RPM-GPG-KEY-terra42-extras
Source12:       RPM-GPG-KEY-terra42-extras-source
Source13:       RPM-GPG-KEY-terra42-mesa
Source14:       RPM-GPG-KEY-terra42-mesa-source
Source15:       RPM-GPG-KEY-terra42-multimedia
Source16:       RPM-GPG-KEY-terra42-multimedia-source
Source17:       RPM-GPG-KEY-terra42-nvidia
Source18:       RPM-GPG-KEY-terra42-nvidia-source
Source19:       RPM-GPG-KEY-terra42-source
Source20:       RPM-GPG-KEY-terra43
Source21:       RPM-GPG-KEY-terra43-extras
Source22:       RPM-GPG-KEY-terra43-extras-source
Source23:       RPM-GPG-KEY-terra43-mesa
Source24:       RPM-GPG-KEY-terra43-mesa-source
Source25:       RPM-GPG-KEY-terra43-multimedia
Source26:       RPM-GPG-KEY-terra43-multimedia-source
Source27:       RPM-GPG-KEY-terra43-nvidia
Source28:       RPM-GPG-KEY-terra43-nvidia-source
Source29:       RPM-GPG-KEY-terra43-source
Source30:       RPM-GPG-KEY-terra44
Source31:       RPM-GPG-KEY-terra44-extras
Source32:       RPM-GPG-KEY-terra44-extras-source
Source33:       RPM-GPG-KEY-terra44-mesa
Source34:       RPM-GPG-KEY-terra44-mesa-source
Source35:       RPM-GPG-KEY-terra44-multimedia
Source36:       RPM-GPG-KEY-terra44-multimedia-source
Source37:       RPM-GPG-KEY-terra44-nvidia
Source38:       RPM-GPG-KEY-terra44-nvidia-source
Source39:       RPM-GPG-KEY-terra44-source
Source40:       RPM-GPG-KEY-terrael10
Source41:       RPM-GPG-KEY-terrael10-source
BuildArch:      noarch

%description
GPG keys for Terra, used for verifying RPM package signatures.

%prep

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 %{_sourcedir}/RPM-GPG-KEY* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%files
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/RPM-GPG-KEY-*
