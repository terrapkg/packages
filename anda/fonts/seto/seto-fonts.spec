Name:      seto-fonts
Version:   6.20
Release:   4%?dist
URL:       https://web.archive.org/web/20240226230836/https://ja.osdn.net/projects/setofont/
Source0:   https://github.com/terrapkg/pkg-seto-fonts/archive/refs/tags/%version.tar.gz
License:   OFL-1.1
Summary:   A handwritten font that contains kanji up to JIS 4th level and difficult kanji
BuildArch: noarch


%description
%summary.


%prep
%setup -q -n pkg-seto-fonts-%version

%build

%install
mkdir -p %buildroot/%_datadir/fonts/%name
install -Dm644 *.ttf %buildroot/%_datadir/fonts/%name/


%files
%doc readme.txt
%license LICENSE.md
%_datadir/fonts/%name/

%changelog
%autochangelog
