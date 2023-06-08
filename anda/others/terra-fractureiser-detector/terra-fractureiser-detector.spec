Name:			terra-fractureiser-detector
Version:		0
Release:		1%?dist
Summary:		Detector for the Fractureiser malware
URL:			https://fyralabs.com/minecraft/
Requires:		python3 pygobject2 libadwaita
Source0:		detect.py
License:		MIT

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

mkdir -p %buildroot/opt/%name
install -Dm755 %SOURCE0 %buildroot/opt/%name/

%posttrans
/usr/bin/python3 /opt/%name/detect.py


%files
%doc README
%license LICENSE
/opt/%name/detect.py

%changelog
* Fri Jun 9 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0-1
- Initial package.
