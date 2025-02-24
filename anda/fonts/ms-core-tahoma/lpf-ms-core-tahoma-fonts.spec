# %%global will not work here, lazy evaluation needed.
%define         target_pkg %(t=%{name}; echo ${t#lpf-})

Name:           lpf-ms-core-tahoma-fonts
Version:        1.0
Release:        4%{?dist}
Summary:        Bootstrap package building mscore-tahoma-fonts using lpf
License:        MIT
URL:            https://github.com/leamas/lpf
Group:          Development/Tools
BuildArch:      noarch
Source0:        ms-core-tahoma-fonts.spec.in
Source1:        License.txt
Source2:        61-ms-core-tahoma.conf
BuildRequires:  desktop-file-utils
BuildRequires:  lpf
Requires:       lpf
Obsoletes:      lpf-mscore-tahoma-fonts


%description
Bootstrap package allowing the lpf system to build the
mscore-tahoma-fonts non-redistributable package.


%prep
%setup -cT


%build


%install
# lpf-setup-pkg [-e eula] <topdir> <specfile> [sources...]
/usr/share/lpf/scripts/lpf-setup-pkg -e %{SOURCE1} %{buildroot} %{SOURCE0} \
    %{SOURCE2}


%post
%lpf_post

%postun
%lpf_postun

%lpf_triggerpostun


%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}


%changelog
%autochangelog
