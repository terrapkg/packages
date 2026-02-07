# not needed because this is a header only library
%global debug_package %{nil}

Name:           glaze-devel
Version:        7.0.2
Release:        1%?dist
License:        MIT
URL:            https://stephenberry.github.io/glaze
Source:         https://github.com/stephenberry/glaze/archive/refs/tags/v%{version}.tar.gz
Summary:        in memory JSON parsing and reflection library for modern C++
Packager:       metcya <metcya@gmail.com>

BuildRequires:  cmake
# even though we're not building anything, cmake still wants a c++ compiler
BuildRequires:  gcc-c++
BuildRequires:  mkdocs
BuildRequires:  mkdocs-material
BuildRequires:  python3-mkdocs-autorefs

%description
One of the fastest JSON libraries in the world. Glaze reads and writes from
object memory, simplifying interfaces and offering incredible performance.

%package -n glaze-docs
Summary:    Documentation files for glaze

%description -n glaze-docs
Documentation files for glaze.

%prep
%autosetup -n glaze-%{version}

%build
%cmake -Dglaze_DEVELOPER_MODE=OFF \
       -Dglaze_INSTALL_CMAKEDIR=%{_libdir}/cmake/glaze
mkdocs build

%install
%cmake_install
pushd site
find -type f -exec install -Dm 644 '{}' '%{buildroot}%{_pkgdocdir}/{}' \;
popd

%files
%license LICENSE
%doc README.md
%{_includedir}/glaze/
%{_libdir}/cmake/glaze/

%files -n glaze-docs
%license LICENSE
%{_pkgdocdir}/

%changelog
* Thu Dec 25 2025 metcya <metcya@gmail.com> - 6.4.0-2
- Install cmake files to correct location

* Wed Dec 24 2025 metcya <metcya@gmail.com> - 6.4.0-1
- Package glaze

