BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Name:           kotlin
Version:        2.0.0
Release:        1%?dist
Summary:        Statically typed programming language

License:        Apache-2.0
URL:            https://kotlinlang.org/
Source0:        https://github.com/JetBrains/kotlin/releases/download/v%{version}/kotlin-compiler-%{version}.zip
Source1:        https://raw.githubusercontent.com/JetBrains/kotlin/v%version/ReadMe.md

BuildRequires:  unzip
BuildRequires:  sed
BuildRequires:  bash
BuildRequires:  (java-headless >= 1:1.8.0 or java >= 1.8.0)
Requires:       (java-headless >= 1:1.8.0 or java >= 1.8.0)
BuildRequires:  fdupes


%description
Kotlin is a statically typed programming language that targets the JVM,
Android, JavaScript and Native (via kotlin-native). Developed by JetBrains,
the project started in 2010 and had its official 1.0 release in 2016.


%prep
unzip -o %{SOURCE0} && cd kotlinc
sed -i "s|\(DIR *= *\).*|\1%{_bindir}|" bin/*
sed -i "s|\(KOTLIN_HOME *= *\).*|\1%{_datadir}/%{name}|" bin/*


%build

%install
rm -rf %{buildroot} && mkdir -p %{buildroot}%{_bindir}/ && cd kotlinc
install -m 0755 bin/kotlin %{buildroot}%{_bindir}/
install -m 0755 bin/kotlin-dce-js %{buildroot}%{_bindir}/
install -m 0755 bin/kotlinc %{buildroot}%{_bindir}/
install -m 0755 bin/kotlinc-js %{buildroot}%{_bindir}/
install -m 0755 bin/kotlinc-jvm %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}/
install -m 0644 build.txt %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_datadir}/%{name}/lib/
install -m 0644 lib/* %{buildroot}%{_datadir}/%{name}/lib/
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
cd license/ && find * -type f -exec install -Dm 0644 {} %{buildroot}%{_datadir}/licenses/%{name}/{} \;
mkdir -p %buildroot%_docdir/%name
install -Dm644 %SOURCE1 %buildroot%_docdir/%name/

%fdupes %buildroot/%_datadir/licenses/%name/


%verifyscript
rm -rf test && mkdir test && cd test
cat <<EOT > test.kt
fun main(args: Array<String>) {
    println("Hello, world!")
}
EOT
kotlinc test.kt && kotlin TestKt
kotlinc test.kt -include-runtime -d test.jar
kotlinc-js test.kt -output test.js
kotlinc-jvm test.kt -include-runtime -d test.jar


%files
%{_bindir}/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/build.txt
%dir %{_datadir}/%{name}/lib/
%{_datadir}/%{name}/lib/*
%dir %{_datadir}/licenses/%{name}/
%{_datadir}/licenses/%{name}/*
%license kotlinc/license/LICENSE.txt
%doc ReadMe.md


%changelog
* Mon Apr 03 2023 Gonçalo Silva <goncalossilva@gmail.com> - 1.8.20-1
- Update to 1.8.20
* Thu Feb 02 2023 Gonçalo Silva <goncalossilva@gmail.com> - 1.8.10-1
- Update to 1.8.10
* Wed Dec 28 2022 Gonçalo Silva <goncalossilva@gmail.com> - 1.8.0-1
- Update to 1.8.0
* Wed Nov 09 2022 Gonçalo Silva <goncalossilva@gmail.com> - 1.7.21-1
- Update to 1.7.21
* Thu Sep 29 2022 Gonçalo Silva <goncalossilva@gmail.com> - 1.7.20-1
- Update to 1.7.20
* Fri Jul 08 2022 Gonçalo Silva <goncalossilva@gmail.com> - 1.7.10-1
- Update to 1.7.10
* Mon Jun 13 2022 Gonçalo Silva <goncalossilva@gmail.com> - 1.7.0-1
- Update to 1.7.0
* Mon Jun 13 2022 Gonçalo Silva <goncalossilva@gmail.com> - 1.6.21-1
- Update to 1.6.21
* Thu Jun 09 2022 Gonçalo Silva <goncalossilva@gmail.com> - 1.7.0-1
- Update to 1.7.0
* Wed Apr 20 2022 Gonçalo Silva <goncalossilva@gmail.com> - 1.6.21-1
- Update to 1.6.21
* Mon Apr 04 2022 Gonçalo Silva <goncalossilva@gmail.com> - 1.6.20-1
- Update to 1.6.20
* Tue Dec 14 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.6.10-1
- Update to 1.6.10
* Fri Dec 10 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.6.0-1
- Update to 1.6.0
* Mon Nov 29 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.5.32-1
- Update to 1.5.32
* Tue Nov 16 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.6.0-1
- Update to 1.6.0
* Mon Sep 20 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.5.31-1
- Update to 1.5.31
* Tue Aug 24 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.5.30-1
- Update to 1.5.30
* Tue Jul 13 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.5.21-1
- Update to 1.5.21
* Thu Jun 24 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.5.20-1
- Update to 1.5.20
* Mon May 24 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.5.10-1
- Update to 1.5.10
* Wed May 05 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.5.0-1
- Update to 1.5.0
* Tue Mar 30 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.4.32-1
- Update to 1.4.32
* Fri Feb 26 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.4.31-1
- Update to 1.4.31
* Wed Feb 03 2021 Gonçalo Silva <goncalossilva@gmail.com> - 1.4.30-1
- Update to 1.4.30
* Mon Jan 18 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.30-RC
* Mon Dec 07 2020 Gonçalo Silva <goncalossilva@gmail.com> - 1.4.21-1
- Update to 1.4.21
* Thu Nov 19 2020 Gonçalo Silva <goncalossilva@gmail.com> - 1.4.20-1
- Update to 1.4.20
* Thu Sep 10 2020 Gonçalo Silva <goncalossilva@gmail.com> - 1.4.10-1
- Update to 1.4.10
* Fri Aug 14 2020 Gonçalo Silva <goncalossilva@gmail.com> - 1.4.0-1
- Update to 1.4.0
* Sat Apr 18 2020 Gonçalo Silva <goncalossilva@gmail.com> - 1.3.72-1
- Update to 1.3.72
* Mon Apr 13 2020 Gonçalo Silva <goncalossilva@gmail.com> - 1.3.71-1
- Kotlin 1.3.71
