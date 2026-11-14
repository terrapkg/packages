# DMS Greeter - stable releases (Fedora/Copr), built from the vendored dank-greeter-<ver>.tar.gz release asset

%global debug_package %{nil}
%global pkg_summary DMS Greeter for greetd

%global goipath github.com/duxlabs-dev/dux-greeter/core
Name:           dms-greeter
Version:        2.1.2
Release:        1%{?dist}
Summary:        %{pkg_summary}

License:        MIT
URL:            https://github.com/duxlabs-dev/dux-greeter

BuildRequires:  golang
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  go-rpm-macros

Requires:       greetd
Requires(post): greetd
Requires:       (quickshell-git or quickshell)
Requires:       policycoreutils-python-utils
Requires(pre):  shadow-utils
Requires(post): shadow-utils

Conflicts:      dms-greeter-git

Recommends:     acl
Suggests:       niri
Suggests:       hyprland
Suggests:       sway

%gometa

%description
DMS Greeter is a greetd login screen with the Dux Shell aesthetic.
A single Go binary with the Quickshell UI embedded; the UI is extracted
to the greeter cache directory at startup.

Supports multiple compositors including Niri, Hyprland, Mango, and Sway with
session selection, user authentication, and dynamic theming synced from
Dux Shell.

%pkg_completion -Bfz

%prep
%git_clone
sed -i 's/CGO_ENABLED=0/CGO_ENABLED=1/g' core/Makefile
%goprep -Ae

%build
%global gomodulesmode GO111MODULE=on
%define currentgoldflags -X main.Version=%{version} -X main.BuildTime=%(date -u '+%%Y-%%m-%%d_%%H:%%M:%%S') -X main.Commit=release
%make_build VERSION=%{version} COMMIT=release BUILD_LDFLAGS=%{shescape:%{gobuildflags}} GO=%{shescape:%{?gobuilddir:GOPATH="%{gobuilddir}:${GOPATH:+${GOPATH}:}%{?gopath}"} %{?gomodulesmode} go}

%install
install -Dm755 core/bin/dms-greeter %{buildroot}%{_bindir}/dms-greeter

install -d %{buildroot}%{_datadir}/bash-completion/completions
install -d %{buildroot}%{_datadir}/zsh/site-functions
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
core/bin/dms-greeter completion bash > %{buildroot}%{_datadir}/bash-completion/completions/dms-greeter
core/bin/dms-greeter completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_dms-greeter
core/bin/dms-greeter completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/dms-greeter.fish

install -Dpm0644 assets/systemd/sysusers-dms-greeter.conf %{buildroot}%{_sysusersdir}/dms-greeter.conf
install -Dpm0644 assets/systemd/tmpfiles-dms-greeter.conf %{buildroot}%{_tmpfilesdir}/dms-greeter.conf

