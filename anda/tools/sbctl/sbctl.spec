%global appid  dev.linderud.sbctl
%global appstream_component console-application
%global patch_commit 14c4027270589b8d6f39cbca97569e6b13e40a05
Name:           sbctl
Version:        0.18
Release:        4%?dist
Summary:        Secure Boot key manager

License:        MIT
URL:            https://github.com/Foxboron/sbctl
Source0:        https://github.com/Foxboron/sbctl/releases/download/%{version}/sbctl-%{version}.tar.gz
Patch1:         https://github.com/Foxboron/sbctl/compare/master...%{patch_commit}.patch
## Based on CachyOS's batch sign script
# https://github.com/CachyOS/CachyOS-Settings/blob/master/usr/bin/sbctl-batch-sign
Source1:        %{name}-batch-sign

ExclusiveArch:  %{golang_arches}

Requires:       binutils
Requires:       util-linux
Requires(post): bash

Recommends:     systemd-udev

BuildRequires:  asciidoc
BuildRequires:  git
BuildRequires:  go-rpm-macros
BuildRequires:  anda-srpm-macros
BuildRequires:  pkgconfig(libpcsclite)

%description
sbctl intends to be a user-friendly secure boot key manager capable of setting
up secure boot, offer key management capabilities, and keep track of files that
needs to be signed in the boot chain.


%prep
%autosetup -p1

sed -i '/go build/d' Makefile


%build
export GOPATH=%{_builddir}/go
%global gomodulesmode GO111MODULE=on
%gobuild -o sbctl ./cmd/sbctl   
%make_build


%install
%make_install PREFIX=%{_prefix}
install -Dm755 %{SOURCE1} -t %{buildroot}%{_bindir}

# We don't want the Debian script
rm -f %{buildroot}%{_prefix}/lib/kernel/postinst.d/91-sbctl.install
%terra_appstream

%transfiletriggerin -P 1 -- /efi /usr/lib /usr/libexec
if [[ ! -f /run/ostree-booted ]] && grep -q -m 1 -e '\.efi$' -e '/vmlinuz$'; then
    exec </dev/null
    %{_bindir}/sbctl-batch-sign
fi


%files
%license LICENSE
%doc README.md
%{_bindir}/sbctl
%{_bindir}/sbctl-batch-sign
%{_prefix}/lib/kernel/install.d/91-sbctl.install
%{_mandir}/man8/sbctl.8*
%{_mandir}/man5/sbctl.conf.5*
%{_datadir}/bash-completion/completions/sbctl
%{_datadir}/fish/vendor_completions.d/sbctl.fish
%{_datadir}/zsh/site-functions/_sbctl
%{_metainfodir}/%{appid}.metainfo.xml


%changelog
* Sat May 24 2025 Esteve Fernandez <esteve@apache.org> - 0.17-2
- Do not run file triggers on atomic systems

* Sat Mar 30 2024 Cappy Ishihara <cappy@cappuchino.xyz> - 0.13-1
- Push to Terra

* Tue Dec 26 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 0.13-1
- Update to version 0.13

* Sun Nov 12 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 0.12-2
- Switch to upstream 91-sbctl.install kernel-install script

* Fri Oct 20 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 0.12-1
- Update to version 0.12

* Sat Mar 25 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 0.11-1
- Update to version 0.11

* Mon Dec 12 2022 Andrew Gunnerson <accounts+fedora@chiller3.com> - 0.10-1
- Update to version 0.10

* Tue May 3 2022 Andrew Gunnerson <chillermillerlong@hotmail.com> - 0.9-1
- Update to version 0.9

* Thu Jan 27 2022 Andrew Gunnerson <chillermillerlong@hotmail.com> - 0.8-1
- Initial release
