Name:           tectonic
Version:        0.12.0
Release:        %autorelease
Summary:        A modernized, complete, self-contained TeX/LaTeX engine, powered by XeTeX and TeXLive
URL:            https://github.com/tectonic-typesetting/tectonic
License:        MIT
Source0:        %{url}/archive/refs/tags/tectonic@%{version}.tar.gz
Requires:       openssl harfbuzz-icu libpng freetype graphite2 zlib fontconfig
BuildRequires:  cargo gcc gcc-c++ mold openssl-devel libpng-devel freetype graphite2-devel zlib-devel fontconfig-devel pkgconfig(icu-uc)

%description
Tectonic is a modernized, complete, self-contained TeX/LaTeX engine, powered by XeTeX and TeXLive.

%prep
%autosetup -n tectonic-tectonic-%{version}


# %build
# cargo build --features external-harfbuzz


%install
cargo install --path . --features external-harfbuzz


%files
%doc README.md
%license LICENSE 


%changelog
* Tue Nov 1 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
