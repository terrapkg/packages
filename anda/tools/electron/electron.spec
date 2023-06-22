%define debug_package %{nil}
%ifarch x86_64
%global garch x64
%elifarch aarch64
%global garch arm64
%endif

Name:			electron
Version:		25.2.0
Release:		1%{?dist}
Summary:		Build cross platform desktop apps with web technologies
License:		MIT
URL:			https://electronjs.org/
Source0:		https://github.com/electron/electron/releases/download/v%{version}/chromedriver-v%{version}-linux-%{garch}.zip
Source1:		https://github.com/electron/electron/releases/download/v%{version}/electron-v%{version}-linux-%{garch}.zip
Source2:		https://raw.githubusercontent.com/electron/electron/v%version/README.md
Requires:		c-ares gtk3 minizip nss re2
Requires:		(ffmpeg-free or ffmpeg)
BuildRequires:	unzip

%description
The Electron framework lets you write cross-platform desktop applications using
JavaScript, HTML and CSS. It is based on Node.js and Chromium and is used by
the Atom editor and many other apps.

%prep
unzip %{SOURCE0}
unzip -o %{SOURCE1}

%build

%install
install -dm755 %{buildroot}/usr/lib/%{name}/
find . -mindepth 1 -maxdepth 1 -type f ! -name "*.zip" ! -name "LICENSE*" -exec cp -r --no-preserve=ownership --preserve=mode -t %{buildroot}/usr/lib/%{name}/. {} +

for _folder in 'locales' 'resources'; do
	cp -r --no-preserve=ownership --preserve=mode "${_folder}/" %{buildroot}/usr/lib/%{name}/${_folder}/
done

chmod 0755 %buildroot/usr/lib/%name/chrome-sandbox

install -dm755 %{buildroot}/usr/bin
ln -nfs /usr/lib/%{name}/%{name} %{buildroot}/usr/bin/%{name}
mkdir -p %buildroot%_docdir/%name/
install -Dm644 %SOURCE2 %buildroot%_docdir/%name/


%files
%doc README.md
%license LICENSE
%license LICENSES.chromium.html
/usr/lib/electron
/usr/bin/electron


%changelog
* Fri Feb 10 2023 windowsboy111 <windowsboy111@fyralabs.com> - 20.3.12-1
- Initial package
