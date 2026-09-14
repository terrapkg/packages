%global extension   shatter-shell
%global uuid        %{extension}@adilhanney.com
%global appid       org.gnome.shell.extensions.%{extension}

Name:           gnome-shell-extension-%{extension}
Version:        2.2.0
Release:        2%{?dist}
Summary:        Advanced tiling window management extension for GNOME
License:        GPL-3.0-only
URL:            https://github.com/adil192/shatter-shell
Packager:       Adil Hanney <adilhanney@disroot.org>
BuildArch:      noarch

Source0:        %{url}/archive/refs/tags/%{version}/%{extension}-%{version}.tar.gz

Source1:        50_org.gnome.desktop.wm.keybindings.%{extension}.gschema.override
Source2:        50_org.gnome.mutter.%{extension}.gschema.override
Source3:        50_org.gnome.mutter.wayland.%{extension}.gschema.override
Source4:        50_org.gnome.settings-daemon.plugins.media-keys.%{extension}.gschema.override
Source5:        50_%{appid}.gschema.override
# downstream-only
Source6:        %{appid}.metainfo.xml
Patch:          0001-Remove-schema-handling-from-transpile.sh.patch

# START NPM SOURCES
Source100:      https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.10.1.tgz
Source101:      https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-3.4.3.tgz
Source102:      https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.12.2.tgz
Source103:      https://registry.npmjs.org/@eslint/config-array/-/config-array-0.23.5.tgz
Source104:      https://registry.npmjs.org/@eslint/config-helpers/-/config-helpers-0.7.0.tgz
Source105:      https://registry.npmjs.org/@eslint/core/-/core-1.2.1.tgz
Source106:      https://registry.npmjs.org/@eslint/js/-/js-10.0.1.tgz
Source107:      https://registry.npmjs.org/@eslint/object-schema/-/object-schema-3.0.5.tgz
Source108:      https://registry.npmjs.org/@eslint/plugin-kit/-/plugin-kit-0.7.3.tgz
Source109:      https://registry.npmjs.org/@girs/accountsservice-1.0/-/accountsservice-1.0-4.6.0.tgz
Source110:      https://registry.npmjs.org/@girs/adw-1/-/adw-1-4.6.0.tgz
Source111:      https://registry.npmjs.org/@girs/atk-1.0/-/atk-1.0-4.6.0.tgz
Source112:      https://registry.npmjs.org/@girs/cairo-1.0/-/cairo-1.0-4.6.0.tgz
Source113:      https://registry.npmjs.org/@girs/clutter-18/-/clutter-18-4.6.0.tgz
Source114:      https://registry.npmjs.org/@girs/cogl-18/-/cogl-18-4.6.0.tgz
Source115:      https://registry.npmjs.org/@girs/freetype2-2.0/-/freetype2-2.0-4.6.0.tgz
Source116:      https://registry.npmjs.org/@girs/gck-2/-/gck-2-4.6.0.tgz
Source117:      https://registry.npmjs.org/@girs/gcr-4/-/gcr-4-4.6.0.tgz
Source118:      https://registry.npmjs.org/@girs/gdesktopenums-3.0/-/gdesktopenums-3.0-4.6.0.tgz
Source119:      https://registry.npmjs.org/@girs/gdk-4.0/-/gdk-4.0-4.6.0.tgz
Source120:      https://registry.npmjs.org/@girs/gdkpixbuf-2.0/-/gdkpixbuf-2.0-4.6.0.tgz
Source121:      https://registry.npmjs.org/@girs/gdm-1.0/-/gdm-1.0-4.6.0.tgz
Source122:      https://registry.npmjs.org/@girs/gio-2.0/-/gio-2.0-4.6.0.tgz
Source123:      https://registry.npmjs.org/@girs/giounix-2.0/-/giounix-2.0-4.6.0.tgz
Source124:      https://registry.npmjs.org/@girs/gjs/-/gjs-4.6.0.tgz
Source125:      https://registry.npmjs.org/@girs/gl-1.0/-/gl-1.0-4.6.0.tgz
Source126:      https://registry.npmjs.org/@girs/glib-2.0/-/glib-2.0-4.6.0.tgz
Source127:      https://registry.npmjs.org/@girs/gmodule-2.0/-/gmodule-2.0-4.6.0.tgz
Source128:      https://registry.npmjs.org/@girs/gnome-shell/-/gnome-shell-50.0.4.tgz
Source129:      https://registry.npmjs.org/@girs/gnomebg-4.0/-/gnomebg-4.0-4.6.0.tgz
Source130:      https://registry.npmjs.org/@girs/gnomebluetooth-3.0/-/gnomebluetooth-3.0-4.6.0.tgz
Source131:      https://registry.npmjs.org/@girs/gnomedesktop-4.0/-/gnomedesktop-4.0-4.6.0.tgz
Source132:      https://registry.npmjs.org/@girs/gobject-2.0/-/gobject-2.0-4.6.0.tgz
Source133:      https://registry.npmjs.org/@girs/graphene-1.0/-/graphene-1.0-4.6.0.tgz
Source134:      https://registry.npmjs.org/@girs/gsk-4.0/-/gsk-4.0-4.6.0.tgz
Source135:      https://registry.npmjs.org/@girs/gtk-4.0/-/gtk-4.0-4.6.0.tgz
Source136:      https://registry.npmjs.org/@girs/gvc-1.0/-/gvc-1.0-4.6.0.tgz
Source137:      https://registry.npmjs.org/@girs/harfbuzz-0.0/-/harfbuzz-0.0-4.6.0.tgz
Source138:      https://registry.npmjs.org/@girs/meta-18/-/meta-18-4.6.0.tgz
Source139:      https://registry.npmjs.org/@girs/mtk-18/-/mtk-18-4.6.0.tgz
Source140:      https://registry.npmjs.org/@girs/nm-1.0/-/nm-1.0-4.6.0.tgz
Source141:      https://registry.npmjs.org/@girs/pango-1.0/-/pango-1.0-4.6.0.tgz
Source142:      https://registry.npmjs.org/@girs/pangocairo-1.0/-/pangocairo-1.0-4.6.0.tgz
Source143:      https://registry.npmjs.org/@girs/polkit-1.0/-/polkit-1.0-4.6.0.tgz
Source144:      https://registry.npmjs.org/@girs/polkitagent-1.0/-/polkitagent-1.0-4.6.0.tgz
Source145:      https://registry.npmjs.org/@girs/shell-18/-/shell-18-4.6.0.tgz
Source146:      https://registry.npmjs.org/@girs/shew-0/-/shew-0-4.6.0.tgz
Source147:      https://registry.npmjs.org/@girs/st-18/-/st-18-4.6.0.tgz
Source148:      https://registry.npmjs.org/@girs/upowerglib-1.0/-/upowerglib-1.0-4.6.0.tgz
Source149:      https://registry.npmjs.org/@girs/xfixes-4.0/-/xfixes-4.0-4.6.0.tgz
Source150:      https://registry.npmjs.org/@girs/xlib-2.0/-/xlib-2.0-4.6.0.tgz
Source151:      https://registry.npmjs.org/@humanfs/core/-/core-0.19.2.tgz
Source152:      https://registry.npmjs.org/@humanfs/node/-/node-0.16.8.tgz
Source153:      https://registry.npmjs.org/@humanfs/types/-/types-0.15.0.tgz
Source154:      https://registry.npmjs.org/@humanwhocodes/module-importer/-/module-importer-1.0.1.tgz
Source155:      https://registry.npmjs.org/@humanwhocodes/retry/-/retry-0.4.3.tgz
Source156:      https://registry.npmjs.org/@parcel/watcher/-/watcher-2.6.0.tgz
Source157:      https://registry.npmjs.org/@parcel/watcher-linux-arm-glibc/-/watcher-linux-arm-glibc-2.6.0.tgz
Source158:      https://registry.npmjs.org/@parcel/watcher-linux-arm-musl/-/watcher-linux-arm-musl-2.6.0.tgz
Source159:      https://registry.npmjs.org/@parcel/watcher-linux-arm64-glibc/-/watcher-linux-arm64-glibc-2.6.0.tgz
Source160:      https://registry.npmjs.org/@parcel/watcher-linux-arm64-musl/-/watcher-linux-arm64-musl-2.6.0.tgz
Source161:      https://registry.npmjs.org/@parcel/watcher-linux-x64-glibc/-/watcher-linux-x64-glibc-2.6.0.tgz
Source162:      https://registry.npmjs.org/@parcel/watcher-linux-x64-musl/-/watcher-linux-x64-musl-2.6.0.tgz
Source163:      https://registry.npmjs.org/@stylistic/eslint-plugin/-/eslint-plugin-5.10.0.tgz
Source164:      https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-4.2.1.tgz
Source165:      https://registry.npmjs.org/espree/-/espree-10.4.0.tgz
Source166:      https://registry.npmjs.org/@types/esrecurse/-/esrecurse-4.3.1.tgz
Source167:      https://registry.npmjs.org/@types/estree/-/estree-1.0.9.tgz
Source168:      https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz
Source169:      https://registry.npmjs.org/@typescript-eslint/eslint-plugin/-/eslint-plugin-8.69.0.tgz
Source170:      https://registry.npmjs.org/ignore/-/ignore-7.0.8.tgz
Source171:      https://registry.npmjs.org/@typescript-eslint/parser/-/parser-8.69.0.tgz
Source172:      https://registry.npmjs.org/@typescript-eslint/project-service/-/project-service-8.69.0.tgz
Source173:      https://registry.npmjs.org/@typescript-eslint/scope-manager/-/scope-manager-8.69.0.tgz
Source174:      https://registry.npmjs.org/@typescript-eslint/tsconfig-utils/-/tsconfig-utils-8.69.0.tgz
Source175:      https://registry.npmjs.org/@typescript-eslint/type-utils/-/type-utils-8.69.0.tgz
Source176:      https://registry.npmjs.org/@typescript-eslint/types/-/types-8.69.0.tgz
Source177:      https://registry.npmjs.org/@typescript-eslint/typescript-estree/-/typescript-estree-8.69.0.tgz
Source178:      https://registry.npmjs.org/@typescript-eslint/utils/-/utils-8.69.0.tgz
Source179:      https://registry.npmjs.org/@typescript-eslint/visitor-keys/-/visitor-keys-8.69.0.tgz
Source180:      https://registry.npmjs.org/typescript/-/typescript-7.0.2.tgz
Source181:      https://registry.npmjs.org/typescript/-/typescript-6.0.3.tgz
Source182:      https://registry.npmjs.org/@typescript/typescript-linux-arm/-/typescript-linux-arm-7.0.2.tgz
Source183:      https://registry.npmjs.org/@typescript/typescript-linux-arm64/-/typescript-linux-arm64-7.0.2.tgz
Source184:      https://registry.npmjs.org/@typescript/typescript-linux-loong64/-/typescript-linux-loong64-7.0.2.tgz
Source185:      https://registry.npmjs.org/@typescript/typescript-linux-mips64el/-/typescript-linux-mips64el-7.0.2.tgz
Source186:      https://registry.npmjs.org/@typescript/typescript-linux-ppc64/-/typescript-linux-ppc64-7.0.2.tgz
Source187:      https://registry.npmjs.org/@typescript/typescript-linux-riscv64/-/typescript-linux-riscv64-7.0.2.tgz
Source188:      https://registry.npmjs.org/@typescript/typescript-linux-s390x/-/typescript-linux-s390x-7.0.2.tgz
Source189:      https://registry.npmjs.org/@typescript/typescript-linux-x64/-/typescript-linux-x64-7.0.2.tgz
Source190:      https://registry.npmjs.org/acorn/-/acorn-8.18.0.tgz
Source191:      https://registry.npmjs.org/acorn-jsx/-/acorn-jsx-5.3.2.tgz
Source192:      https://registry.npmjs.org/ajv/-/ajv-6.15.0.tgz
Source193:      https://registry.npmjs.org/balanced-match/-/balanced-match-4.0.4.tgz
Source194:      https://registry.npmjs.org/brace-expansion/-/brace-expansion-5.0.9.tgz
Source195:      https://registry.npmjs.org/chokidar/-/chokidar-5.0.0.tgz
Source196:      https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz
Source197:      https://registry.npmjs.org/debug/-/debug-4.4.3.tgz
Source198:      https://registry.npmjs.org/deep-is/-/deep-is-0.1.4.tgz
Source199:      https://registry.npmjs.org/detect-libc/-/detect-libc-2.1.2.tgz
Source200:      https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-4.0.0.tgz
Source201:      https://registry.npmjs.org/eslint/-/eslint-10.9.1.tgz
Source202:      https://registry.npmjs.org/eslint-scope/-/eslint-scope-9.1.2.tgz
Source203:      https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-5.0.1.tgz
Source204:      https://registry.npmjs.org/espree/-/espree-11.2.0.tgz
Source205:      https://registry.npmjs.org/esquery/-/esquery-1.7.0.tgz
Source206:      https://registry.npmjs.org/esrecurse/-/esrecurse-4.3.0.tgz
Source207:      https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz
Source208:      https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source209:      https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source210:      https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
Source211:      https://registry.npmjs.org/fast-levenshtein/-/fast-levenshtein-2.0.6.tgz
Source212:      https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz
Source213:      https://registry.npmjs.org/file-entry-cache/-/file-entry-cache-8.0.0.tgz
Source214:      https://registry.npmjs.org/find-up/-/find-up-5.0.0.tgz
Source215:      https://registry.npmjs.org/flat-cache/-/flat-cache-4.0.1.tgz
Source216:      https://registry.npmjs.org/flatted/-/flatted-3.4.4.tgz
Source217:      https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz
Source218:      https://registry.npmjs.org/ignore/-/ignore-5.3.2.tgz
Source219:      https://registry.npmjs.org/immutable/-/immutable-5.1.9.tgz
Source220:      https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz
Source221:      https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz
Source222:      https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz
Source223:      https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source224:      https://registry.npmjs.org/json-buffer/-/json-buffer-3.0.1.tgz
Source225:      https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source226:      https://registry.npmjs.org/json-stable-stringify-without-jsonify/-/json-stable-stringify-without-jsonify-1.0.1.tgz
Source227:      https://registry.npmjs.org/keyv/-/keyv-4.5.4.tgz
Source228:      https://registry.npmjs.org/levn/-/levn-0.4.1.tgz
Source229:      https://registry.npmjs.org/locate-path/-/locate-path-6.0.0.tgz
Source230:      https://registry.npmjs.org/minimatch/-/minimatch-10.2.6.tgz
Source231:      https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
Source232:      https://registry.npmjs.org/natural-compare/-/natural-compare-1.4.0.tgz
Source233:      https://registry.npmjs.org/node-addon-api/-/node-addon-api-7.1.1.tgz
Source234:      https://registry.npmjs.org/optionator/-/optionator-0.9.4.tgz
Source235:      https://registry.npmjs.org/p-limit/-/p-limit-3.1.0.tgz
Source236:      https://registry.npmjs.org/p-locate/-/p-locate-5.0.0.tgz
Source237:      https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz
Source238:      https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz
Source239:      https://registry.npmjs.org/picomatch/-/picomatch-4.0.7.tgz
Source240:      https://registry.npmjs.org/prelude-ls/-/prelude-ls-1.2.1.tgz
Source241:      https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz
Source242:      https://registry.npmjs.org/readdirp/-/readdirp-5.1.1.tgz
Source243:      https://registry.npmjs.org/sass/-/sass-1.104.0.tgz
Source244:      https://registry.npmjs.org/semver/-/semver-7.8.5.tgz
Source245:      https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz
Source246:      https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz
Source247:      https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz
Source248:      https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.17.tgz
Source249:      https://registry.npmjs.org/ts-api-utils/-/ts-api-utils-2.5.0.tgz
Source250:      https://registry.npmjs.org/type-check/-/type-check-0.4.0.tgz
Source251:      https://registry.npmjs.org/@typescript/typescript6/-/typescript6-6.0.2.tgz
Source252:      https://registry.npmjs.org/typescript-eslint/-/typescript-eslint-8.69.0.tgz
Source253:      https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
Source254:      https://registry.npmjs.org/which/-/which-2.0.2.tgz
Source255:      https://registry.npmjs.org/word-wrap/-/word-wrap-1.2.5.tgz
Source256:      https://registry.npmjs.org/yocto-queue/-/yocto-queue-0.1.0.tgz
# END NPM SOURCES

