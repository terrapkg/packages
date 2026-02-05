Name:			electron
%electronmeta
Version:		39.5.1
Release:		1%?dist
Summary:		Build cross platform desktop apps with web technologies
License:		%{electron_license}
URL:			https://electronjs.org/
Source0:		https://github.com/electron/electron/releases/download/v%{version}/chromedriver-v%{version}-linux-%{_electron_cpu}.zip
Source1:		https://github.com/electron/electron/releases/download/v%{version}/electron-v%{version}-linux-%{_electron_cpu}.zip
Source2:		https://raw.githubusercontent.com/electron/electron/v%version/README.md
BuildRequires:  anda-srpm-macros >= 0.2.26

%description
The Electron framework lets you write cross-platform desktop applications using
JavaScript, HTML and CSS. It is based on Node.js and Chromium and is used by
the Atom editor and many other apps.

%prep
unzip %{SOURCE0}
unzip -o %{SOURCE1}

%build

%install
install -dm755 %buildroot%_libdir/%name/
find . -mindepth 1 -maxdepth 1 -type f ! -name "*.zip" ! -name "LICENSE*" -exec cp -r --no-preserve=ownership --preserve=mode -t %buildroot%_libdir/%name/. {} +

for _folder in 'locales' 'resources'; do
	cp -r --no-preserve=ownership --preserve=mode "${_folder}/" %buildroot%_libdir/%name/${_folder}/
done

chmod 0755 %buildroot%_libdir/%name/chrome-sandbox

install -dm755 %buildroot%_bindir
ln -nfs %_libdir/%name/%name %buildroot%_bindir/%name
mkdir -p %buildroot%_docdir/%name/
install -Dm644 %SOURCE2 %buildroot%_docdir/%name/


%files
%doc README.md
%license LICENSE
%license LICENSES.chromium.html
%_libdir/%name
%_bindir/%name


%changelog
* Fri Feb 10 2023 madonuko <mado@fyralabs.com> - 20.3.12-1
- Initial package
