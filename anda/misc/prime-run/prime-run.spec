Name:           prime-run
Version:        1.0.0
Release:        1%{?dist}
Summary:        A simple script to run an application with NVIDIA PRIME GPU offloading

License:        MIT
URL:            https://terra.fyralabs.com
Source0:        prime-run.sh

# Bash script
Requires:       bash
BuildArch:      noarch

%description
A simple Bash script to force an application to run with PRIME GPU offloading. This is useful for
laptops with NVIDIA Optimus technology, where the integrated GPU is switchable alongside the dedicated
NVIDIA GPU. By default, the integrated GPU is used to save power, but this can be overridden for
specific applications using the prime-run script.

%prep


%build


%install
install -Dm755 %{SOURCE0} %{buildroot}%{_bindir}/prime-run


%files
%{_bindir}/prime-run



%changelog
* Sun Mar 03 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial release
