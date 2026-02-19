Name:           python-yt-dlp-ejs
Version:        0.4.0
Release:        1%?dist
Summary:        External JavaScript for yt-dlp supporting many runtimes

License:        Unlicense AND MIT AND ISC
URL:            https://github.com/yt-dlp/ejs
Source:         %{pypi_source yt_dlp_ejs}
Packager:		madonuko <mado@fyralabs.com>

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  (deno or bun or nodejs-npm)


%global _description %{expand:
%summary.}

%description %_description

%package -n     python3-yt-dlp-ejs
Summary:        %{summary}
Provides:		yt-dlp-ejs = %evr
Requires:       (deno or bun or nodejs-npm)

%description -n python3-yt-dlp-ejs %_description


%prep
%autosetup -p1 -n yt_dlp_ejs-%{version}


#generate_buildrequires
#pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l yt_dlp_ejs


%check
%pyproject_check_import


%files -n python3-yt-dlp-ejs -f %{pyproject_files}
