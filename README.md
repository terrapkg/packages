# Terra Sources

[![Repository status](https://repology.org/badge/repository-big/terra_39.svg?header=Terra+39)](https://repology.org/repository/terra_39)
[![Repository status](https://repology.org/badge/repository-big/terra_40.svg?header=Terra+40)](https://repology.org/repository/terra_40)
[![Repository status](https://repology.org/badge/repository-big/terra_rawhide.svg?header=Terra+Rawhide)](https://repology.org/repository/terra_rawhide)

Terra is a rolling-release Fedora repository for all the software you need.
With Terra, you can install the latest packages knowing that quality and security are assured.

This monorepo contains the package manifests for all packages in Terra.

## Installation
```bash
sudo dnf config-manager --add-repo https://github.com/terrapkg/subatomic-repos/raw/main/terra.repo
```
You should also install the `terra-release` package so that when our infrastructure has any migrations, you can be assured that your Terra installation will still work as-is.

## Documentation
Our documentation can be found on our [Devdocs](https://developer.fyralabs.com/terra/). Alternatively, the GitHub Wiki contains older versions of the documentations.

## Questions?
Feel free to reach out on [Discord](https://discord.gg/5fdPuxTg5Q). We're always happy to help!
