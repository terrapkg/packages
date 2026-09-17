%global __arch_install_post /bin/true

# The annobin gcc plugin (baked into %%{optflags}/CFLAGS via
# -specs=.../redhat-annobin-cc1) isn't built for i686 multilib, so with it
# active a plain `-m32` compile fails at the "C compiler cannot create
# executables" autoconf sanity check before anything of ours even runs.
%undefine _annotated_build

# Shares Name: apparmor with the main spec - caused a debuginfo Name
# collision on Rakuos's fork of this spec. Disabled defensively.
%global debug_package %{nil}

Name:           apparmor
Version:        6.0.0~alpha1
Release:        1%{?dist}
Summary:        AppArmor userspace components (32-bit multilib libs)

%define baseversion %(echo %{version} | cut -d. -f-2)
%global normver %(echo %version | sed 's/~/-/')

License:        GPL-2.0-only
URL:            https://gitlab.com/apparmor/apparmor
Source0:        %url/-/archive/v%normver/apparmor-v%normver.tar.gz
Packager:       CatPieLeaf <catpieleaf@proton.me>

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  autoconf-archive
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gawk
BuildRequires:  which
BuildRequires:  libzstd-devel

%description
This is a trimmed-down i686 multilib-companion build of apparmor: just
libraries/libapparmor (the shared library + headers), with no python
bindings, parser, utils, pam, or httpd module. Those subpackages are
x86_64-only and are built from the full apparmor.spec instead - this
spec exists only so the i686 cross-build doesn't have to drag in
httpd-devel/pam-devel/etc. for pieces nobody uploads as i686.

%package      libs
Summary:      AppArmor library (32-bit)

%description  libs
32-bit multilib companion of apparmor-libs.

%package       devel
Summary:       AppArmor development libraries and header files (32-bit)
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
32-bit multilib companion of apparmor-devel.

%prep
%autosetup -n %name-v%normver

%conf
pushd libraries/libapparmor
./autogen.sh
# Built inside a real i686 arch mock chroot (native i686 gcc, no -m32/
# multilib hack needed) - plain %%configure is a native build here.
# --disable-man-pages: podchecker (perl-Pod-Checker) isn't guaranteed on
# every builder image, and man pages are arch-independent content already
# owned by the main apparmor-devel package - shipping them again here would
# just be a duplicate-file install conflict for no reason.
%configure --disable-man-pages || \
  { cat config.log; exit 1; }
popd

%build
pushd libraries/libapparmor
%make_build VERSION=%normver
popd

%install
%make_install -C libraries/libapparmor
find %{buildroot} \( -name "*.a" -o -name "*.la" \) -delete

%files libs
%license LICENSE
%{_libdir}/libapparmor.so.*

%files devel
%{_libdir}/libapparmor.so
%{_includedir}/aalogparse
%{_includedir}/sys/apparmor*
%{_libdir}/pkgconfig/libapparmor.pc

%changelog
* Fri Aug 07 2026 CatPieLeaf <catpieleaf@proton.me>
- Initial package - 32-bit multilib companion of apparmor-libs/apparmor-devel
