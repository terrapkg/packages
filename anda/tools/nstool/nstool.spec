%global debug_package %{nil}

%global ver v1.9.2
%global sanitized_ver %(echo "$( tr -d 'v' <<< %{ver} )")

Name:           nstool
Version:        %{sanitized_ver}
Release:        1%{?dist}
Summary:        General purpose read/extract tool for Nintendo Switch file formats

License:        MIT
URL:            https://github.com/jakcron/nstool

Packager:       sadlerm <lerm@chromebooks.lol>

BuildRequires:  make gcc gcc-c++
BuildRequires:  anda-srpm-macros

%description
General purpose reading/extraction tool for Nintendo Switch file formats.

%prep
%git_clone %{url} %{ver}

%build
%make_build deps
%make_build program

%install
install -Dm755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md SWITCH_KEYS.md
%{_bindir}/%{name}

