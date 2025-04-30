%global debug_package %{nil}

Name:			fuc
Version:		3.0.1
Release:		1%?dist
Summary:		Modern, performance focused unix commands
URL:			https://github.com/SUPERCILEX/fuc
Source0:		https://raw.githubusercontent.com/SUPERCILEX/fuc/%{version}/README.md
Source1:		https://raw.githubusercontent.com/SUPERCILEX/fuc/%{version}/LICENSE
%ifarch x86_64
Source2:		%{url}/releases/download/%{version}/x86_64-unknown-linux-gnu-rmz
Source3:		%{url}/releases/download/%{version}/x86_64-unknown-linux-gnu-cpz
%elifarch aarch64
Source2:		%{url}/releases/download/%{version}/aarch64-unknown-linux-gnu-rmz
Source3:		%{url}/releases/download/%{version}/aarch64-unknown-linux-gnu-cpz
%endif
License:		Apache-2.0
Requires:		cpz rmz

%description
Fast Unix Commands,
the FUC-ing project providing modern unix commands focused on performance.

%package -n rmz
Summary: Fast `rm` command from the FUC project

%description -n rmz
%{summary}. See the `fuc` package.

%package -n cpz
Summary: Fast `cp` command from the FUC project

%description -n cpz
%{summary}. See the `fuc` package.

%prep

%build

%install
install -Dm644 %{SOURCE0} "%{buildroot}/%{_datadir}/doc/%{name}/README.md"
install -Dm644 %{SOURCE1} "%{buildroot}/%{_datadir}/licenses/%{name}/LICENSE"
install -Dm644 %{SOURCE0} "%{buildroot}/%{_datadir}/doc/rmz/README.md"
install -Dm644 %{SOURCE1} "%{buildroot}/%{_datadir}/licenses/rmz/LICENSE"
install -Dm644 %{SOURCE0} "%{buildroot}/%{_datadir}/doc/cpz/README.md"
install -Dm644 %{SOURCE1} "%{buildroot}/%{_datadir}/licenses/cpz/LICENSE"
install -Dm755 %{SOURCE2} %{buildroot}/usr/bin/rmz
install -Dm755 %{SOURCE3} %{buildroot}/usr/bin/cpz

%files
%doc README.md
%license LICENSE

%files -n rmz
%doc README.md
%license LICENSE
/usr/bin/rmz

%files -n cpz
%doc README.md
%license LICENSE
/usr/bin/cpz