install -Dm644 LICENSE %{buildroot}%{_docdir}/dms-greeter/LICENSE
install -Dm644 README.md %{buildroot}%{_docdir}/dms-greeter/README.md
install -d %{buildroot}%{_docdir}/dms-greeter/examples
install -m644 assets/examples/* %{buildroot}%{_docdir}/dms-greeter/examples/

install -dm755 %{buildroot}%{_sharedstatedir}/greeter
install -dm750 %{buildroot}%{_localstatedir}/cache/dms-greeter

%files
%dir %{_docdir}/dms-greeter
%license %{_docdir}/dms-greeter/LICENSE
%doc %{_docdir}/dms-greeter/README.md
%doc %{_docdir}/dms-greeter/examples
%{_bindir}/dms-greeter
%{_sysusersdir}/dms-greeter.conf
%{_tmpfilesdir}/dms-greeter.conf
%dir %attr(0755,greeter,greeter) %{_sharedstatedir}/greeter
%dir %attr(0750,greeter,greeter) %{_localstatedir}/cache/dms-greeter

%pre
# Create greeter user/group if they don't exist
getent group greeter >/dev/null || groupadd -r greeter
getent passwd greeter >/dev/null || \
    useradd -r -g greeter -d %{_sharedstatedir}/greeter -s /bin/bash \
    -c "System Greeter" greeter
exit 0

%post

# Set SELinux contexts for greeter files on Fedora systems
if [ -x /usr/sbin/semanage ] && [ -x /usr/sbin/restorecon ]; then
    # Greeter launcher binary
    semanage fcontext -a -t bin_t '%{_bindir}/dms-greeter' >/dev/null 2>&1 || true
    restorecon %{_bindir}/dms-greeter >/dev/null 2>&1 || true

    # Greeter home directory
    semanage fcontext -a -t user_home_dir_t '%{_sharedstatedir}/greeter(/.*)?' >/dev/null 2>&1 || true
    restorecon -R %{_sharedstatedir}/greeter >/dev/null 2>&1 || true

    # Cache directory for greeter data (also holds the extracted embedded UI)
    semanage fcontext -a -t cache_home_t '%{_localstatedir}/cache/dms-greeter(/.*)?' >/dev/null 2>&1 || true
    restorecon -R %{_localstatedir}/cache/dms-greeter >/dev/null 2>&1 || true

    # PAM configuration
    restorecon %{_sysconfdir}/pam.d/greetd >/dev/null 2>&1 || true
fi

# follow the greetd user from config.toml like dms-greeter sync does
GREETER_USER=$(sed -n '/^\[default_session\]/,/^\[/s/^user *= *"\([^"]*\)".*/\1/p' /etc/greetd/config.toml 2>/dev/null | head -n1)
if [ -z "$GREETER_USER" ] || ! getent passwd "$GREETER_USER" >/dev/null 2>&1; then
    GREETER_USER=greeter
fi
chown -R "$GREETER_USER:greeter" %{_localstatedir}/cache/dms-greeter 2>/dev/null || true
chown -R greeter:greeter %{_sharedstatedir}/greeter 2>/dev/null || true

# Verify PAM configuration - only fix if insufficient, and never shadow greetd's own /usr/lib/pam.d/greetd
if [ ! -f /usr/lib/pam.d/greetd ]; then
PAM_CONFIG="/etc/pam.d/greetd"
if [ ! -f "$PAM_CONFIG" ]; then
    cat > "$PAM_CONFIG" << 'PAM_EOF'
#%PAM-1.0
auth       substack    system-auth
auth       include     postlogin

account    required    pam_nologin.so
account    include     system-auth

password   include     system-auth

session    required    pam_selinux.so close
session    required    pam_loginuid.so
session    required    pam_selinux.so open
session    optional    pam_keyinit.so force revoke
session    include     system-auth
session    include     postlogin
PAM_EOF
    chmod 644 "$PAM_CONFIG"
    # Only show message on initial install
    [ "$1" -eq 1 ] && echo "Created PAM configuration for greetd"
elif ! grep -q "pam_systemd\|system-auth" "$PAM_CONFIG"; then
    cp "$PAM_CONFIG" "$PAM_CONFIG.backup-dms-greeter"
    cat > "$PAM_CONFIG" << 'PAM_EOF'
#%PAM-1.0
auth       substack    system-auth
auth       include     postlogin

account    required    pam_nologin.so
account    include     system-auth

password   include     system-auth

session    required    pam_selinux.so close
session    required    pam_loginuid.so
session    required    pam_selinux.so open
session    optional    pam_keyinit.so force revoke
session    include     system-auth
session    include     postlogin
PAM_EOF
    chmod 644 "$PAM_CONFIG"
    # Only show message on initial install
    [ "$1" -eq 1 ] && echo "Updated PAM configuration (old config backed up to $PAM_CONFIG.backup-dms-greeter)"
fi
fi

# Auto-configure greetd config
GREETD_CONFIG="/etc/greetd/config.toml"
CONFIG_STATUS="Not modified (already configured)"

# Check if niri or hyprland exists
COMPOSITOR="niri"
if ! command -v niri >/dev/null 2>&1; then
        if command -v Hyprland >/dev/null 2>&1; then
                COMPOSITOR="hyprland"
        fi
fi

