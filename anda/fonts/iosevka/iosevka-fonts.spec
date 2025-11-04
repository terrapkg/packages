
%global fontorg io.github.be5invis
# Enable this flag to build with SMT, if you have unlimited RAM
%bcond_with smt
Version:		33.3.3
Release:		1%{?dist}
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE
%global foundry           be5invis
%global common_description %{expand:
Versatile typeface for code, from code.
}
# hoo boy, this is gonna be a long one

Name:			iosevka-fonts
Provides:       %{name} = %{version}-%{release}
Packager:       Cappy Ishihara <cappy@fyralabs.com>
Summary:		Versatile typeface for code, from code.
License:		OFL-1.1
BuildRequires:  rpm_macro(fontpkg)
BuildArch:		noarch
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
# https://github.com/be5invis/Iosevka/archive/refs/tags/v33.3.3.tar.gz
BuildRequires:  nodejs-npm
BuildRequires:  ttfautohint

%description
%{common_description}

%global fontfamily1        Iosevka
%global fonts1             dist/Iosevka/TTF*.ttf


%fontpkg -a
%fontmetapkg
# pull in tlwg-laksaman-fonts
# since this actually provides a fix for TH Sarabun
# (#6929) (#2482)


%prep
%autosetup -n Iosevka-%{version}
npm i

%build
font="Iosevka"

# If you love pain, consider using %%_smp_build_ncpus in jCmd
# to parallelize builds
#
%if %{with smt}
%define _font_smp_flags --jcmd=%{_smp_build_ncpus}
%else
# However, we will be doing only 1 thread here to avoid
# thrashing builders
%define _font_smp_flags --jcmd=1
%endif

collections=$(grep '^\[collectPlans\.' build-plans.toml | grep -v '\[collectPlans\.[^.]*\.' | sed -E 's/^\[collectPlans\.([^.]+)\].*/\1/' | sort -u | tr '\n' ' ')

build_font() {
    local style=$1
    npm run build -- ttc::${style} %{_font_smp_flags}
}

for collection in $collections; do
    build_font "$collection"
done


%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a


%fontfiles -a


%changelog
%autochangelog