BuildRequires:  anda-srpm-macros
BuildRequires:  nodejs
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-packaging
BuildRequires:  make
BuildRequires:  terra-appstream-helper

Requires:       gnome-shell >= 48
Recommends:     gnome-extensions-app
Recommends:     %{name}-shortcut-overrides = %{version}-%{release}
Provides:       %{extension} = %{version}-%{release}


%description
Shatter Shell is a keyboard-driven layer for GNOME Shell which allows for quick and
sensible navigation and management of windows.  The core feature of Shatter Shell
is the addition of advanced tiling window management - a feature that has been
highly sought within our community.  For many - ourselves included - i3wm has
become the leading competitor to the GNOME desktop.

Shatter Shell is a fork of Pop Shell.


%package shortcut-overrides
Summary:        Shortcut overrides for %{name}
Conflicts:      gnome-shell-extension-pop-shell-shortcut-overrides


%description shortcut-overrides
Shortcut overrides for %{name}.


%prep
%autosetup -p 1 -n %{extension}-%{version}
# START NPM CACHE ADD
%__npm cache add %{SOURCE100}
%__npm cache add %{SOURCE101}
%__npm cache add %{SOURCE102}
%__npm cache add %{SOURCE103}
%__npm cache add %{SOURCE104}
%__npm cache add %{SOURCE105}
%__npm cache add %{SOURCE106}
%__npm cache add %{SOURCE107}
%__npm cache add %{SOURCE108}
%__npm cache add %{SOURCE109}
%__npm cache add %{SOURCE110}
%__npm cache add %{SOURCE111}
%__npm cache add %{SOURCE112}
%__npm cache add %{SOURCE113}
%__npm cache add %{SOURCE114}
%__npm cache add %{SOURCE115}
%__npm cache add %{SOURCE116}
%__npm cache add %{SOURCE117}
%__npm cache add %{SOURCE118}
%__npm cache add %{SOURCE119}
%__npm cache add %{SOURCE120}
%__npm cache add %{SOURCE121}
%__npm cache add %{SOURCE122}
%__npm cache add %{SOURCE123}
%__npm cache add %{SOURCE124}
%__npm cache add %{SOURCE125}
%__npm cache add %{SOURCE126}
%__npm cache add %{SOURCE127}
%__npm cache add %{SOURCE128}
%__npm cache add %{SOURCE129}
%__npm cache add %{SOURCE130}
%__npm cache add %{SOURCE131}
%__npm cache add %{SOURCE132}
%__npm cache add %{SOURCE133}
%__npm cache add %{SOURCE134}
%__npm cache add %{SOURCE135}
%__npm cache add %{SOURCE136}
%__npm cache add %{SOURCE137}
%__npm cache add %{SOURCE138}
%__npm cache add %{SOURCE139}
%__npm cache add %{SOURCE140}
%__npm cache add %{SOURCE141}
%__npm cache add %{SOURCE142}
%__npm cache add %{SOURCE143}
%__npm cache add %{SOURCE144}
%__npm cache add %{SOURCE145}
%__npm cache add %{SOURCE146}
%__npm cache add %{SOURCE147}
%__npm cache add %{SOURCE148}
%__npm cache add %{SOURCE149}
%__npm cache add %{SOURCE150}
%__npm cache add %{SOURCE151}
%__npm cache add %{SOURCE152}
%__npm cache add %{SOURCE153}
%__npm cache add %{SOURCE154}
%__npm cache add %{SOURCE155}
%__npm cache add %{SOURCE156}
%__npm cache add %{SOURCE157}
%__npm cache add %{SOURCE158}
%__npm cache add %{SOURCE159}
%__npm cache add %{SOURCE160}
%__npm cache add %{SOURCE161}
%__npm cache add %{SOURCE162}
%__npm cache add %{SOURCE163}
%__npm cache add %{SOURCE164}
%__npm cache add %{SOURCE165}
%__npm cache add %{SOURCE166}
%__npm cache add %{SOURCE167}
%__npm cache add %{SOURCE168}
%__npm cache add %{SOURCE169}
%__npm cache add %{SOURCE170}
%__npm cache add %{SOURCE171}
%__npm cache add %{SOURCE172}
%__npm cache add %{SOURCE173}
%__npm cache add %{SOURCE174}
%__npm cache add %{SOURCE175}
%__npm cache add %{SOURCE176}
%__npm cache add %{SOURCE177}
%__npm cache add %{SOURCE178}
%__npm cache add %{SOURCE179}
%__npm cache add %{SOURCE180}
%__npm cache add %{SOURCE181}
%__npm cache add %{SOURCE182}
%__npm cache add %{SOURCE183}
%__npm cache add %{SOURCE184}
%__npm cache add %{SOURCE185}
%__npm cache add %{SOURCE186}
%__npm cache add %{SOURCE187}
%__npm cache add %{SOURCE188}
%__npm cache add %{SOURCE189}
%__npm cache add %{SOURCE190}
%__npm cache add %{SOURCE191}
%__npm cache add %{SOURCE192}
%__npm cache add %{SOURCE193}
%__npm cache add %{SOURCE194}
%__npm cache add %{SOURCE195}
%__npm cache add %{SOURCE196}
%__npm cache add %{SOURCE197}
%__npm cache add %{SOURCE198}
%__npm cache add %{SOURCE199}
%__npm cache add %{SOURCE200}
%__npm cache add %{SOURCE201}
%__npm cache add %{SOURCE202}
%__npm cache add %{SOURCE203}
%__npm cache add %{SOURCE204}
%__npm cache add %{SOURCE205}
%__npm cache add %{SOURCE206}
%__npm cache add %{SOURCE207}
%__npm cache add %{SOURCE208}
%__npm cache add %{SOURCE209}
%__npm cache add %{SOURCE210}
%__npm cache add %{SOURCE211}
%__npm cache add %{SOURCE212}
%__npm cache add %{SOURCE213}
%__npm cache add %{SOURCE214}
%__npm cache add %{SOURCE215}
%__npm cache add %{SOURCE216}
%__npm cache add %{SOURCE217}
%__npm cache add %{SOURCE218}
%__npm cache add %{SOURCE219}
%__npm cache add %{SOURCE220}
%__npm cache add %{SOURCE221}
%__npm cache add %{SOURCE222}
%__npm cache add %{SOURCE223}
%__npm cache add %{SOURCE224}
%__npm cache add %{SOURCE225}
%__npm cache add %{SOURCE226}
%__npm cache add %{SOURCE227}
%__npm cache add %{SOURCE228}
%__npm cache add %{SOURCE229}
%__npm cache add %{SOURCE230}
%__npm cache add %{SOURCE231}
%__npm cache add %{SOURCE232}
%__npm cache add %{SOURCE233}
%__npm cache add %{SOURCE234}
%__npm cache add %{SOURCE235}
%__npm cache add %{SOURCE236}
%__npm cache add %{SOURCE237}
%__npm cache add %{SOURCE238}
%__npm cache add %{SOURCE239}
%__npm cache add %{SOURCE240}
%__npm cache add %{SOURCE241}
%__npm cache add %{SOURCE242}
%__npm cache add %{SOURCE243}
%__npm cache add %{SOURCE244}
%__npm cache add %{SOURCE245}
%__npm cache add %{SOURCE246}
%__npm cache add %{SOURCE247}
%__npm cache add %{SOURCE248}
%__npm cache add %{SOURCE249}
%__npm cache add %{SOURCE250}
%__npm cache add %{SOURCE251}
%__npm cache add %{SOURCE252}
%__npm cache add %{SOURCE253}
%__npm cache add %{SOURCE254}
%__npm cache add %{SOURCE255}
%__npm cache add %{SOURCE256}
# END NPM CACHE ADD


