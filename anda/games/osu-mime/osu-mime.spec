Name:			osu-mime
Version:		0.1
Release:		1%{?dist}
Summary:		Provides MIME types for osu! file formats
BuildArch:		noarch
License:		AGPLv3
Requires:		xdg-utils shared-mime-info desktop-file-utils
BuildRequires:	librsvg2-tools ImageMagick
Recommends:		osu-handler
Source0:		https://raw.githubusercontent.com/ppy/osu-web/master/public/images/layout/osu-logo-triangles.svg
Source1:		https://raw.githubusercontent.com/ppy/osu-web/master/public/images/layout/osu-logo-white.svg
Source2:		osu-file-extensions.xml

%description
%{summary}.

%prep

%build
mkdir -p 'icons/hicolor'
for size in 16 24 32 48 64 96 128 192 256 384 512 1024; do
	mkdir -p "icons/hicolor/${size}x${size}/apps"
	cd "icons/hicolor/${size}x${size}/apps"

	rsvg-convert -w "$size" -h "$size" -f png -o "osu!.png.1" %{SOURCE0}
	rsvg-convert -w "$size" -h "$size" -f png -o "osu!.png.2" %{SOURCE1}
	convert -composite 'osu!.png.1' 'osu!.png.2' -gravity center 'osu!.png'
	rm 'osu!.png.1' 'osu!.png.2'

	cd ../../../..
done

%install
mkdir -p %{buildroot}/usr/share
cp -r --no-preserve=ownership icons %{buildroot}/usr/share/icons
install -D -m644 %{SOURCE2} %{buildroot}/usr/share/mime/packages/osu-file-extensions.xml

%post
xdg-icon-resource forceupdate --theme hicolor &>/dev/null
update-mime-database usr/share/mime &>/dev/null
update-desktop-database -q

%postun
xdg-icon-resource forceupdate --theme hicolor &>/dev/null
update-mime-database usr/share/mime &>/dev/null
update-desktop-database -q

%posttrans
xdg-icon-resource forceupdate --theme hicolor &>/dev/null
update-mime-database usr/share/mime &>/dev/null
update-desktop-database -q


%files
/usr/share/icons/hicolor/*/apps/osu!.png
/usr/share/mime/packages/osu-file-extensions.xml

%changelog
* Mon Feb 13 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
