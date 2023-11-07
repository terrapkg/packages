%undefine __brp_mangle_shebangs

Name:			gleam
Version:		0.32.3
Release:		1%{?dist}
Summary:		A friendly language for building type-safe, scalable systems
License:		Apache-2.0
URL:			https://gleam.run/
Source0:		https://github.com/gleam-lang/gleam/archive/v%version.tar.gz
Requires:		erlang elixir
BuildRequires:	cargo-rpm-macros anda-srpm-macros

%description
Gleam is a friendly language for building type-safe, scalable systems!
It compiles to Erlang (or JavaScript) and has straightforward interop with other BEAM languages such as Erlang, Elixir, and LFE.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/gleam %buildroot%_bindir/gleam

%files
%_bindir/gleam

%changelog
%autochangelog
