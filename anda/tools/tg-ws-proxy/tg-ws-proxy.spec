%global debug_package %{nil}

Name:           tg-ws-proxy
Version:        1.6.5
Release:        1%?dist
Summary:        Local MTProto proxy server for partial bypassing of Telegram loading

License:        MIT
URL:            https://github.com/Flowseal/tg-ws-proxy
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        tg-ws-proxy.desktop
Source2:        tg-ws-proxy.service

BuildRequires:  python3 python3-tkinter python3-pip libappindicator libayatana-appindicator-gtk3 ImageMagick

Requires:       python3 python3-tkinter libappindicator libayatana-appindicator-gtk3

Packager:       veuxit <erroor234@gmail.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}


%build
python -m venv .venv
    .venv/bin/pip install --upgrade pip 
    .venv/bin/pip install "."
    .venv/bin/pip install "pyinstaller"
    .venv/bin/pyinstaller --noconfirm packaging/linux.spec

rm -rf .venv

%install
install -Dm 755 dist/TgWsProxy %{buildroot}%{_bindir}/tg-ws-proxy

magick "icon.ico" -background none -alpha on tg-ws-proxy.png

install -Dm644 tg-ws-proxy.png %{buildroot}%{_hicolordir}/64x64/apps/tg-ws-proxy.png

install -Dm644 %{SOURCE1} %{buildroot}%{_appsdir}/tg-ws-proxy.desktop

install -Dm644 %{SOURCE2} -t %{buildroot}/%{_unitdir}

%post
%systemd_post tg-ws-proxy.service

%preun
%systemd_preun tg-ws-proxy.service

%postun
%systemd_postun_with_restart tg-ws-proxy.service

%files
%doc docs/README.md docs/CfProxy.md
%license LICENSE
%{_bindir}/tg-ws-proxy
%{_hicolordir}/64x64/apps/tg-ws-proxy.png
%{_unitdir}/tg-ws-proxy.service
%{_appsdir}/tg-ws-proxy.desktop


%changelog
* Sun May 3 2026 veuxit <erroor234@gmail.com>
- Initial commit
