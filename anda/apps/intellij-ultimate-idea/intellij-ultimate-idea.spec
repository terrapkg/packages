%global buildver 231.9161.38
%global jbr_ver 17.0.6
%global jbr_build aarch64-b469
%global jbr_minor 82

Name:		intellij-ultimate-idea
Version:	2023.1.3
Release:	1%?dist
Summary:	IDE for Java/Groovy/etc. with advanced refactoring features
License:	Unlicense
URL:		https://jetbrains.com/idea
Source0:	https://download.jetbrains.com/idea/ideaIU-%version.tar.gz
Requires:	giflib libXtst libXrender
Suggests:	%name-jre
Recommends:	libdbusmenu java-17-openjdk


%ifarch aarch64
Source1:	https://cache-redirector.jetbrains.com/intellij-jbr/jbr-%jbr_ver-linux-%jbr_build.%jbr_minor.tar.gz
Source2:	https://github.com/JetBrains/intellij-community/raw/master/bin/linux/aarch64/fsnotifier
%endif


%description
Intellij IDEA is an IDE for Java, Groovy and other programming languages with
advanced refactoring features.


%package jre
Summary:	IDE for Java/Groovy/etc. with advanced refactoring features

%description jre
Intellij IDEA is an IDE for Java, Groovy and other programming languages with
advanced refactoring features.


%prep
%autosetup -n idea-IU-%buildver

# https://youtrack.jetbrains.com/articles/IDEA-A-48/JetBrains-IDEs-on-AArch64#linux
%ifarch aarch64
	cp -a . jbr
	cp -f fsnotifier bin/fsnotifier
	chmod +x bin/fsnotifier
	rm -rf jbr
%else
	mv idea-IU-%buildver/jbr jbr
%endif


cat<<EOF > jetbrains-idea.desktop
[Desktop Entry]
Name=IntelliJ IDEA Ultimate Edition
Comment=Intelligent Java IDE
Exec=intellij-idea-ultimate-edition %u
Icon=intellij-idea-ultimate-edition
Terminal=false
StartupWMClass=jetbrains-idea
Type=Application
Categories=Development;IDE;
EOF


%build

%install
install -d %buildroot%_bindir %buildroot%_datadir/%name
mv * %buildroot%_datadir/%name
# https://youtrack.jetbrains.com/issue/IDEA-185828
chmod +x %buildroot%_datadir/%name/plugins/maven/lib/maven3/bin/mvn
ln -s %_datadir/%name/bin/idea.sh %buildroot%_bindir/%name
install -Dm644 jetbrains-idea.desktop %buildroot%_datadir/applications/jetbrains-idea.desktop
install -Dm644 %buildroot%_datadir/%name/bin/idea.svg %buildroot%_datadir/pixmaps/%name.svg

# workaround FS#40934
sed -i 's|lcd|on|' %buildroot/%name/bin/*.vmoptions

mv jbr %buildroot%_datadir/%name

%files
%_datadir/%name
%_bindir/%name
%_datadir/applications/jetbrains-idea.desktop
%_datadir/pixmaps/%name.svg

%files jre
%buildroot%_datadir/%name/jbr

%changelog
%autochangelog
