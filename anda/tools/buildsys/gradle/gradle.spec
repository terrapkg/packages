Name:			gradle
Version:		9.3.0
Release:		1%?dist
Summary:		Powerful build system for the JVM
URL:			https://gradle.org/
Source0:		https://github.com/gradle/gradle/archive/refs/tags/v%{version}.tar.gz
License:		Apache-2.0
Requires:		java coreutils findutils sed which bash
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
%autosetup -n %{name}-%{version}

cat <<EOF > gradle.sh
#!/bin/sh
export GRADLE_HOME=/usr/share/java/gradle
EOF

%build
export PATH="/usr/lib/jvm/java-21-openjdk/bin:${PATH}"
./gradlew installAll --parallel \
	-Porg.gradle.java.installations.auto-download=false \
	-PfinalRelease=true \
	-Pgradle_installPath="$(pwd)/dist" \
	-Porg.gradle.ignoreBuildJavaVersionCheck=true \
	--warning-mode all \
	--no-configuration-cache

%install

# install profile.d script
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
install -Dm755 gradle.sh %{buildroot}/%{_sysconfdir}/profile.d/

# create the necessary directory structure
install -d "%{buildroot}%{_javadir}/%{name}/bin"
install -d "%{buildroot}%{_javadir}/%{name}/lib/plugins"
install -d "%{buildroot}%{_javadir}/%{name}/lib/agents"
install -d "%{buildroot}%{_javadir}/%{name}/init.d"

# copy across jar files
install -Dm644 dist/lib/*.jar "%{buildroot}%{_javadir}/%{name}/lib"
install -Dm644 dist/lib/plugins/*.jar "%{buildroot}%{_javadir}/%{name}/lib/plugins"
install -Dm644 dist/lib/agents/*.jar "%{buildroot}%{_javadir}/%{name}/lib/agents"

# copy across supporting text documentation and scripts
install -m644 dist/NOTICE "%{buildroot}%{_javadir}/%{name}"
mkdir -p %{buildroot}%{_javadir}/%{name}/bin
install -m755 dist/bin/%{name} "%{buildroot}%{_javadir}/%{name}/bin"
install -m644 dist/init.d/*.* "%{buildroot}%{_javadir}/%{name}/init.d"

# link gradle script to /usr/bin
mkdir -p "%{buildroot}/%{_bindir}"
ln -s %{_javadir}/%{name}/bin/%{name} "%{buildroot}%{_bindir}/%{name}"

install -d %{buildroot}%{_javadir}/%{name}/docs
cp -r dist/docs/* %{buildroot}%{_javadir}/%{name}/docs

install -d %{buildroot}%{_javadir}/%{name}/src
cp -r dist/src/* %{buildroot}%{_javadir}/%{name}/src

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/profile.d/gradle.sh
%{_javadir}/%{name}/
%{_bindir}/%{name}

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
- Pull in adoptium repo, fix many build issues, change source to GitHub release artifacts

* Tue Feb 7 2023 madonuko <mado@fyralabs.com>
- Initial package