# If config doesn't exist, create a default one
if [ ! -f "$GREETD_CONFIG" ]; then
        mkdir -p /etc/greetd
        cat > "$GREETD_CONFIG" << 'GREETD_EOF'
[terminal]
vt = 1

[default_session]
user = "greeter"
command = "/usr/bin/dms-greeter --command COMPOSITOR_PLACEHOLDER"
GREETD_EOF
        sed -i "s|COMPOSITOR_PLACEHOLDER|$COMPOSITOR|" "$GREETD_CONFIG"
        CONFIG_STATUS="Created new config with $COMPOSITOR ✓"

elif ! grep -q "dms-greeter" "$GREETD_CONFIG"; then
        BACKUP_FILE="${GREETD_CONFIG}.backup-$(date +%%Y%%m%%d-%%H%%M%%S)"
        cp "$GREETD_CONFIG" "$BACKUP_FILE" 2>/dev/null || true

        # Update command in default_session section
        sed -i "/^\[default_session\]/,/^\[/ s|^command =.*|command = \"/usr/bin/dms-greeter --command $COMPOSITOR\"|" "$GREETD_CONFIG"
        sed -i '/^\[default_session\]/,/^\[/ s|^user =.*|user = "greeter"|' "$GREETD_CONFIG"
        CONFIG_STATUS="Updated existing config (backed up) with $COMPOSITOR ✓"
fi

# Set graphical.target as default
CURRENT_TARGET=$(systemctl get-default 2>/dev/null || echo "unknown")
if [ "$CURRENT_TARGET" != "graphical.target" ]; then
	systemctl set-default graphical.target >/dev/null 2>&1 || true
	TARGET_STATUS="Set to graphical.target (was: $CURRENT_TARGET) ✓"
else
	TARGET_STATUS="Already graphical.target ✓"
fi

# Only show banner on initial install
if [ "$1" -eq 1 ]; then
cat << 'EOF'

=========================================================================
        DMS Greeter Package Installed
=========================================================================

Status:
EOF
echo "    ✓ Greetd config: $CONFIG_STATUS"
echo "    ✓ Default target: $TARGET_STATUS"
cat << 'EOF'
    ✓ Greeter runtime account and directories prepared

Finish setup before rebooting:
1. Enable greetd and prepare runtime permissions/security labels:
     dms-greeter enable

2. Sync your existing DMS theme and settings to the greeter after reboot:
     dms-greeter sync

Verify with: dms-greeter status
Documentation: https://duxlabs.dev/docs/dms-greeter/
=========================================================================

EOF
fi

%postun
# Clean up SELinux contexts on package removal
if [ "$1" -eq 0 ] && [ -x /usr/sbin/semanage ]; then
    semanage fcontext -d '%{_bindir}/dms-greeter' 2>/dev/null || true
    semanage fcontext -d '%{_sharedstatedir}/greeter(/.*)?' 2>/dev/null || true
    semanage fcontext -d '%{_localstatedir}/cache/dms-greeter(/.*)?' 2>/dev/null || true
fi

%changelog
* Sun Nov 08 2026 github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com> - 1:2.1.2-1
- update to 2.1.2

* Fri Nov 06 2026 github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com> - 1:2.1.1-1
- update to 2.1.1

* Wed Nov 04 2026 github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com> - 1:2.1.0-1
- update to 2.1.0

* Sat Oct 24 2026 Avenge Media <AvengeMedia.US@gmail.com> - 1:2.0.0-2
- Packaging moved to dux-packaging; build from the vendored release tarball
  with the distro Go toolchain (GOTOOLCHAIN=auto) instead of bundled go.dev tarballs

* Sat Oct 17 2026 AvengeMedia <contact@avengemedia.com> - 1:2.0.0-1
- Stable release 2.0.0 built from the dank-greeter repository
- Greeter extracted from DankMaterialShell; the bash wrapper and the
  /usr/share/quickshell/dms-greeter QML tree are replaced by a single Go
  binary with the UI embedded
- Epoch bumped to 1 so the restarted 1.x versioning upgrades over the old
  DMS-versioned package
