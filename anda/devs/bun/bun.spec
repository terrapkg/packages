%bcond bootstrap 1

%global forgeurl https://github.com/oven-sh/bun

%global tag bun-v1.3.2

%forgemeta

Name:			bun
Version:		1.3.2
Release:		%autorelease
Summary:		Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one
License:		MIT
URL:			https://bun.sh




Source0:		%{forgesource}

BuildRequires:	cmake
BuildRequires:	ninja-build
BuildRequires:	zig
BuildRequires:	llvm19
BuildRequires:	clang19
BuildRequires:	lld19
BuildRequires:	sccache
BuildRequires:	cargo
BuildRequires:	libicu-devel
BuildRequires:	libicu-devel
BuildRequires:	perl(Math::BigInt)
%if  %{with bootstrap}
BuildRequires:	bun-bin
%else
BuildRequires:	bun
%endif


Conflicts: bun-bin
ExclusiveArch: x86_64 aarch64

%description
%summary.


%prep
%{forgesetup}

%build
%cmake -G Ninja -DBUN_TEST=ON -DCI=ON -DUSE_STATIC_LIBATOMIC=OFF
%cmake_build



%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%_bindir/bun
%_bindir/bunx
%bash_completions_dir/bun.bash
%fish_completions_dir/bun.fish
%zsh_completions_dir/_bun

%changelog
%autochangelog
