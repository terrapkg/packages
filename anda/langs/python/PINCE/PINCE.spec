Name:           PINCE
Version:        0.10.1
Release:        1%?dist
Summary:        Reverse engineering tool for Linux
License:        GPL-3.0-or-later
URL:            https://korcankaraokcu.github.io/PINCE
Packager:       madonuko <mado@fyralabs.com>
Provides:       pince = %evr
ExclusiveArch:  x86_64
BuildRequires:  python3-devel
BuildRequires:  qt6-linguist
BuildRequires:  libmemscan
BuildRequires:  zig
BuildRequires:  python3dist(capstone)
# ↓ unmaintained since 2020
BuildRequires:  python3dist(keyboard)
# ↓ unmaintained since 2020
BuildRequires:  python3dist(keystone-engine)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(pyqt6)

%description
PINCE is a front-end/reverse engineering tool for the GNU Project Debugger (GDB), focused on games. However, it can be used for any reverse-engineering related stuff. PINCE is an abbreviation for "PINCE is not Cheat Engine".


%prep
%git_clone https://github.com/korcankaraokcu/PINCE

mkdir PINCE
for f in *; do
  if [ "$f" != "PINCE" ]; then
    cp -r $f PINCE/
  fi
done
cat<<EOF > pyproject.toml
[build-system]
requires = ["setuptools >= 77.0.3"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
py-modules = ["PINCE"]

[project.scripts]
pince = "PINCE:main"

[project]
name = "%name"
dynamic = ["version"]
dependencies = [
EOF
sed 's/^.*$/"\0",/' requirements.txt >> pyproject.toml
echo ']' >> pyproject.toml

sed 's@if __name__ == "__main__":@def main():@' -i PINCE/PINCE.py


%generate_buildrequires
%pyproject_buildrequires -r


%build
cp --preserve %_libdir/libmemscan.so libpince/libmemscan/
cp --preserve libmemscan/memscan.py libpince/libmemscan/
	
cd mono_collector
zig build -Doptimize=ReleaseFast -Dtarget=x86_64-linux-gnu
cp --preserve zig-out/lib/libmono_collector.so ../libpince/libmono_collector/mono_collector_x64.so
zig build -Doptimize=ReleaseFast -Dtarget=x86-linux-gnu
cp --preserve zig-out/lib/libmono_collector.so ../libpince/libmono_collector/mono_collector_x86.so
zig build -Doptimize=ReleaseFast -Dtarget=x86_64-windows-gnu
cp --preserve zig-out/bin/mono_collector.dll ../libpince/libmono_collector/mono_collector_wine_x64.dll
zig build -Doptimize=ReleaseFast -Dtarget=x86-windows-gnu
cp --preserve zig-out/bin/mono_collector.dll ../libpince/libmono_collector/mono_collector_wine_x86.dll
cd ..

lrelease-qt6 i18n/ts/*
mkdir -p i18n/qm
mv i18n/ts/*.qm i18n/qm/

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files PINCE


%files -f %{pyproject_files}
%doc README.md THANKS AUTHORS CONTRIBUTING.md
%license COPYING COPYING.CC-BY
%_bindir/pince
