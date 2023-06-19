Name:       naikai-fonts
Version:    1.89
Release:    %autorelease
URL:        https://github.com/max32002/naikaifont
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz
License:    OFL-1.1
Summary:    A free font family derived from setofont
BuildRequires: unzip
BuildArch:  noarch

%description
%{summary}.

%package jp
Summary:    A free font family derived from setofont (JP version)
%description jp
%{summary}.
瀬戸フォントに由来、たくさん中国語文字を加えた無料なフォント。

%package tw
Summary:    A free font family derived from setofont (TW version)
%description tw
%{summary}.
瀨戶字體的繁體中文補字計畫。


%prep
%setup -q -n naikaifont-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/%{name}-{jp,tw}/
install -Dm644 jp/*.ttf %{buildroot}/%{_datadir}/fonts/%{name}-jp/
install -Dm644 tw/*.ttf %{buildroot}/%{_datadir}/fonts/%{name}-tw/


%files jp
%doc README.md
%license SIL_Open_Font_License_1.1.txt
/%{_datadir}/fonts/%{name}-jp

%files tw
%doc README.md
%license SIL_Open_Font_License_1.1.txt
/%{_datadir}/fonts/%{name}-tw

%changelog
* Tue Nov 22 2022 windowsboy111 <windowsboy111@fyralabs.com> - 1.87
- Initial package
