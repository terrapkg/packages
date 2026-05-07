%bcond_without posix_2024
%bcond_without make_extensions

%global forgeurl https://github.com/rmyorston/pdpmake
%global tag 2.0.4
%forgemeta

Name:           pdpmake
Version:        %{tag}
Release:        1%{?dist}
Summary:        Public domain POSIX make 

Packager:       metcya <metcya@gmail.com>

License:        Unlicense
URL:            https://frippery.org/make
Source0:        %{forgesource}

BuildRequires:  gcc

%description
This is a public domain implementation of make which follows the POSIX
standard. 

%prep
%forgesetup

%build

%{__cc} -DENABLE_FEATURE_POSIX_2024=%{with_posix_2024} \
        -DENABLE_FEATURE_MAKE_EXTENSIONS=%{with_make_extensions} \
        $CFLAGS \
        $LDFLAGS \
        -o pdpmake \
        *.c

%install
install -Dm 755 pdpmake %{buildroot}%{_bindir}/pdpmake
install -Dm 644 pdpmake.1 %{buildroot}%{_mandir}/man1/pdpmake.1

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Jan 25 2026 metcya <metcya@gmail.com>
- Initial package
