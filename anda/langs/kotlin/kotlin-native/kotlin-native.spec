%define _binaries_in_noarch_packages_terminate_build   0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Name:           kotlin-native
Version:        2.0.0
Release:        1%?dist
Summary:        LLVM backend for the Kotlin compiler
ExclusiveArch:  x86_64

License:        ASL 2.0
URL:            https://kotlinlang.org/docs/reference/native-overview.html
Source0:        https://github.com/JetBrains/kotlin/releases/download/v%{version}/kotlin-native-linux-x86_64-%{version}.tar.gz 

BuildRequires:  tar
BuildRequires:  sed
BuildRequires:  bash
BuildRequires:  (java-headless >= 1:1.8.0 or java >= 1.8.0)
Requires:       (java-headless >= 1:1.8.0 or java >= 1.8.0)
Requires:       ncurses-compat-libs
Suggests:       python
Suggests:       lldb


%description
Kotlin/Native is a technology for compiling Kotlin code to native binaries,
which can run without a virtual machine. It is an LLVM based backend for the
Kotlin compiler and native implementation of the Kotlin standard library.


%prep
tar -xf %{SOURCE0} && cd kotlin-native-linux-x86_64-%{version}
sed -i "s|\(DIR *= *\).*|\1%{_bindir}|" bin/*
sed -i "s|\(KONAN_HOME *= *\).*|\1%{_datadir}/%{name}|" bin/*


%build

%install
rm -rf %{buildroot} && mkdir -p %{buildroot}%{_bindir}/ && cd kotlin-native-linux-x86_64-%{version}
install -m 0755 bin/cinterop %{buildroot}%{_bindir}/
install -m 0755 bin/generate-platform %{buildroot}%{_bindir}/
install -m 0755 bin/jsinterop %{buildroot}%{_bindir}/
install -m 0755 bin/klib %{buildroot}%{_bindir}/
install -m 0755 bin/konanc %{buildroot}%{_bindir}/
install -m 0755 bin/konan-lldb %{buildroot}%{_bindir}/
install -m 0755 bin/kotlinc-native %{buildroot}%{_bindir}/
install -m 0755 bin/run_konan %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}/
for name in klib konan tools; do
    find "$name/" -type f -exec install -Dm 0644 {} %{buildroot}%{_datadir}/%{name}/{} \;
done
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/
cd licenses && find * -type f -exec install -Dm 0644 {} %{buildroot}%{_datadir}/licenses/%{name}/{} \;


%verifyscript
rm -rf test && mkdir test && cd test
cat <<EOT > test.kt
fun main(args: Array<String>) {
    println("Hello, world!")
}
EOT
kotlinc-native test.kt -o test
./test.kexe


%files
%{_bindir}/*
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/klib/
%{_datadir}/%{name}/klib/**
%dir %{_datadir}/%{name}/konan/
%{_datadir}/%{name}/konan/**
%dir %{_datadir}/%{name}/tools/
%{_datadir}/%{name}/tools/**
%dir %{_datadir}/licenses/%{name}/
%{_datadir}/licenses/%{name}/*
%license kotlin-native-linux-x86_64-%{version}/licenses/LICENSE.txt


%changelog
* Mon Apr 03 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.8.20
* Thu Feb 02 2023 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.8.10
* Wed Dec 28 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.8.0
* Wed Nov 09 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.7.21
* Thu Sep 29 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.7.20
* Fri Jul 08 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.7.10
* Mon Jun 13 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.7.0
* Mon Jun 13 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.6.21
* Thu Jun 09 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.7.0
* Wed Apr 20 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.6.21
* Mon Apr 04 2022 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.6.20
* Tue Dec 14 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.6.10
* Fri Dec 10 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.6.0
* Mon Nov 29 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.5.32
* Tue Nov 16 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.6.0
* Mon Sep 20 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.5.31
* Tue Aug 24 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.5.30
* Tue Jul 13 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.5.21
* Thu Jun 24 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.5.20
* Mon May 24 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.5.10
* Wed May 05 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.5.0
* Tue Mar 30 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.32
* Fri Feb 26 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.31
* Wed Feb 03 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.30
* Mon Jan 18 2021 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.30-RC
* Mon Dec 07 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.21
* Thu Nov 19 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.20
* Thu Sep 10 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.10
* Fri Aug 14 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.4.0
* Sat Apr 18 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Update to 1.3.72
* Mon Apr 13 2020 Gonçalo Silva <goncalossilva@gmail.com>
- Kotlin/Native 1.3.71
