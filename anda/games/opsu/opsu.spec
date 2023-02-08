Name:		opsu
Version:	0.16.1
Release:	1%{?dist}
URL:		https://itdelatrisu.github.io/opsu/
Source0:	https://github.com/itdelatrisu/opsu/releases/download/%{version}/opsu-%{version}.jar
Source1:	https://github.com/itdelatrisu/opsu/raw/%{version}/res/logo.png
Source2:	https://raw.githubusercontent.com/itdelatrisu/opsu/%{version}/LICENSE
Source3:	https://raw.githubusercontent.com/itdelatrisu/opsu/%{version}/README.md
License:	GPLv3
Summary:	An open source osu!-client written in Java
Requires:	java-latest-openjdk hicolor-icon-theme xrandr
Recommends:	ffmpeg
BuildArch:	noarch

%description
opsu! is an unofficial open-source client for the rhythm game osu!, written in Java using Slick2D and LWJGL (wrappers around OpenGL and OpenAL).

%prep

%build
cat <<EOF > %{name}.sh
#!/bin/sh
exec /usr/bin/java -jar '/usr/share/java/opsu/opsu.jar' "\$@"
EOF

cat <<EOF > %{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Opsu!
Comment=An open source osu!-client written in Java.
Exec=opsu
Icon=opsu
Terminal=false
StartupNotify=false
Categories=Game;ActionGame;
EOF

%install
mkdir -p %{buildroot}/usr/share/{applications,{licenses,doc}/%{name}}
install -Dm644 %{name}.sh %{buildroot}/usr/bin/%{name}
install -Dm644 %{SOURCE0} %{buildroot}/usr/share/java/%{name}/%{name}.jar
install -Dm644 %{SOURCE1} %{buildroot}/usr/share/icons/hicolor/scalable/apps/%{name}.png
install -Dm644 %{name}.desktop %{buildroot}/usr/share/applications/
install -Dm644 %{SOURCE2} "%{buildroot}/%{_datadir}/licenses/%{name}/LICENSE"
install -Dm644 %{SOURCE3} "%{buildroot}/%{_datadir}/doc/%{name}/README.md"

%files
%doc README.md
%license LICENSE
/usr/bin/%{name}
/usr/share/java/%{name}/%{name}.jar
/usr/share/icons/hicolor/scalable/apps/%{name}.png
/usr/share/applications/%{name}.desktop

%changelog
* Tue Feb 7 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
