# Creating a new package

## Prerequisites
- ensure the package doesn't exist in fedora repos
- avoid name coincide with other packages (including Fedora ones)

## Create dir struct
1. Change directory to `anda/`. If the package is related to any categories, `cd` into the corresponding folder.
    - For example, A Pantheon DE package goes into `anda/desktops/elementary/`.
    - If the category is undecided, it's ok to put it in `anda/`.
2. Let's say we are adding a package called `tic-tac-toe`. We are going to make a new directory and add some required files:
```sh
cd anda/games
mkdir tic-tac-toe
cd tic-tac-toe
touch anda.hcl tic-tac-toe.spec
```
3. Edit `anda.hcl`, which tells the [Andaman] toolchain how to build the package:
```hcl
project "pkg" {
    rpm {
        spec = "tic-tac-toe.spec"
    }
}
```
4. Edit the spec file `tic-tac-toe.spec`. It is an RPM spec file, and you are advised to read the documentation:
    - This [RPM Packaging Guide] might help newbies with no prior experiences with RPM specs.
    - This [Spec file format] docs goes into the details of the spec file format.
## Spec file
In general, you should state the name and the latest version of the package first.
1. Use `Release: %autorelease` unless you know what you are doing
2. The `License` field is required. If you don't know the license, check its repository page for the license file, or check other package repositories (such as the AUR) if it already exists there
3. State its dependencies with `Requires`
4. You will build the package. Add the `BulidRequires` packages
5. Add `Source0` or `Source1` or more. These preambles should link to a compressed file (preferably `tar`) and will be extracted during `%prep`
6. The source file will be automatically downloaded and extracted if you use `%autosetup -n <root dir name in tar file>` inside `%prep`. Check `blackbox-terminal.spec` as an example
7.  If it is not a tar archive, extract the file manually with a command. See `authy.spec` as an example (`unsquashfs`)
8. Inside `%build`, you might need to build the package. `%meson` and `%cmake` is supported. Check `blackbox-terminal` or `prismlauncher`
    - if not, manually state the command
9. Copy, move, install files or add symlinks in `%install`
10. List out all the files to be included inside `%files`
11. Add `%changelog` (message preferrably "Initial Package")

## Building
- Check if your new package builds. See [BUILDING.md]
```sh
anda build -c anda-37-x86_64 anda/games/tic-tac-toe/pkg
```
- If it doesn't build, fix your spec file and try again

## Finish
- Push and create a new PR


[Andaman]:  https://github.com/FyraLabs/anda
[RPM Packaging Guide]:  https://rpm-packaging-guide.github.io/
[Spec file format]:     https://rpm-software-management.github.io/rpm/manual/spec.html
[BUILDING.md]:  BUILDING.md
