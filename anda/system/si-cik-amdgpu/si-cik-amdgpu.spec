%global commit c0c7df418d9d5eb499b72f738fa4c9c4ee7fcbc6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250620

Name:             si-cik-amdgpu
Version:          0^%{commit_date}git.%{shortcommit}
Release:          1%{?dist}
Summary:          Modprobe config to enable the amdgpu drivers on Southern Islands (SI) and CIK (Sea Islands)
License:          GPL-3.0-only
URL:              https://github.com/terrapkg/pkg-si-cik-amdgpu
Source0:          %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
BuildRequires:    systemd-rpm-macros
Requires(post):   dracut
Requires(postun): dracut
BuildArch:        noarch
Packager:         Gilver E. <rockgrub@disroot.org>

%description
%{summary}.

Forcing these generations of cards to use the amdgpu driver generally improves performance, especially for gaming.

DISCLAIMER:
Using the amdgpu driver with SI and CIK GPUs is NOT officially supported.
You SHOULD NOT report any issues with doing so to AMD or Mesa.

Using this driver with these GPUs is known in some cases to cause a higher power draw.
If this is not a potential tradeoff you are comfortable with, please do not use this config.

%prep
%autosetup -n pkg-%{name}-%{commit}

%build
# [Crickets chirping]

%install
install -Dm644 amdgpu.conf -t %{buildroot}%{_modprobedir}

%post
dracut -f --regenerate-all

%postun
dracut -f --regenerate-all

%files
%doc README.md
%license LICENSE
%{_modprobedir}/amdgpu.conf

%changelog
* Fri Jun 20 2025 Gilver E. <rockgrub@disroot.org> - 0^20250620git.c0c7df4-1
- Initial package
