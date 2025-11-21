%bcond bootstrap 1



Name:			bun
Version:		1.3.2
Release:		%autorelease
Summary:		Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one
License:		MIT
URL:			https://bun.sh

BuildRequires:	cmake
BuildRequires:	ninja-build
BuildRequires:	llvm19
BuildRequires:	clang19
BuildRequires:	lld19
BuildRequires:	sccache
BuildRequires:	cargo
BuildRequires:	libicu-devel
BuildRequires:glibc-devel
BuildRequires:	golang
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
%git_clone https://github.com/oven-sh/bun bun-v%{version}

%build
bun run  build:smol -DUSE_STATIC_LIBATOMIC=OFF -DCI=ON




%install

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
