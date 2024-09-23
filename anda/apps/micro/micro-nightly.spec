# https://github.com/zyedidia/micro
%global goipath        github.com/zyedidia/micro
%global commit         2259fd10affd19be60400a1ac2c86b920f2c64c2

%global shortcommit    %(c=%{commit}; echo ${c:0:7})
%global commit_date    20240731
%global compiledate    %(date "+%%B %%d, %%Y")

%gometa -f

%global goname         micro

%global common_description %{expand: 
Micro is a terminal-based text editor that aims to be easy to use and intuitive, while also taking advantage of the full capabilities of modern terminals.}

%global golicenses     LICENSE LICENSE-THIRD-PARTY
%global godocs         README.md

Name:           %{goname}-%{tag}
Version:        2.0.14~dev^%{commit_date}g%{shortcommit}
Release:        %autorelease
Summary:        A modern and intuitive terminal-based text editor
License:        MIT AND Apache-2.0 AND MPL-2.0
URL:            https://micro-editor.github.io
Source0:        %{gosource}

Recommends:     wl-clipboard xsel

%description
%{common_description}

%prep
%goprep
# fix go build requires
sed -i "s|github.com/zyedidia/json5|github.com/flynn/json5|" $(find . -name "*.go")

%build
%define build_version %(go run ./tools/build-version.go)
export LDFLAGS="-X 'github.com/zyedidia/micro/internal/util.Version=%build_version' \
                -X 'github.com/zyedidia/micro/internal/util.CommitHash=%{shortcommit}' \
                -X 'github.com/zyedidia/micro/internal/util.CompileDate=%{compiledate}' \
                -X 'github.com/zyedidia/micro/internal/util.Debug=OFF'"

# for syntax highlighting
export GOPATH='/usr/share/gocode/'
export GO111MODULE=off
go generate ./runtime

for cmd in cmd/* ; do
    %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%generate_buildrequires
%go_generate_buildrequires

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man1
cp -p ./assets/packaging/micro.1 %{buildroot}%{_mandir}/man1/

%check
%gocheck -d cmd/micro/shellwords -d cmd/micro/terminfo

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*
%{_mandir}/man1/micro.1.gz

%changelog
* Sat Aug  3 2024 davidusrex <dlunn@outlook.com>
- Initial package
