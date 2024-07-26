%global srcname sound-theme

Name:           elementary-sound-theme
Summary:        Set of system sounds for elementary
Version:        1.1.0
Release:        2%?dist
License:        Unlicense AND CC-BY-4.0

# Unlicense:
# - audio-volume-change
# - bell
# - dialog-information
# Creative Commons Attribution:
# - dialog-warning:
#   https://notificationsounds.com/standard-ringtones/answer-quickly-45

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson

BuildArch:      noarch

%description
A set of system sounds for elementary OS. Designed to be light, natural/
physical, and pleasant.


%prep
%autosetup -n %{srcname}-%{version}


%build
%meson
%meson_build


%install
%meson_install



%files
%doc README.md
%license LICENSE

%{_datadir}/sounds/elementary/


%changelog
%autochangelog
