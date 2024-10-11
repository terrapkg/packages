Name:			intellij-community-idea
Version:		231.9161.38
Release:		1%?dist
Summary:		IDE for Java/Groovy/etc. with advanced refactoring features
License:		Apache-2.0
URL:			https://jetbrains.com/idea
Source0:		https://github.com/JetBrains/intellij-community/archive/refs/tags/idea/%version.tar.gz
Source1:		https://github.com/JetBrains/android/archive/refs/tags/idea/%version.tar.gz
Source2:		https://repo1.maven.org/maven2/junit/junit/3.8.1/junit-3.8.1.jar
Patch0:			enable-no-jdr.patch
Requires:		giflib java-17-openjdk python3 bash libdbusmenu fontconfig hicolor-icon-theme
BuildRequires:	ant git java-17-openjdk-devel maven

%description
Intellij IDEA is an IDE for Java, Groovy and other programming languages with
advanced refactoring features.

%prep
%autosetup -p1
tar xf %SOURCE1

cat<<EOF > idea.desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=IntelliJ IDEA Community Edition
Comment=Develop with pleasure!
Exec=/usr/bin/idea %f
Icon=idea
Terminal=false
StartupNotify=true
StartupWMClass=jetbrains-idea-ce
Categories=Development;IDE;Java;
EOF


cat<<EOF > idea.sh
#!/bin/sh
if [ -z "$IDEA_JDK" ] ; then
	IDEA_JDK="/usr/lib/jvm/java-17-openjdk/"
fi
# open-jfx location that should match the JDK version
if [ -z "$IDEA_JFX" ] ; then
	IDEA_JFX="/usr/lib/jvm/java-17-openjfx/"
fi
# classpath according to defined JDK/JFX
if [ -z "$IDEA_CLASSPATH" ] ; then
IDEA_CLASSPATH="${IDEA_JDK}/lib/*:${IDEA_JFX}/lib/*"
fi

exec env IDEA_JDK="$IDEA_JDK" IDEA_CLASSPATH="$IDEA_CLASSPATH" %_datadir/idea/bin/idea.sh "$@"
EOF


%build
export MAVEN_REPOSITORY=%HOME/.m2/repository
mvn install:install-file -Dfile=%SOURCE2 -DgroupId=junit -DartifactId=junit -Dversion=3.8.1 -Dpackaging=jar -DgeneratePom=true

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
export PATH="/usr/lib/jvm/java-17-openjdk/bin:$PATH"

./installers.cmd -Dintellij.build.use.compiled.classes=false -Dintellij.build.target.os=linux

tar xf out/idea-ce/artifacts/ideaIC-%version-no-jbr.tar.gz -C .


%install
cd idea-IC-%version
install -dm755 %buildroot%_datadir/{pixmaps,idea,icons/hicolor/scalable/apps}
cp -dr --no-preserve='ownership' bin lib plugins %buildroot%_datadir/idea/
ln -s %_datadir/idea/bin/idea.png %buildroot%_datadir/pixmaps/
ln -s %_datadir/idea/bin/idea.svg %buildroot%_datadir/icons/hicolor/scalable/apps/
install -Dm644 ../idea.desktop -t %buildroot%_datadir/applications/
install -Dm755 ../idea.sh %buildroot/%_bindir/idea
chmod +x %buildroot/%_bindir/idea
echo %version > build.txt
install -Dm644 build.txt -t %buildroot%_datadir/idea


%files
%doc README.md docs/
%license idea-IC-%version/license
%_datadir/pixmaps/idea.png
%_datadir/icons/hicolor/scalable/apps/idea.svg
%_datadir/applications/idea.desktop
%_bindir/idea
%_datadir/idea/

%changelog
%autochangelog
