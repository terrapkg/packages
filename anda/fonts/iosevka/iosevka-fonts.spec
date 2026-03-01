%define _iosevka_families Iosevka IosevkaAile IosevkaCurly IosevkaCurlySlab IosevkaEtoile IosevkaSS01 IosevkaSS02 IosevkaSS03 IosevkaSS04 IosevkaSS05 IosevkaSS06 IosevkaSS07 IosevkaSS08 IosevkaSS09 IosevkaSS10 IosevkaSS11 IosevkaSS12 IosevkaSS13 IosevkaSS14 IosevkaSS15 IosevkaSS16 IosevkaSlab

# HACK: Download prebuilt binaries instead of building from source
# 
# XXX: Use `--without bins` only if you enjoy waiting 33+ hours and death by
# a thousand JavaScript apps, or you use Gentoo.
%bcond_without bins

%bcond_without smt
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
    if rpm.expand("%{with bins}") == "1" then
        -- PkgTTC-Iosevka-33.3.3
        rpm.define(string.format("fonts%d %s/*.ttc", i, family))
        else
            if rpm.expand("%{with ttc}") == "1" then
                rpm.define(string.format("fonts%d dist/.ttc/%s/*.ttc", i, family))
            else
                rpm.define(string.format("fonts%d dist/%s/TTF/*.ttf", i, family))
        end
    end
    rpm.define(string.format("fontdescription%d %%fontdescription (%s)", i, pretty))
    i = i + 1
  end
  rpm.define(string.format("iosevka_family_count %d", i))
}



%global fontorg io.github.be5invis
%global fontlicense       OFL-1.1
%if %{with bins}
%global fontlicenses      Iosevka-%{version}/LICENSE.md
%else
%global fontlicenses      LICENSE.md
%endif
%global foundry           Belleve Invis
%global fontdescription   %{expand:
Versatile typeface for code, from code.}

Version:		34.2.0
Release:		1%?dist
Packager:       Cappy Ishihara <cappy@fyralabs.com>
Summary:		Versatile typeface for code, from code.
BuildRequires:  rpm_macro(fontpkg)
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
%if %{with bins}
BuildRequires:  curl
BuildRequires:  jq
BuildRequires:  aria2
BuildRequires:  unzip
%else
BuildRequires:  bun-bin
BuildRequires:  ttfautohint
%endif

%fontpkg -a
%fontmetapkg

%prep
%if %{with bins}
%setup -c

# TODO: Probably enhance by scripting RPM to add a `SourceN` directive instead
# download prebuilt binaries instead of building from source
# NOTE: May invite the ire of GitHub rate limiting since this pulls
# a LOT of assets in one go
curl https://api.github.com/repos/be5invis/Iosevka/releases/tags/v%{version} \
  | jq -r ".assets[] | .browser_download_url" | grep PkgTTC-Iosevka \
  | aria2c -i -

%else

%autosetup -n Iosevka-%{version}
bun i
%endif

%build

# XXX: Verda is VERY expensive when building fonts from source,
# which might be fine if you're building on a supercomputer with
# many cores and tons of RAM and lots of time to spare.
# 
# By default the SMT build is enabled in case you want to
# melt your computer by literally building fonts from source, see
# the `--with bin` option to disable prebuilt binaries
# 
# The build time is roughly ~1.5h * 22 = 33 hours on a quad-core
# machine with 32GB of RAM when building with maximum parallelism,
# so be warned.
# 
%if %{with smt}
%define _font_smp_flags --jCmd=%{_smp_build_ncpus}
%else
# However, we will be doing only 1 thread here to avoid
# thrashing builders
%define _font_smp_flags --jCmd=1
%endif


collections="%{_iosevka_families}"

%if %{with bins}
build_font() {
    local style=$1
    local zipfile="PkgTTC-${style}-%{version}.zip"
    unzip -d ${style}/ ${zipfile}
}
%else
build_font() {
    local style=$1
    bun run --bun build -- ttc::${style} %{_font_smp_flags}
}
%endif

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
