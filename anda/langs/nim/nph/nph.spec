Name:           nph
Version:        0.6.0
Release:        1%?dist
Summary:        An opinionated code formatter for Nim
License:        MIT
URL:            https://github.com/arnetheduck/nph
Source0:        %url/archive/refs/tags/v%version.tar.gz
SourceLicense:  MIT
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  anda-srpm-macros
BuildRequires:  nim

%description
nph is an opinionated source code formatter for the Nim language, aiming to take the drudgery of manual formatting out of your coding day.

%prep
%autosetup
%nim_prep -t:"%nim_tflags" -l:"%nim_lflags"

%build
nimble c -d:release -t:"%nim_tflags" -l:"%nim_lflags" src/nph

%install
install -Dpm755 src/nph %buildroot%_bindir/nph

%files
%_bindir/nph
%license copying.txt
%doc README.md
