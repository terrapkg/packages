%define _iosevka_families Iosevka IosevkaAile IosevkaCurly IosevkaCurlySlab IosevkaEtoile IosevkaSS01 IosevkaSS02 IosevkaSS03 IosevkaSS04 IosevkaSS05 IosevkaSS06 IosevkaSS07 IosevkaSS08 IosevkaSS09 IosevkaSS10 IosevkaSS11 IosevkaSS12 IosevkaSS13 IosevkaSS14 IosevkaSS15 IosevkaSS16 IosevkaSlab
%bcond_with smt
%bcond_with ttc

# this runs at macro expansion time, not build time
%{lua:
  local families = rpm.expand("%{_iosevka_families}")
  local i = 0
  local function prettify(name)
    -- insert space before uppercase letters (except first)
    local spaced = name:gsub("(%l)(%u)", "%1 %2")
    -- fix "SSxx" into "SSxx" (with space before)
    spaced = spaced:gsub("(%a)(SS%d+)", "%1 %2")
    return spaced
  end
  for family in string.gmatch(families, "%S+") do
    local pretty = prettify(family)
    rpm.define(string.format("fontfamily%d %s", i, pretty))
    if rpm.expand("%{with ttc}") == "1" then
      rpm.define(string.format("fonts%d dist/.ttc/%s/*.ttc", i, family))
    else
      rpm.define(string.format("fonts%d dist/%s/TTF/*.ttf", i, family))
    end
    rpm.define(string.format("fontdescription%d %%fontdescription (%s)", i, pretty))
    i = i + 1
  end
  rpm.define(string.format("iosevka_family_count %d", i))
}



%global fontorg io.github.be5invis
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.md
%global foundry           be5invis
%global fontdescription   %{expand:
Versatile typeface for code, from code.}

Version:		33.3.3
Release:		1%{?dist}
Packager:       Cappy Ishihara <cappy@fyralabs.com>
Summary:		Versatile typeface for code, from code.
BuildRequires:  rpm_macro(fontpkg)
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  nodejs-npm
BuildRequires:  ttfautohint

%fontpkg -a
%fontmetapkg

%prep
%autosetup -n Iosevka-%{version}
npm i

%build
font="Iosevka"

# If you love pain, consider using %%_smp_build_ncpus in jCmd
# to parallelize builds
#
%if %{with smt}
%define _font_smp_flags --jCmd=%{_smp_build_ncpus}
%else
# However, we will be doing only 1 thread here to avoid
# thrashing builders
%define _font_smp_flags --jCmd=1
%endif

collections="%{_iosevka_families}"

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
