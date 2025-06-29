%global commit 31218294b0df40211e8573d08c178fb4d9c4bce5

Name:          micro-default-editor
# Version, release, and epoch are inherited from the editor package just like other default editors
Version:       2.0.11
Release:       10%{?dist}
Epoch:         0
# Inherited from Micro itself
License:       MIT and ASL 2.0
Summary:       Sets Micro as the default editor
URL:           https://github.com/zyedidia/micro
Source0:       https://raw.githubusercontent.com/terrapkg/pkg-micro-default-editor/%{commit}/micro-default-editor.csh
Source1:       https://raw.githubusercontent.com/terrapkg/pkg-micro-default-editor/%{commit}/micro-default-editor.sh
Source2:       https://raw.githubusercontent.com/terrapkg/pkg-micro-default-editor/%{commit}/micro-default-editor.fish
# For EVR macro
BuildRequires: anda-srpm-macros
Requires:      default-editor
Requires:      (micro = %{evr} or micro-nightly)
# All default editor packages MUST provide this
Provides:      system-default-editor
BuildArch:     noarch
Packager:      Gilver E. <rockgrub@disroot.org>

%description
This package ensures the EDITOR shell variable
is set in common shells to Micro.

%build
# Nothing

%install
install -Dpm644 %{SOURCE0} -t %{buildroot}%{_sysconfdir}/profile.d/
install -Dpm644 %{SOURCE1} -t %{buildroot}%{_sysconfdir}/profile.d/
install -Dpm644 %{SOURCE2} -t %{buildroot}%{_datadir}/fish/vendor_conf.d/

%files
%dir %{_sysconfdir}/profile.d
%config(noreplace) %{_sysconfdir}/profile.d/micro-default-editor.*
%dir %{_datadir}/fish/vendor_conf.d
%{_datadir}/fish/vendor_conf.d/micro-default-editor.fish

%changelog
* Sat Jun 28 2025 Gilver E. <rockgrub@disroot.org> - 2.0.11-10
- Initial package
