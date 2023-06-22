Name:			terra-fractureiser-detector
Version:		0
Release:		2%?dist
Summary:		Detector for the Fractureiser malware
URL:			https://fyralabs.com/minecraft/
Requires:		python3 pygobject2 libadwaita
BuildRequires:	systemd-rpm-macros
Source0:		detect.py
Source1:		fyra-fractureiser-detector.service
Source2:		fyra-fractureiser-detector.timer
Source3:		dialog.py
License:		MIT
BuildArch:		noarch

%description
This is a rapid security response for the detection of the Fractureiser malware.
For more info, see https://fyralabs.com/minecraft/.
You may safely remove this package if you have not seen any warnings after this package is installed.

%prep

%build

%install
cat <<EOF > README
This is a rapid security response for the detection of the Fractureiser malware.
For more info, see https://fyralabs.com/minecraft/.
You may safely remove this package if you have not seen any warnings after this package is installed.
EOF

cat <<EOF > LICENSE
Copyright © 2023 Fyra Labs

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
EOF

mkdir -p %buildroot/opt/%name %buildroot/%_unitdir # in case
install -Dm755 %SOURCE0 %buildroot/opt/%name/
install -Dm755 %SOURCE3 %buildroot/opt/%name/
install -Dm644 %SOURCE1 %buildroot/%_unitdir/
install -Dm644 %SOURCE2 %buildroot/%_unitdir/

%post
%systemd_post fyra-fractureiser-detector.timer
%systemd_post fyra-fractureiser-detector.service
if [ $1 -eq 1 ]; then
	systemctl enable --now fyra-fractureiser-detector.timer
fi

%preun
%systemd_preun fyra-fractureiser-detector.timer
%systemd_preun fyra-fractureiser-detector.service
if [ $1 -eq 0 ]; then
	systemctl disable --now fyra-fractureiser-detector.timer
fi

%postun
%systemd_postun_with_restart fyra-fractureiser-detector.timer
%systemd_postun_with_restart fyra-fractureiser-detector.service

%files
%doc README
%license LICENSE
/opt/%name/detect.py
/opt/%name/dialog.py
%_unitdir/fyra-fractureiser-detector.timer
%_unitdir/fyra-fractureiser-detector.service

%changelog
* Fri Jun 9 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0-1
- Initial package.
