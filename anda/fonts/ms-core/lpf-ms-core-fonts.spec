%define         target_pkg %(t=%{name}; echo ${t#lpf-})

Name:           lpf-ms-core-fonts
Version:        2.2
Release:        1%{?dist}
Summary:        Bootstrap package building ms-core-fonts using lpf
License:        MIT
URL:            https://github.com/leamas/lpf
Group:          Development/Tools
BuildArch:      noarch
Source0:        ms-core-fonts.spec.in
Source1:        Licen.TXT
Source2:        61-ms-core-arial.conf
Source3:        61-ms-core-andale.conf
Source4:        61-ms-core-comic.conf
Source5:        61-ms-core-courier.conf
Source6:        61-ms-core-georgia.conf
Source7:        61-ms-core-impact.conf
Source8:        61-ms-core-times.conf
Source9:        61-ms-core-trebuchet.conf
Source10:       61-ms-core-verdana.conf
Source11:       61-ms-core-webdings.conf
BuildRequires:  desktop-file-utils
BuildRequires:  lpf
Requires:       lpf


%description
Bootstrap package allowing the lpf system to build the
ms-core-fonts non-redistributable package.


%prep
%setup -cT


%build


%install
# lpf-setup-pkg [-e eula] <topdir> <specfile> [sources...]
/usr/share/lpf/scripts/lpf-setup-pkg -e %{SOURCE1} %{buildroot} %{SOURCE0} \
    %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
    %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11}


%post
%lpf_post

%postun
%lpf_postun

%lpf_triggerpostun


%files
%{_datadir}/applications/lpf-ms-core-fonts.desktop
%{_datadir}/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}


%changelog
%autochangelog
