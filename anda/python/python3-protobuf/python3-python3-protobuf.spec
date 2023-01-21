# Created by pyp2rpm-3.3.8
%global pypi_name python3-protobuf

Name:           python3-%{pypi_name}
Version:        2.5.0
Release:        1%{?dist}
Summary:        Protocol Buffers

License:        New BSD License
URL:            https://developers.google.com/protocol-buffers/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Protocol Buffers are Google's data interchange format.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# so apparently they decided to mix tabs and spaces
# dirty fix
sed "s@\t@    @g" google/protobuf/internal/cpp_message.py > google/protobuf/internal/cpp_message.py

%build
%py3_build

%install
%py3_install

%dnl %check
%dnl %{__python3} setup.py test

%files
%doc README.txt
%{python3_sitelib}/google/protobuf/compiler/plugin_pb2.py
%{python3_sitelib}/google/protobuf/descriptor.py
%{python3_sitelib}/google/protobuf/descriptor_database.py
%{python3_sitelib}/google/protobuf/descriptor_pb2.py
%{python3_sitelib}/google/protobuf/descriptor_pool.py
%{python3_sitelib}/google/protobuf/internal/api_implementation.py
%{python3_sitelib}/google/protobuf/internal/containers.py
%{python3_sitelib}/google/protobuf/internal/cpp_message.py
%{python3_sitelib}/google/protobuf/internal/decoder.py
%{python3_sitelib}/google/protobuf/internal/encoder.py
%{python3_sitelib}/google/protobuf/internal/enum_type_wrapper.py
%{python3_sitelib}/google/protobuf/internal/message_listener.py
%{python3_sitelib}/google/protobuf/internal/python_message.py
%{python3_sitelib}/google/protobuf/internal/type_checkers.py
%{python3_sitelib}/google/protobuf/internal/utils.py
%{python3_sitelib}/google/protobuf/internal/wire_format.py
%{python3_sitelib}/google/protobuf/message.py
%{python3_sitelib}/google/protobuf/message_factory.py
%{python3_sitelib}/google/protobuf/reflection.py
%{python3_sitelib}/google/protobuf/service.py
%{python3_sitelib}/google/protobuf/service_reflection.py
%{python3_sitelib}/google/protobuf/text_format.py
%{python3_sitelib}/google
%{python3_sitelib}/python3_protobuf-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/python3_protobuf-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Jan 08 2023 windowsboy111 <wboy111@outlook.com> - 2.5.0-1
- Initial package.