%build
%make_build compile


%install
# install main extension files
%make_install

# install the schema file
install -D -p -m 0644 \
    schemas/%{appid}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml

# install the gnome-control-center keybindings
install -d -m 0755 %{buildroot}%{_datadir}/gnome-control-center/keybindings
install -p -m 0644 keybindings/*.xml %{buildroot}%{_datadir}/gnome-control-center/keybindings/

# install the schema override files
install -d -m 0755 %{buildroot}%{_datadir}/glib-2.0/schemas
install -p -m 0644 %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{buildroot}%{_datadir}/glib-2.0/schemas/

%terra_appstream -o %{SOURCE6}


%files
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_metainfodir}/%{appid}.metainfo.xml


%files shortcut-overrides
%{_datadir}/glib-2.0/schemas/*.%{extension}.gschema.override


%changelog
* Mon Sep 14 2026 Adil Hanney <adilhanney@disroot.org> - 2.2.0-2
- Port to Terra

* Sun Sep 13 2026 Adil Hanney <adilhanney@disroot.org> - 2.2.0-1
- New:
  - Ported the floating exceptions dialog and color chooser dialog to Adwaita/GTK4, and removed all imports of GTK3.
- Developer:
  - Minor cleanups:  this release is 121 lines slimmer

* Sat Sep 12 2026 Adil Hanney <adilhanney@disroot.org> - 2.1.0-1
- New:
  - Added keyboard shortcuts for horizontal workspaces by @laikq in https://github.com/pop-os/shell/pull/1777.
    (Pop!_OS previously only supported vertical workspaces.)
  - Added smarter floating exceptions:
    - Don't tile non-resizeable windows or non-moveable windows, e.g. Steam's sign-in dialog.
    - Don't tile windows with the "skip-taskbar" flag, e.g. XWaylandVideoBridge's invisible window.
    - This nets us wider compatibility and less reliance on an explicit floating exceptions list.
  - Performance improvement in determining which windows to tile by caching compiled RegExp objects.
- Fixed:
  - Ignore no-op stack resize grabs by @philip-sterne in https://github.com/pop-os/shell/pull/1826.
  - Fixed GNOME 48 crash if you click a tab's close button multiple times, based on @siddhpant's fix for https://github.com/pop-os/shell/issues/1794.
  - Replaced pop orange with adwaita blue in another spot that I forgot last release.
- Developer:
  - Suppressed a warning in `make enable` when you don't have the original pop-shell installed.
  - Minor cleanups: this release is 52 lines slimmer

* Fri Sep 11 2026 Adil Hanney <adilhanney@disroot.org> - 2.0.1-1
- New:
  - Improved the smoothness and symmetry of the fade transition between stacked windows.
  - Switched the default active hint color from Pop Orange to Adwaita Blue.
- Fixed:
  - Stack tabs are now clickable even in the 3px gap around each button.
  - Reduced possibility of a window getting stuck as transparent.
- Developer:
  - Formatted code with `@stylistic/eslint-plugin`.
  - Added `checked` attribute to stack tabs, possibly good for accessibility.
  - Improved safety of `window_exec` by passing the `Tab` directly instead of its index.

* Thu Sep 10 2026 Adil Hanney <adilhanney@disroot.org> - 2.0.0-1
- Features:
  - Rebranded from Pop Shell to Shatter Shell.
  - Added GNOME 51 support.
  - Added a setting to stop Shatter Shell from resetting your windows' positions when untiling.
  - Adwaita-themed tab bar for stacked windows: the tabs are bigger and easier to click, and fit in better with GNOME.
  - Added a fade transition when switching between stacked windows.
- Removals:
  - Removed pop-launcher (Super+/) integration in favor of GNOME's overview.
  - Removed system76-scheduler integration, since it's not common outside of Pop!_OS.
  - Removed the "Show Minimize to Tray Windows" setting in favor of stock GNOME Alt+Tab behavior.
  - Removed the "Show Window Titles" setting since it does nothing on Wayland.
- Fixes:
  - Fixed some tiling jank with a fixed `area_right` function.
    This can possibly be upstreamed but needs benchmarking to see if it's actually an improvement or just placebo.
  - Fixed brief flickers in active hints when tiling/untiling/moving windows.
- Floating window exceptions:
  - New: Steam sign-in dialog
  - New: Firefox Picture-in-Picture windows
  - New: Git Credential Manager login popups
  - New: Firefox "About" dialog
  - Fixed: Floating Window Exceptions config window
- Technical:
  - Replaced manual `.d.ts` bindings with `gjsify/gnome-shell`.
  - Updated to Typescript 7 for 10x faster builds and type checking.
  - Enabled eslint for code style and reducing dynamic types.
  - Removed legacy code for X11 and old GNOME versions (47 or older). This is now Wayland only, just like GNOME.
  - Added some basic CI to make sure code at least compiles.
