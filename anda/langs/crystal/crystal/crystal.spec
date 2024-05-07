%define debug_package %nil

Name:			crystal
Version:		1.12.1
Release:		1%?dist
Summary:		The Crystal Programming Language
License:		Apache-2.0
URL:			https://crystal-lang.org/
Source0:		https://github.com/crystal-lang/crystal/releases/download/%version/crystal-%version-1-linux-x86_64-bundled.tar.gz
ExclusiveArch:	x86_64
BuildRequires:	rpm_macro(fdupes)

%description
%summary.

%package devel
Summary:	Development files for the crystal package

%description devel
%summary.

%prep
%autosetup -n crystal-%version-1

%build

%install
mkdir -p %buildroot/usr/bin
mkdir -p %buildroot/usr/share
mkdir -p %buildroot/usr/lib/crystal
install -Dm755 bin/* %buildroot/usr/bin/
cp -r share/* %buildroot/usr/share/
cp -r lib/crystal/* %buildroot/usr/lib/crystal/

%fdupes %buildroot%_datadir/crystal/src/lib_c/


%files
%license /usr/share/licenses/crystal/LICENSE
/usr/bin/crystal
/usr/share/zsh/site-functions/_crystal
/usr/share/man/man1/crystal.1.gz
/usr/share/crystal/
/usr/share/fish/vendor_completions.d/crystal.fish
/usr/share/bash-completion/completions/crystal

/usr/bin/shards
/usr/share/man/man1/shards.1.gz
/usr/share/man/man5/shard.yml.5.gz

%files devel
/usr/lib/crystal/

%changelog
* Sat Jun 17 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.8.2-2
- Add devel package.

* Sat Apr 15 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.8.0-1
- Initial package.

