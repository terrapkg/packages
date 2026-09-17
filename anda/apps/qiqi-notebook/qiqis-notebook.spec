# Make electron_license macro properly work
%bcond bundled_electron 1


Name:			qiqis-notebook
%electronmeta -D
Version:		1.1.6
Release:		1%?dist
Summary:		Qiqi's Notebook desktop app
URL:			https://qiqis-notebook.com/
Source0:		https://github.com/Qiqis-Notebook/qnb-client/archive/refs/tags/v%{version}.tar.gz
Source1:		qiqis-notebook.desktop
License:		MIT AND %{electron_license}
Packager:   Yoong Jin <solomoncyj@gmail.com>

BuildRequires:	 nodejs-npm
BuildRequires:	 squashfs-tools

Provides:       qnb-client

%description
Qiqi's Notebook is an application used for launcing
user created farming routes for Genshin Impact and
Wuthering Waves

%prep
%autosetup -n  qnb-client-%{version}

%build
%npm_build -r package
#npm i
#npm run package
cd "out/Qiqi's Notebook-linux-%{_electron_cpu}"
mv ./* ..
cd ..
mv "Qiqi's Notebook" ./qiqis-notebook

mv ./LICENSE ./LICENSE.electron

%install
cd ./out

install -Dm755 ./libEGL.so %{buildroot}%{_libdir}/qiqis-notebook/libEGL.so
install -Dm755 ./libGLESv2.so %{buildroot}%{_libdir}/qiqis-notebook/libGLESv2.so
install -Dm755 ./libffmpeg.so %{buildroot}%{_libdir}/qiqis-notebook/libffmpeg.so
install -Dm755 ./libvk_swiftshader.so %{buildroot}%{_libdir}/qiqis-notebook/libvk_swiftshader.so
install -Dm755 ./libvulkan.so.1 %{buildroot}%{_libdir}/qiqis-notebook/libvulkan.so.1
install -Dm644 ./icudtl.dat %{buildroot}%{_libdir}/qiqis-notebook/icudtl.dat
install -Dm644 ./v8_context_snapshot.bin %{buildroot}%{_libdir}/qiqis-notebook/v8_context_snapshot.bin
install -Dm644 ./chrome_100_percent.pak %{buildroot}%{_libdir}/qiqis-notebook/chrome_100_percent.pak
install -Dm644 ./chrome_200_percent.pak %{buildroot}%{_libdir}/qiqis-notebook/chrome_200_percent.pak
install -Dm644 ./resources.pak %{buildroot}%{_libdir}/qiqis-notebook/resources.pak
install -Dm644 ./vk_swiftshader_icd.json %{buildroot}%{_libdir}/qiqis-notebook/vk_swiftshader_icd.json
install -Dm644 ./resources/app.asar %{buildroot}%{_libdir}/qiqis-notebook/resources/app.asar
install -Dm755 ./chrome-sandbox %{buildroot}%{_libdir}/qiqis-notebook/chrome-sandbox
install -Dm755 ./chrome_crashpad_handler %{buildroot}%{_libdir}/qiqis-notebook/chrome_crashpad_handler
install -Dm755 ./qiqis-notebook %{buildroot}%{_libdir}/qiqis-notebook/qiqis-notebook


mkdir  %{buildroot}%{_libdir}/qiqis-notebook/locales/
cp -r locales/*  %{buildroot}%{_libdir}/qiqis-notebook/locales/
chmod -R 755 %{buildroot}%{_libdir}/qiqis-notebook/locales/

cd ..

install -Dm644 assets/logo.png %{buildroot}%{_hicolordir}/1024x1024/apps/qiqis-notebook.png

install -Dm644 %{SOURCE1} %{buildroot}%{_appsdir}/qiqis-notebook.desktop

mkdir -p %{buildroot}%{_bindir}

ln -s %{_libdir}/qiqis-notebook/qiqis-notebook %{buildroot}%{_bindir}/qiqis-notebook

%check
desktop-file-validate %{buildroot}%{_appsdir}/qiqis-notebook.desktop

%files
%doc README.md
%license ./out/LICENSE.electron
%license ./out/LICENSES.chromium.html
%license LICENSE
%{_bindir}/qiqis-notebook
%{_libdir}/qiqis-notebook/
%{_appsdir}/qiqis-notebook.desktop
%{_hicolordir}/1024x1024/apps/qiqis-notebook.png

%changelog
* Sat Jan 17 2026 Yoong Jin <solomoncyj@gmail.com> - 1.1.6
- Initial package.
