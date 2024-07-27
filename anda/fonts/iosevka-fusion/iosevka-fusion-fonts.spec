%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-fusion-fonts
Version:        31.0.0
Release:        1%?dist
Summary:        A custom font based on iosevka

License:        OFL-1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        iosevka-fusion.toml

BuildArch:      noarch

BuildRequires:  clang
BuildRequires:  nodejs-npm
BuildRequires:  ttfautohint

%description
Based on Iosevka font, https://github.com/be5invis/Iosevka,
this font mixes elements from various fonts tailored to my personal taste.

%prep
%autosetup -n %{source_name}-%{version}
%__cp %SOURCE1 %{_builddir}/%{source_name}-%{version}/private-build-plans.toml

%build
npm install
npm run build -- ttf::iosevka-fusion

%install
%__mkdir -p %{buildroot}%{_datadir}/fonts/%{name}

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-bold.ttf             \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Bold.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-bolditalic.ttf       \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-BoldItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-book.ttf             \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Book.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-bookitalic.ttf       \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-BookItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-extrabold.ttf        \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-ExtraBold.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-extrabolditalic.ttf  \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-ExtraBoldItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-extralight.ttf       \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-ExtraLight.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-extralightitalic.ttf \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-ExtraLightItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-heavy.ttf            \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Heavy.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-heavyitalic.ttf      \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-HeavyItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-italic.ttf           \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Italic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-light.ttf            \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Light.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-lightitalic.ttf      \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-LightItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-medium.ttf           \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Medium.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-mediumitalic.ttf     \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-MediumItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-regular.ttf          \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Regular.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-semibold.ttf         \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-SemiBold.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-semibolditalic.ttf   \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-SemiBoldItalic.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-thin.ttf             \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-Thin.ttf

%__install -m 0644                                                     \
           dist/iosevka-fusion/ttf/iosevka-fusion-thinitalic.ttf       \
           -T                                                          \
           %{buildroot}%{_datadir}/fonts/%{name}/IosevkaFusion-ThinItalic.ttf

%files
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/*

%changelog
* Wed Dec 28 2022 windowsboy111 <windowsboy111@fyralabs.com> - 16.8.4
- Initial package
