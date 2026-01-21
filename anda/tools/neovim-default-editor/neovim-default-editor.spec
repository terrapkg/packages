%global commit abde842fa612fccf0f665462b4bd0b721f6b8f0e

Name:          neovim-default-editor
# Version, release, and epoch are inherited from the editor package just like other default editors
Version:       0.11.5
Release:       1%?dist
Epoch: 0
# Inherited from Neovim itself
License:       Apache-2.0 AND Vim AND MIT
Summary:       Sets Neovim as the default editor
URL:           https://neovim.io
Source0:       https://raw.githubusercontent.com/terrapkg/pkg-neovim-default-editor/%{commit}/neovim-default-editor.csh
Source1:       https://raw.githubusercontent.com/terrapkg/pkg-neovim-default-editor/%{commit}/neovim-default-editor.sh
Source2:       https://raw.githubusercontent.com/terrapkg/pkg-neovim-default-editor/%{commit}/neovim-default-editor.fish
# For EVR macro
BuildRequires: anda-srpm-macros
Requires:      default-editor
Requires:      neovim
# All default editor packages MUST provide this
Provides:      system-default-editor
BuildArch:     noarch
Packager:      Gilver E. <roachy@fyralabs.com>

%description
This package ensures the EDITOR shell variable
is set in common shells to Neovim.

%build
# Nothing

%install
install -Dpm644 %{SOURCE0} -t %{buildroot}%{_sysconfdir}/profile.d/
install -Dpm644 %{SOURCE1} -t %{buildroot}%{_sysconfdir}/profile.d/
install -Dpm644 %{SOURCE2} -t %{buildroot}%{_datadir}/fish/vendor_conf.d/

%files
%dir %{_sysconfdir}/profile.d
%config(noreplace) %{_sysconfdir}/profile.d/neovim-default-editor.*
%dir %{_datadir}/fish/vendor_conf.d
%{_datadir}/fish/vendor_conf.d/neovim-default-editor.fish

%changelog
* Fri Jul 18 2025 Gilver E. <rockgrub@disroot.org> - 0.11.3-1
- Initial package
