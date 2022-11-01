Name:           tectonic
Version:        0.12.0
Release:        %autorelease
Summary:        A modernized, complete, self-contained TeX/LaTeX engine, powered by XeTeX and TeXLive
URL:            https://github.com/tectonic-typesetting/tectonic
License:        MIT
Source0:        %{url}/archive/refs/tags/tectonic@%{version}.tar.gz
Requires:       r-openssl harfbuzz-icu libpng freetype graphite2 zlib fontconfig
BuildRequires:  cargo gcc gcc-c++ mold

%description
Tectonic is a modernized, complete, self-contained TeX/LaTeX engine, powered by XeTeX and TeXLive.

%build
cargo build


%install
cargo install


%files
%doc README.md
%license LICENSE 
