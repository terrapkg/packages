%global pypi_name markitdown
%global _desc %{expand:
MarkItDown is a lightweight Python utility for converting
various files to Markdown for use with LLMs and related text
analysis pipelines. To this end, it is most comparable to textract,
but with a focus on preserving important document structure and
content as Markdown (including: headings, lists, tables, links, etc.)
While the output is often reasonably presentable and human-friendly,
it is meant to be consumed by text analysis tools -- and may not be
the best option for high-fidelity document conversions for human consumption.
}

Name:			python-%{pypi_name}
Version:		0.1.6
Release:		1%{?dist}
Summary:		Python tool for converting files to Markdown
License:		MIT
URL:			https://github.com/microsoft/markitdown
Source0:		%{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-devel
BuildRequires:  python3-hatchling

Packager:	    Its-J <jonah@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires: python3-magika
Requires: python3-markdownify
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%package -n python3-%{pypi_name}-mcp
Summary:    Lightweight STDIO, Streamable HTTP, and SSE MCP server for calling MarkItDown
Requires:   python3-%{pypi_name} = %{evr}

%description -n python3-%{pypi_name}-mcp
%{summary}.

%package -n python3-%{pypi_name}-ocr
Summary:    LLM Vision plugin for MarkItDown that extracts text from images embedded in PDF, DOCX, PPTX, and XLSX files
Requires:   python3-%{pypi_name} = %{evr}

%description -n python3-%{pypi_name}-ocr
%{summary}.

%package -n python3-%{pypi_name}-sample-plugin
Summary:    Shows how to create a sample plugin for MarkItDown
Requires:   python3-%{pypi_name} = %{evr}

%description -n python3-%{pypi_name}-sample-plugin
%{summary}.

%prep
%autosetup -n markitdown-%{version}

%build
pushd packages/%{pypi_name}
%pyproject_wheel
popd
pushd packages/%{pypi_name}-mcp
%pyproject_wheel
popd
pushd packages/%{pypi_name}-ocr
%pyproject_wheel
popd
pushd packages/%{pypi_name}-sample-plugin
%pyproject_wheel
popd

%install
%pyproject_install
pushd packages/%{pypi_name}
%pyproject_install
popd
pushd packages/%{pypi_name}-mcp
%pyproject_install
popd
pushd packages/%{pypi_name}-ocr
%pyproject_install
popd
pushd packages/%{pypi_name}-sample-plugin
%pyproject_install
popd

%files -n python3-%{pypi_name}
%license LICENSE
%doc packages/%{pypi_name}/README.md
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.dist-info/*
%{python3_sitelib}/%{pypi_name}/converters/*.py
%{python3_sitelib}/%{pypi_name}/converters/__pycache__/*.pyc
%{python3_sitelib}/%{pypi_name}/*.py
%{python3_sitelib}/%{pypi_name}/py.typed
%{python3_sitelib}/%{pypi_name}/__pycache__/*.pyc
%{python3_sitelib}/%{pypi_name}/converter_utils/*.py
%{python3_sitelib}/%{pypi_name}/converter_utils/__pycache__/*.pyc
%{python3_sitelib}/%{pypi_name}/converter_utils/docx/*.py
%{python3_sitelib}/%{pypi_name}/converter_utils/docx/__pycache__/*.pyc
%{python3_sitelib}/%{pypi_name}/converter_utils/docx/math/*.py
%{python3_sitelib}/%{pypi_name}/converter_utils/docx/math/__pycache__/*.pyc

%files -n python3-%{pypi_name}-mcp
%doc packages/%{pypi_name}-mcp/README.md
%{_bindir}/%{pypi_name}-mcp
%{python3_sitelib}/%{pypi_name}_mcp/*.py
%{python3_sitelib}/%{pypi_name}_mcp/__pycache__/*.pyc
%{python3_sitelib}/%{pypi_name}_mcp/py.typed
%{python3_sitelib}/%{pypi_name}_mcp-*.dist-info/*

%files -n python3-%{pypi_name}-ocr
%doc packages/%{pypi_name}-ocr/README.md
%{python3_sitelib}/%{pypi_name}_ocr/*.py
%{python3_sitelib}/%{pypi_name}_ocr/__pycache__/*.pyc
%{python3_sitelib}/%{pypi_name}_ocr-*.dist-info/*

%files -n python3-%{pypi_name}-sample-plugin
%doc packages/%{pypi_name}-sample-plugin/README.md
%{python3_sitelib}/%{pypi_name}_sample_plugin/*.py
%{python3_sitelib}/%{pypi_name}_sample_plugin/__pycache__/*.pyc
%{python3_sitelib}/%{pypi_name}_sample_plugin-*.dist-info/*
%{python3_sitelib}/%{pypi_name}_sample_plugin/py.typed

%changelog
* Sun Jun 28 2026 Its-J <jonah@fyralabs.com> - 0.1.6-1
- Initial commit
