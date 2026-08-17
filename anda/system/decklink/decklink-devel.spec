Name:           decklink-devel
Version:        14.4
Release:        1%{?dist}
Summary:        Blackmagic Design DeckLink SDK
License:        End User License Agreement for the Software Development Kit
URL:            https://www.blackmagicdesign.com/
BuildArch:      noarch

Source0:        https://github.com/terrapkg/pkg-decklink-devel/releases/download/%{version}/Blackmagic_DeckLink_SDK_%{version}.zip

%description
This SDK provides developer support for Desktop Video that allows updating
of hardware control and software interfaces for Desktop Video products.

%package        samples
Summary:        Sample files and documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description    samples
The %{name}-samples package contains documentation and samplese for the
DeckLink SDK.

%prep
%autosetup -c
mv Blackmagic\ DeckLink\ SDK\ %{version}/* .
rm -fr Blackmagic\ DeckLink\ SDK\ %{version}

rm -fr Mac Win Examples/Mac Examples/Win
rm -fr Examples/Linux/bin Linux/Samples/bin

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 0644 Linux/include/* %{buildroot}%{_includedir}

%files
%license "End User License Agreement.pdf"
%{_includedir}/*

%files samples
%doc ReadMe.rtf "Blackmagic DeckLink SDK.pdf"
%doc Examples/

%changelog
%autochangelog
