Name:           icoextract-thumbnailer
Version:        0.2.0
Release:        1%?dist
Summary:        XDG-compatible thumbnailer for Windows PE executables

URL:            https://github.com/jlu5/icoextract/
License:        MIT
Source0:        %{url}/raw/refs/tags/%{version}/exe-thumbnailer.thumbnailer
Packager:       Cappy Ishihara <cappy@fyralabs.com>
BuildArch:      noarch
BuildRequires:  /usr/bin/install
Requires:       python3dist(icoextract)


%description
%{summary}.
This package supplements icoextract by providing the thumbnailer configuration file for file managers
that support XDG thumbnailers, such as Nautilus, Dolphin and Thunar.

%prep

%build



%install
install -Dm644 %{SOURCE0} %{buildroot}%{_datadir}/thumbnailers/exe-thumbnailer.thumbnailer


%files
%{_datadir}/thumbnailers/exe-thumbnailer.thumbnailer



%changelog
* Sat Dec 14 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial package
