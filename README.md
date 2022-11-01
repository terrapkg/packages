# Terra repositories

This monorepo contains the package manifests for the Terra repositories.


# How to use
```bash
sudo dnf config-manager --add-repo https://github.com/terrapkg/subatomic-repos/raw/main/terra.repo
```
# Add packages
Pull requests are welcomed! See [here](docs/BUILDING.md) for instructions.
1. Add a new dir named after the package
1. Add `pkg.spec` and replace `pkg` with the name
1. See [here](https://rpm-packaging-guide.github.io/) for the RPM packaging guide (for writing a spec file)
1. Commit to a new branch then send a pull request
