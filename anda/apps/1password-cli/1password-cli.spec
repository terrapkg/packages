%global debug_package %{nil}

%ifarch x86_64
%global op_arch amd64
%elifarch aarch64
%global op_arch arm64
%endif

Name:           1password-cli
Version:        2.34.1
Release:        2%{?dist}
Summary:        1Password command-line tool

Packager:       Cappy Ishihara <cappy@fyralabs.com>

License:        LicenseRef-1Password-Proprietary
URL:            https://developer.1password.com/docs/cli/
Source0:        https://cache.agilebits.com/dist/1P/op2/pkg/v%{version}/op_linux_%{op_arch}_v%{version}.zip
Source1:        1password-cli.sysusers
ExclusiveArch:  x86_64 aarch64

BuildRequires:  systemd-rpm-macros
BuildRequires:  unzip
Requires(post): /usr/bin/chown
Requires(post): /usr/bin/chmod
Recommends:     1password
Recommends:     polkit

%description
1Password CLI brings 1Password to your terminal.

%prep
%autosetup -c

%build

%install
install -Dm0755 op %{buildroot}%{_bindir}/op
chmod 2755 %{buildroot}%{_bindir}/op
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
/usr/bin/chown root:onepassword-cli %{_bindir}/op
/usr/bin/chmod 2755 %{_bindir}/op

%files
%{_bindir}/op
%{_sysusersdir}/%{name}.conf

%changelog
* Fri Jun 19 2026 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Package
