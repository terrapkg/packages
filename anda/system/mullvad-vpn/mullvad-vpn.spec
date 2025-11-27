Name:          mullvad-vpn
Version:       2025.13
Release:       1%{?dist}
Summary:       The Mullvad VPN client app for desktop
SourceLicense: GPL-3.0-only
License:       ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 AND ISC) AND (Apache-2.0 OR BSD-3-Clause) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CC0-1.0 AND GPL-3.0-only AND ISC AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR BSD-3-Clause) AND (MIT OR MPL-2.0-or-later) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND WTFPL AND (Zlib OR Apache-2.0 OR MIT)
URL:           https://mullvad.net/en/vpn
Source0:       %{name}.preset
Patch0:        no-prebuilt-binaries.patch
BuildRequires: anda-srpm-macros
BuildRequires: cargo
BuildRequires: cargo-rpm-macros
BuildRequires: dbus-devel
BuildRequires: golang >= 1.21
BuildRequires: libxcrypt-compat
BuildRequires: mold
BuildRequires: pkgconfig(libnftnl)
BuildRequires: protobuf-devel
BuildRequires: systemd-rpm-macros
Requires:      dbus-libs
Requires:      libnotify
Requires:      libXScrnSaver
Packager:      Gilver E. <rockgrub@disroot.org>

%electronmeta -a

%description
Mullvad is a free and open source VPN especially focused on privacy and freedom.

%pkg_completion -Bfz mullvad

%package       doc
Summary:       Documentation for Mullvad VPN
BuildArch:     noarch

%description   doc
The mullvad-vpn-doc package contains documentation for Mullvad VPN.

%prep
%git_clone https://github.com/mullvad/mullvadvpn-app.git %{version}
%cargo_prep_online
%autopatch -p1

# This is run prior to build in Mullvad's CI
%{__cargo} clean

%build
%{cargo_build} -p mullvad-daemon --bin mullvad-daemon          \
        -p mullvad-cli --bin mullvad                           \
        -p mullvad-setup --bin mullvad-setup                   \
        -p mullvad-problem-report --bin mullvad-problem-report \
        -p talpid-openvpn-plugin --lib                         \
        -p mullvad-exclude --bin mullvad-exclude

mkdir -p build/shell-completions
for sh in bash fish zsh; do
  %{__cargo} run --bin mullvad -- shell-completions $sh build/shell-completions/
done
%{__cargo} run -p mullvad-api --bin relay_list > build/relays.json

cp target/rpm/{mullvad-daemon,mullvad,mullvad-problem-report,libtalpid_openvpn_plugin.so,mullvad-setup,mullvad-exclude} -t dist-assets

pushd desktop/packages/%{name}
%npm_build -c -e %{__nodejs} tasks/pack-linux.js
popd

%install
# Similar to crate_install_bin but this package has MULTIPLE Crates
%{__install} -Dm755 target/rpm/mullvad{,-daemon,-exclude} -t %{buildroot}%{_bindir}
%{__install} -Dm644 build/shell-completions/mullvad.bash %{buildroot}%{bash_completions_dir}/mullvad
%{__install} -Dm644 build/shell-completions/mullvad.fish -t %{buildroot}%{fish_completions_dir}
%{__install} -Dm644 build/shell-completions/_mullvad -t %{buildroot}%{zsh_completions_dir}
%{__install} -Dm644 dist-assets/linux/mullvad-{daemon,early-boot-blocking}.service -t %{buildroot}%{_unitdir}
%{__install} -Dm644 %{SOURCE0} -t %{buildroot}%{_presetdir}

%electron_install -D
# Extra symlink
ln -sf %{_libdir}/%{name}/resources/mullvad-problem-report %{buildroot}%{_bindir}/mullvad-problem-report

%{cargo_license_online} > LICENSE.dependencies

%pre
# Check if daemon is running, if it is, prepare the daemon for scriptlets.
# If a log exists, back it up for the user to check.
if which systemctl &> /dev/null && systemctl is-system-running | grep -vq offline &> /dev/null; then
    if systemctl status mullvad-daemon &> /dev/null; then
        %{_libdir}/%{name}/resources/mullvad-setup prepare-restart || true
        if stat /var/log/mullvad-vpn/daemon.log &> /dev/null; then
          cp /var/log/mullvad-vpn/daemon.log /var/log/mullvad-vpn/daemon.log.bak || echo "Mullvad log backup failed."
        fi
    fi
fi

rm -f /var/cache/mullvad-vpn/relays.json
rm -f /var/cache/mullvad-vpn/api-ip-address.txt

%preun
%systemd_preun mullvad-daemon.service
%systemd_preun mullvad-early-boot-blocking.service

# Internal daemon handling.
%{_libdir}/%{name}/resources/mullvad-setup reset-firewall || :
%{_libdir}/%{name}/resources/mullvad-setup remove-device || :

%postun
%systemd_postun_with_restart mullvad-daemon.service
%systemd_postun_with_restart mullvad-early-boot-blocking.service

%posttrans
%systemd_posttrans_with_restart mullvad-daemon.service
%systemd_posttrans_with_restart mullvad-early-boot-blocking.service

%files
%license LICENSE.md
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc README.md
%{_bindir}/mullvad
%{_bindir}/mullvad-daemon
%{_bindir}/mullvad-exclude
%{_bindir}/%{name}
%{_bindir}/mullvad-problem-report
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_unitdir}/mullvad-daemon.service
%{_unitdir}/mullvad-early-boot-blocking.service
%{_presetdir}/%{name}.preset
%{_iconsdir}/

%files doc
%doc docs/*
