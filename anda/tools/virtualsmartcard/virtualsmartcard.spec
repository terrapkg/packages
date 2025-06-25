Name:           virtualsmartcard
Version:        0.10 
Release:        1%?dist
Summary:        Smart card emulator and driver for networked smart card reader/emulator
URL:            https://frankmorgner.github.io/vsmartcard/index.html
Source0:        https://github.com/frankmorgner/vsmartcard/releases/download/%name-%version/%name-%version.tar.gz
License:        GPL-3.0-only
BuildRequires:  pcsc-lite-devel gcc libtool pkg-config qrencode-devel python3-devel help2man

Requires:       qrencode-libs python3
Packager:       june-fish <git@june.fish>

%description
Virtual Smart Card emulates a smart card and makes it accessible through PC/SC. The vpcd is a smart card reader driver for PCSC-Lite and the windows smart card service. It allows smart card applications to access the vpicc through the PC/SC API.
 
%prep
%autosetup
autoreconf --verbose --install
%configure prefix=NONE pythondir=%{python3_sitelib} bindir=%{_bindir}
 
%build
%make_build
 
%install
%make_install prefix=NONE pythondir=%{python3_sitelib} bindir=%{_bindir}
 
%files
%{_bindir}/vicc
%{_mandir}/man1/vicc.1.gz
%{python3_sitelib}/virtualsmartcard/
%{python3_sitelib}/virtualsmartcard/cards/
%{_libdir}/pcsc/drivers/serial/libifdvpcd.so.%version
%{_libdir}/pcsc/drivers/serial/libifdvpcd.so
%{_sysconfdir}/reader.conf.d/vpcd
%{_bindir}/vpcd-config
%doc docs
 
%changelog
* Wed Jun 25 2025 june-fish <git@june.fish>
- Initial Package
