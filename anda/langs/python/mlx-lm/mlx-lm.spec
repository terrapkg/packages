%global pypi_name mlx-lm
%global _desc Run LLMs with MLX.

Name:			python-%{pypi_name}
Version:		0.31.3
Release:		1%?dist
Summary:		Run LLMs with MLX
License:		MIT
URL:			https://github.com/ml-explore/mlx-lm
Source0:		%{pypi_source mlx_lm}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mlx_lm

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/mlx_lm
%{_bindir}/mlx_lm.awq
%{_bindir}/mlx_lm.benchmark
%{_bindir}/mlx_lm.cache_prompt
%{_bindir}/mlx_lm.chat
%{_bindir}/mlx_lm.convert
%{_bindir}/mlx_lm.dwq
%{_bindir}/mlx_lm.dynamic_quant
%{_bindir}/mlx_lm.evaluate
%{_bindir}/mlx_lm.fuse
%{_bindir}/mlx_lm.generate
%{_bindir}/mlx_lm.gptq
%{_bindir}/mlx_lm.lora
%{_bindir}/mlx_lm.manage
%{_bindir}/mlx_lm.perplexity
%{_bindir}/mlx_lm.server
%{_bindir}/mlx_lm.share
%{_bindir}/mlx_lm.upload

%changelog
* Thu Sep 03 2026 Owen Zimmerman <owen@fyralabs.com> - 0.31.3-1
- Initial commit
