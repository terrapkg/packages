%define _binaries_in_noarch_packages_terminate_build   0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Name:           kotlin-native
Version:        2.0.10
Release:        1%?dist
Summary:        LLVM backend for the Kotlin compiler
ExclusiveArch:  x86_64

License:        ASL 2.0
URL:            https://kotlinlang.org/docs/reference/native-overview.html
Source0:        https://github.com/JetBrains/kotlin/releases/download/v%version/kotlin-native-prebuilt-linux-x86_64-%version.tar.gz

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
tar -xf %{SOURCE0} && cd kotlin-native-prebuilt-linux-x86_64-%{version}
sed -i "s|\(DIR *= *\).*|\1%{_bindir}|" bin/*
sed -i "s|\(KONAN_HOME *= *\).*|\1%{_datadir}/%{name}|" bin/*


%build

%install
rm -rf %{buildroot} && mkdir -p %{buildroot}%{_bindir}/ && cd kotlin-native-prebuilt-linux-x86_64-%{version}
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
%autochangelog
- Kotlin/Native 1.3.71
