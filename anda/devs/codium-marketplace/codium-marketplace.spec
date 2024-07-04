# ref: https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=vscodium-marketplace

Name:       codium-marketplace
Version:    1.65.0
Release:    1%?dist
Summary:    Enable vscode marketplace in vscodium
License:    MIT
BuildArch:  noarch
URL:        https://marketplace.visualstudio.com/vscode
Requires:   codium sed

%description
This package replaces the default marketplace (https://open-vsx.org/)
to the official one used by vscode.

%install
touch dummy
install -Dm644 dummy %buildroot/tmp/terra-codium-marketplace-dummy-file

%posttrans
if [ $1 -gt 1 ]; then  # update/install
  sed -i -e 's/^[[:blank:]]*"serviceUrl":.*/    "serviceUrl": "https:\/\/marketplace.visualstudio.com\/_apis\/public\/gallery",/' \
    -e '/^[[:blank:]]*"cacheUrl/d' \
    -e '/^[[:blank:]]*"serviceUrl/a\    "cacheUrl": "https:\/\/vscode.blob.core.windows.net\/gallery\/index",' \
    -e 's/^[[:blank:]]*"itemUrl":.*/    "itemUrl": "https:\/\/marketplace.visualstudio.com\/items"/' \
    -e '/^[[:blank:]]*"linkProtectionTrustedDomains/d' \
    /usr/share/codium/resources/app/product.json || true
fi

%preun
sed -i -e 's/^[[:blank:]]*"serviceUrl":.*/    "serviceUrl": "https:\/\/open-vsx.org\/vscode\/gallery",/' \
  -e '/^[[:blank:]]*"cacheUrl/d' \
  -e 's/^[[:blank:]]*"itemUrl":.*/    "itemUrl": "https:\/\/open-vsx.org\/vscode\/item"/' \
  -e '/^[[:blank:]]*"linkProtectionTrustedDomains/d' \
  -e '/^[[:blank:]]*"documentationUrl/i\  "linkProtectionTrustedDomains": ["https://open-vsx.org"],' \
  /usr/share/codium/resources/app/product.json || true

%triggerin -- codium
sed -i -e 's/^[[:blank:]]*"serviceUrl":.*/    "serviceUrl": "https:\/\/marketplace.visualstudio.com\/_apis\/public\/gallery",/' \
  -e '/^[[:blank:]]*"cacheUrl/d' \
  -e '/^[[:blank:]]*"serviceUrl/a\    "cacheUrl": "https:\/\/vscode.blob.core.windows.net\/gallery\/index",' \
  -e 's/^[[:blank:]]*"itemUrl":.*/    "itemUrl": "https:\/\/marketplace.visualstudio.com\/items"/' \
  -e '/^[[:blank:]]*"linkProtectionTrustedDomains/d' \
  /usr/share/codium/resources/app/product.json || true

%files
/tmp/terra-codium-marketplace-dummy-file
