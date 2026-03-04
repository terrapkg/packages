Name:			depthcharge-tools
Version:		0.6.3
Release:		1%?dist
Summary:		Tools to manage the Chrome OS bootloader
License:		GPL-2.0-or-later
URL:			https://gitlab.postmarketos.org/postmarketOS/depthcharge-tools
Source0:		%url/-/archive/v%version/%name-v%version.tar.gz
Requires:		vboot-utils dtc gzip lz4 python3-setuptools uboot-tools vboot-utils xz
BuildRequires:	python3-setuptools python3-rpm-macros systemd-rpm-macros redhat-rpm-config python3-docutils
BuildArch:		noarch

%description
depthcharge-tools is a collection of tools that ease and automate interacting
with depthcharge, the Chrome OS bootloader.

%pkg_completion -Bz mkdepthcharge depthchargectl

%prep
%autosetup -n %name-v%version

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%buildroot
mkdir -p %buildroot/usr/lib/kernel/install.d %buildroot{%_unitdir,%bash_completions_dir,%zsh_completions_dir,%_mandir/man1}
install -Dm644 systemd/*.install %buildroot/usr/lib/kernel/install.d/
install -Dm644 systemd/*.service %buildroot%_unitdir/
install -Dm644 completions/_mkdepthcharge.bash %buildroot%bash_completions_dir/mkdepthcharge
install -Dm644 completions/_depthchargectl.bash %buildroot%bash_completions_dir/depthchargectl
install -Dm644 completions/_mkdepthcharge.zsh %buildroot%zsh_completions_dir/_mkdepthcharge
install -Dm644 completions/_depthchargectl.zsh %buildroot%zsh_completions_dir/_depthchargectl
rst2man mkdepthcharge.rst | gzip > mkdepthcharge.1.gz
rst2man depthchargectl.rst | gzip > depthchargectl.1.gz
install -Dm644 *.1.gz %buildroot%_mandir/man1/

%files
%doc README.rst
%license LICENSE
%_bindir/{mkdepthcharge,depthchargectl}
%_mandir/man1/{mkdepthcharge,depthchargectl}.1.gz
/usr/lib/kernel/install.d/90-depthcharge-tools.install
%_unitdir/depthchargectl-bless.service
%_prefix/lib/python%python3_version/site-packages/depthcharge_tools-%version-py%python3_version.egg-info/
%_prefix/lib/python%python3_version/site-packages/depthcharge_tools/

%changelog
%autochangelog
