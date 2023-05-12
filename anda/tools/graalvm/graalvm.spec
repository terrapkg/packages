%global gsummary Universal virtual machine for running applications written in a variety of languages
%ifarch x86_64
%global garch amd64
%elifarch aarch64
%global garch aarch64
%endif
%global desc GraalVM is a high-performance JDK distribution designed to accelerate the execution of applications written in Java and other JVM languages along with support for JavaScript, Ruby, Python, and a number of other popular languages.

Name:		graalvm
Version:	22.3.2
Release:	1%{?dist}
URL:		https://www.graalvm.org/
Summary:	%{gsummary}
License:	GPL-2.0

%description
%{desc}

%define _p(v) %{expand:
%package jdk%1
Source%1: https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-%{version}/graalvm-ce-java%1-linux-%{garch}-%{version}.tar.gz
Summary: %{gsummary} (JDK %1)
%description jdk%1
%{desc}
JDK Version: %1
}

%_p 11
%_p 17
%dnl %_p 19

%prep
tar -xzf %{SOURCE11}
tar -xzf %{SOURCE17}
#tar -xzf %{SOURCE19}
ls

mv graalvm-ce-java11-%version/GRAALVM-README.md .


%build

%install
%define _i(v) %{expand:
    cd graalvm-ce-java%1-%{version}
    mkdir -p %{buildroot}/usr/lib/jvm/java-%1-graalvm/ %{buildroot}/usr/share/licenses/%{name}-jdk%1
    cp -a -t %{buildroot}/usr/lib/jvm/java-%1-graalvm/ *
    install -DTm644 LICENSE.txt %{buildroot}/usr/share/licenses/%{name}-jdk%1/LICENSE
    cd ..
}
%_i 11
%_i 17
#%_i 19

%files jdk11
%doc GRAALVM-README.md
%license LICENSE
/usr/lib/jvm/java-11-graalvm/

%files jdk17
%doc GRAALVM-README.md
%license LICENSE
/usr/lib/jvm/java-17-graalvm/

#%files jdk19
#%doc GRAALVM-README.md
#%license LICENSE
#/usr/lib/jvm/java-19-graalvm/

%changelog
* Thu May 11 2023 windowsboy111 <windowsboy111@fyralabs.com> - 22.3.2-1
- Remove jdk19
    
* Thu Feb 9 2023 windowsboy111 <windowsboy111@fyralabs.com> - 22.3.1-1
- Initial package
