Name:			gradle
Version:		9.2.1
Release:		1%?dist
Summary:		Powerful build system for the JVM
URL:			https://gradle.org/
Source0:		https://services.gradle.org/distributions/%{name}-%{version}-src.zip
Source1:		https://services.gradle.org/distributions/%{name}-%{version}-all.zip
License:		Apache-2.0
Requires:		java-latest-openjdk coreutils findutils sed which bash
BuildRequires:	java-21-openjdk-devel asciidoc xmlto groovy unzip git
BuildRequires:  temurin-17-jdk temurin-17-jre anda-srpm-macros
BuildArch:		noarch
Recommends:		gradle-doc gradle-src

%description
Gradle is a build tool with a focus on build automation and support for multi-language development. If you are building, testing, publishing, and deploying software on any platform, Gradle offers a flexible model that can support the entire development lifecycle from compiling and packaging code to publishing web sites. Gradle has been designed to support build automation across multiple languages and platforms including Java, Scala, Android, Kotlin, C/C++, and Groovy, and is closely integrated with development tools and continuous integration servers including Eclipse, IntelliJ, and Jenkins.

%package doc
Summary:	Gradle documentation
%description doc
Documentation for gradle, a powerful build system for the JVM.

%package src
Summary:	Gradle sources
%description src
Sources for gradle, a powerful build system for the JVM.

%prep
%git_clone https://github.com/gradle/gradle.git v%version

cat <<EOF > gradle.sh
#!/bin/sh
export GRADLE_HOME=/usr/share/java/gradle
EOF

# remove ADOPTIUM contraint from all build related files
sed -i '/JvmVendorSpec.ADOPTIUM/d' \
	build-logic/jvm/src/main/kotlin/gradlebuild.unittest-and-compile.gradle.kts \
#	subprojects/docs/src/snippets/java/toolchain-filters/groovy/build.gradle \
#	subprojects/docs/src/snippets/java/toolchain-filters/kotlin/build.gradle.kts \
#	build-logic-commons/gradle-plugin/src/main/kotlin/common.kt
# inhibit automatic download of binary gradle
sed -i "s#distributionUrl=.*#distributionUrl=file\:%{SOURCE1}#" \
	gradle/wrapper/gradle-wrapper.properties

%build
%dnl cd %{name}-%{version}
export PATH="/usr/lib/jvm/java-21-openjdk/bin:${PATH}"
./gradlew installAll --parallel \
	-Porg.gradle.java.installations.auto-download=false \
	-PfinalRelease=true \
	-Pgradle_installPath="$(pwd)/dist" \
	-Porg.gradle.ignoreBuildJavaVersionCheck=true \
	--warning-mode all \
	--no-configuration-cache

%install
%dnl cd %{name}-%{version}/dist

# install profile.d script
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d/
install -Dm755 gradle.sh %{buildroot}/%{_sysconfdir}/profile.d/

# create the necessary directory structure
install -d "%{buildroot}%{_javadir}/%{name}/bin"
install -d "%{buildroot}%{_javadir}/%{name}/lib/plugins"
install -d "%{buildroot}%{_javadir}/%{name}/init.d"

# copy across jar files
install -Dm644 dist/lib/*.jar "%{buildroot}%{_javadir}/%{name}/lib"
install -Dm644 dist/lib/plugins/*.jar "%{buildroot}%{_javadir}/%{name}/lib/plugins"

# copy across supporting text documentation and scripts
install -m644 dist/NOTICE "%{buildroot}%{_javadir}/%{name}"
mkdir -p %{buildroot}/%{_javadir}/%{name}/bin
install -m755 dist/bin/gradle "%{buildroot}%{_javadir}/%{name}/bin"
install -m644 dist/init.d/*.* "%{buildroot}%{_javadir}/%{name}/init.d"

# link gradle script to /usr/bin
ln -s %{_javadir}/%{name}/bin/%{name} "%{buildroot}/usr/bin"S

install -d %{buildroot}%{_javadir}/gradle/docs
cp -r dist/docs/* %{buildroot}%{_javadir}/gradle/docs

install -d %{buildroot}%{_javadir}/gradle/src
cp -r dist/src/* %{buildroot}%{_javadir}/gradle/src

%dnl install -Dm644 %{SOURCE2} %{buildroot}/%{_datadir}/licenses/%{name}/
%dnl install -Dm644 %{SOURCE2} %{buildroot}/%{_datadir}/licenses/%{name}-doc/
%dnl install -Dm644 %{SOURCE2} %{buildroot}/%{_datadir}/licenses/%{name}-src/
%dnl install -Dm644 %{SOURCE3} %{buildroot}/%{_datadir}/doc/%{name}/
%dnl install -Dm644 %{SOURCE3} %{buildroot}/%{_datadir}/doc/%{name}-doc/
%dnl install -Dm644 %{SOURCE3} %{buildroot}/%{_datadir}/doc/%{name}-src/

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/profile.d/gradle.sh
%{_javadir}/%{name}/
%dnl %{_bindir}/%{name}
/usr/binS

%files doc
%doc README.md
%license LICENSE
%{_javadir}/%{name}/docs

%files src
%doc README.md
%license LICENSE
%{_javadir}/%{name}/src

%changelog
* Fri Dec 05 2025 Owen Zimmerman <owen@fyralabs.com>
- Pull in adoptium repo, fix some build issues

* Tue Feb 7 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
