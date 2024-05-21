Name:		sarasa-gothic-fonts
Version:	1.0.12
Release:	1%?dist
URL:		https://github.com/be5invis/Sarasa-Gothic
Source0:	%url/releases/download/v%version/Sarasa-TTC-%version.7z
Source1:	%url/releases/download/v%version/Sarasa-SuperTTC-%version.7z
Source2:	https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/v%version/LICENSE
Source3:	https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/v%version/README.md
License:	OFL-1.1
Summary:	Sarasa Gothic / 更纱黑体 / 更紗黑體 / 更紗ゴシック / 사라사 고딕
BuildArch:	noarch
BuildRequires:	p7zip-plugins

%description
A CJK programming font based on Iosevka and Source Han Sans.

%package -n sarasa-gothic-super-fonts
Summary: Sarasa Gothic / 更纱黑体 / 更紗黑體 / 更紗ゴシック / 사라사 고딕

%description -n sarasa-gothic-super-fonts
A CJK programming font based on Iosevka and Source Han Sans.


%prep
mkdir ttc
cd ttc
7z e %SOURCE0
cd ..
mkdir super
cd super
7z e %SOURCE1

%build

%install
mkdir -p %buildroot/%_datadir/{fonts/sarasa-gothic{,-super},{licenses,doc}/sarasa-gothic{,-super}-fonts}
cd ttc
install -Dm644 *.ttc %buildroot/%_datadir/fonts/sarasa-gothic/
cd ..
cd super
install -Dm644 *.ttc %buildroot/%_datadir/fonts/sarasa-gothic-super/
cd ..
install -Dm644 %SOURCE2 %buildroot/%_datadir/licenses/%name/
install -Dm644 %SOURCE3 %buildroot/%_datadir/doc/%name/
install -Dm644 %SOURCE2 %buildroot/%_datadir/licenses/sarasa-gothic-super-fonts/
install -Dm644 %SOURCE3 %buildroot/%_datadir/doc/sarasa-gothic-super-fonts/


%files
%doc README.md
%license LICENSE
/%{_datadir}/fonts/sarasa-gothic/

%files -n sarasa-gothic-super-fonts
%doc README.md
%license LICENSE
/%{_datadir}/fonts/sarasa-gothic-super/

%changelog
%autochangelog
